from datetime import date

from politylink.graphql.schema import Diet
from politylink.helpers.diet_finder import DietFinder


class TestDietFinder:
    def test_find(self):
        diets = [
            Diet({'id': 'Diet:0', 'startDate': encode_date(2000, 1, 1), 'endDate': encode_date(2000, 1, 31)}),
            Diet({'id': 'Diet:1', 'startDate': encode_date(2001, 1, 1), 'endDate': encode_date(2001, 1, 31)}),
        ]
        diet_finder = DietFinder(diets=diets)

        assert not diet_finder.find(date(1999, 12, 31))
        assert diet_finder.find_one(date(2000, 1, 1)).id == 'Diet:0'
        assert diet_finder.find_one(date(2000, 1, 31)).id == 'Diet:0'
        assert not diet_finder.find(date(2000, 2, 1))
        assert diet_finder.find_one(date(2001, 1, 15)).id == 'Diet:1'
        assert not diet_finder.find(date(2002, 1, 1))


def encode_date(year, month, day):
    return {'year': year, 'month': month, 'day': day}
