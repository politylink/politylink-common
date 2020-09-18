from politylink.graphql.schema import Committee
from politylink.helpers.committee_finder import CommitteeFinder


class TestCommitteeFinder:
    def test_find(self):
        committees = [
            Committee({'id': 'Committee:0', 'name': '衆議院環境委員会', 'aliases': ['衆環委']}),
            Committee({'id': 'Committee:1', 'name': '参議院環境委員会', 'aliases': ['参環委']}),
            Committee({'id': 'Committee:2', 'name': '参議院本会議'}),
        ]
        committee_finder = CommitteeFinder(committees)

        text = '環境委員会'
        assert len(committee_finder.find(text)) == 2
        assert committee_finder.find(text)[0].id == 'Committee:0'
        assert committee_finder.find(text)[1].id == 'Committee:1'

        text = '環委'
        assert len(committee_finder.find(text)) == 2
        assert committee_finder.find(text)[0].id == 'Committee:0'
        assert committee_finder.find(text)[1].id == 'Committee:1'

        text = '参議院本会議'
        assert len(committee_finder.find(text)) == 1
        assert committee_finder.find(text)[0].id == 'Committee:2'

        text = '第201回参議院本会議'
        assert len(committee_finder.find(text)) == 0
