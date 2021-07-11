from politylink.graphql.schema import ParliamentaryGroup

GROUP_NAMES = {
    ParliamentaryGroup.JIMIN: {'自民', '自由民主'},
    ParliamentaryGroup.RIKKEN: {'立民', '立憲'},
    ParliamentaryGroup.KOMEI: {'公明'},
    ParliamentaryGroup.KYOSAN: {'共産', '日本共産党'},
    ParliamentaryGroup.ISHIN: {'維新', '日本維新の会'},
    ParliamentaryGroup.KOKUMIN: {'国民'}
}


def to_parliamentary_group(s: str):
    for group, names in GROUP_NAMES.items():
        for name in names:
            if s.startswith(name):
                return group
    raise ValueError(f'failed to find parliamentary group: {s}')
