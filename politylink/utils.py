import os
import re
from datetime import datetime

from kanjize import kanji2int


def get_env_or_default(key, default):
    return os.environ[key] if key in os.environ else default


class DateConverter:
    pattern = r'(.*)年(.*)月(.*)日'
    era2year = {'明治': 1872, '大正': 1912, '昭和': 1925, '平成': 1989, '令和': 2019}

    @staticmethod
    def convert(s):
        """
        和暦の日付をdatetimeに変換する
        """

        m = re.fullmatch(DateConverter.pattern, s)
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
