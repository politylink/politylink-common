from datetime import datetime

from politylink.utils import DateConverter


class TestDateConverter:
    def test_convert(self):
        assert DateConverter.convert('令和元年10月11日') == datetime(year=2019, month=10, day=11)
        assert DateConverter.convert('令和2年一　月 ２日') == datetime(year=2020, month=1, day=2)
        assert DateConverter.convert('開会年月日　令和2年7月9日(閉会後)') == datetime(year=2020, month=7, day=9)
