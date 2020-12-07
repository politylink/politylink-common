from politylink.graphql.client import GraphQLClient


class CommitteeFinder:
    """
    Cache based Committee finder
    """

    def __init__(self, committees=None, **kwargs):
        if committees:
            self.committees = committees
        else:
            client = GraphQLClient(**kwargs)
            self.committees = client.get_all_committees(['id', 'name', 'aliases'])

    def find(self, text):
        return list(filter(lambda x: CommitteeFinder.match(x, text), self.committees))

    def find_one(self, text):
        committees = self.find(text)
        if len(committees) == 1:
            return committees[0]
        else:
            raise ValueError(f'found {len(committees)} committees that match with {text}:{committees}')

    @staticmethod
    def match(committee, text):
        if hasattr(committee, 'name') and committee.name:
            if text in committee.name or committee.name in text:
                return True
        if hasattr(committee, 'aliases') and committee.aliases:
            for alias in committee.aliases:
                if text in alias or alias in text:
                    return True
        return False
