import os
import re
import unicodedata
from datetime import datetime

from kanjize import kanji2int

KANSUJI = '〇一二三四五六七八九'
KANSUJI_DIGIT = '十百千万'


def get_env_or_default(key, default):
    return os.environ[key] if key in os.environ else default


def to_date_str(dt):
    return '{:02d}-{:02d}-{:02d}'.format(dt.year, dt.month, dt.day)


def filter_dict_by_value(dict_, num_items):
    """
    valueが大きい上位のitemに絞る
    """

    sorted_items = sorted(dict_.items(), key=lambda x: x[1], reverse=True)
    num_items = min(len(dict_), num_items)
    return dict(sorted_items[:num_items])


def filter_dict_by_thresh(dict_, thresh):
    """
    valueがthresh以上のitemに絞る
    """

    return dict(filter(lambda x: x[1] >= thresh, dict_.items()))


def contains_word(text, allow_list=None, block_list=None):
    """
    単語を含むか判定する
    allowとblockの両方が含まれていた場合はFalseを返す
    """

    allow_list = allow_list or list()
    block_list = block_list or list()
    has_allow_word = any(w in text for w in allow_list)
    has_block_word = any(w in text for w in block_list)
    return has_allow_word and not has_block_word


def strip_join(str_list, sep=''):
    return sep.join(map(lambda x: x.strip(), str_list))


def deduplicate(items):
    """
    順番を保持したままリストの重複を除く
    """

    return list(dict.fromkeys(items))


def convert_kansuji_to_int(s):
    buffer = ''
    sr = s[::-1]  # digitを後ろから変換する
    for i, si in enumerate(sr):
        if si in KANSUJI_DIGIT:
            zeros = KANSUJI_DIGIT.find(si) + 1
            if len(buffer) > zeros:
                raise ValueError(f'too many numbers before "{si}": {s}')
            buffer += '〇' * (zeros - len(buffer))  # 〇で桁を埋める
            if i == len(sr) - 1 or sr[i + 1] not in KANSUJI:
                buffer += '一'
        elif si in KANSUJI:
            buffer += si
        else:
            raise ValueError(f'found non-kansuji "{si}": {s}')
    return int(''.join([str(int(unicodedata.numeric(x))) for x in buffer[::-1]]))


def replace_kansuji_to_number(s):
    pattern = f'[{KANSUJI + KANSUJI_DIGIT}]+'
    return re.sub(pattern, lambda x: str(convert_kansuji_to_int(x.group(0))), s)


def get_str_offset(s):
    for i, c in enumerate(s):
        if c not in {' ', '　'}:
            return i
    return -1


class DateConverter:
    era2year = {'明治': 1872, '大正': 1912, '昭和': 1925, '平成': 1989, '令和': 2019}
    pattern = r'((?:明治|大正|昭和|平成|令和).*)年(.*)月(.*)日'

    @staticmethod
    def convert(s):
        """
        和暦の日付をdatetimeに変換する
        """

        m = re.search(DateConverter.pattern, s)
        if not m:
            raise ValueError(f'{s} does not fully match with {DateConverter.pattern}')
        year = DateConverter.convert_year_to_int(m.group(1))
        month = DateConverter.convert_to_int(m.group(2))
        day = DateConverter.convert_to_int(m.group(3))
        return datetime(year=year, month=month, day=day)

    @staticmethod
    def convert_year_to_int(s):
        s = s.strip()
        for era, year in DateConverter.era2year.items():
            if s.startswith(era):
                offset = DateConverter.convert_to_int(s[len(era):]) - 1
                return year + offset
        return DateConverter.convert_to_int(s)

    @staticmethod
    def convert_to_int(s):
        s = s.strip()
        if s.isdigit():
            return int(s)
        elif s == '元':
            return 1
        else:
            return kanji2int(s)
