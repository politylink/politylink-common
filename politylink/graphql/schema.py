import sgqlc.types


schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class BillCategory(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('KAKUHOU', 'SYUHOU', 'SANHOU')


class BillType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('NEW', 'AMENDMENT')


Boolean = sgqlc.types.Boolean

class ElectionType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CONSTITUENCY', 'PROPORTIONAL')


Float = sgqlc.types.Float

class House(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('SYUGIIN', 'SANGIIN')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

String = sgqlc.types.String

class _BillOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'billTitle_asc', 'billTitle_desc', 'billNumber_asc', 'billNumber_desc', 'billCategory_asc', 'billCategory_desc', 'billType_asc', 'billType_desc', 'submittedDate_asc', 'submittedDate_desc', 'passedSyugiinCommitteeDate_asc', 'passedSyugiinCommitteeDate_desc', 'passedSyugiinDate_asc', 'passedSyugiinDate_desc', 'passedSangiinCommitteeDate_asc', 'passedSangiinCommitteeDate_desc', 'passedSangiinDate_asc', 'passedSangiinDate_desc', 'proclaimedDate_asc', 'proclaimedDate_desc', '_id_asc', '_id_desc')


class _CommitteeOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'name_asc', 'name_desc', 'house_asc', 'house_desc', '_id_asc', '_id_desc')


class _DietOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'number_asc', 'number_desc', 'name_asc', 'name_desc', 'startDate_asc', 'startDate_desc', 'endDate_asc', 'endDate_desc', '_id_asc', '_id_desc')


class _ElectionOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'electionType_asc', 'electionType_desc', 'district_asc', 'district_desc', 'prefecture_asc', 'prefecture_desc', 'datetime_asc', 'datetime_desc', '_id_asc', '_id_desc')


class _LawOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'lawTitle_asc', 'lawTitle_desc', 'lawNumber_asc', 'lawNumber_desc', '_id_asc', '_id_desc')


class _MemberOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'name_asc', 'name_desc', 'nameHira_asc', 'nameHira_desc', 'firstName_asc', 'firstName_desc', 'firstNameHira_asc', 'firstNameHira_desc', 'lastName_asc', 'lastName_desc', 'lastNameHira_asc', 'lastNameHira_desc', 'house_asc', 'house_desc', '_id_asc', '_id_desc')


class _MinutesOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'minutesNumber_asc', 'minutesNumber_desc', 'startDateTime_asc', 'startDateTime_desc', 'endDateTime_asc', 'endDateTime_desc', '_id_asc', '_id_desc')


class _RelationDirections(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('IN', 'OUT')


class _TimelineOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'content_asc', 'content_desc', 'datetime_asc', 'datetime_desc', '_id_asc', '_id_desc')


class _UrlOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'url_asc', 'url_desc', 'domain_asc', 'domain_desc', 'title_asc', 'title_desc', 'description_asc', 'description_desc', '_id_asc', '_id_desc')



########################################################################
# Input Objects
########################################################################
class _BillFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'bill_title', 'bill_title_not', 'bill_title_in', 'bill_title_not_in', 'bill_title_contains', 'bill_title_not_contains', 'bill_title_starts_with', 'bill_title_not_starts_with', 'bill_title_ends_with', 'bill_title_not_ends_with', 'bill_number', 'bill_number_not', 'bill_number_in', 'bill_number_not_in', 'bill_number_contains', 'bill_number_not_contains', 'bill_number_starts_with', 'bill_number_not_starts_with', 'bill_number_ends_with', 'bill_number_not_ends_with', 'bill_category', 'bill_category_not', 'bill_category_in', 'bill_category_not_in', 'bill_type', 'bill_type_not', 'bill_type_in', 'bill_type_not_in', 'be_submitted_by_members', 'be_submitted_by_members_not', 'be_submitted_by_members_in', 'be_submitted_by_members_not_in', 'be_submitted_by_members_some', 'be_submitted_by_members_none', 'be_submitted_by_members_single', 'be_submitted_by_members_every', 'be_received_by_diet', 'be_received_by_diet_not', 'be_received_by_diet_in', 'be_received_by_diet_not_in', 'be_discussed_by_minutes', 'be_discussed_by_minutes_not', 'be_discussed_by_minutes_in', 'be_discussed_by_minutes_not_in', 'be_discussed_by_minutes_some', 'be_discussed_by_minutes_none', 'be_discussed_by_minutes_single', 'be_discussed_by_minutes_every', 'amended_laws', 'amended_laws_not', 'amended_laws_in', 'amended_laws_not_in', 'amended_laws_some', 'amended_laws_none', 'amended_laws_single', 'amended_laws_every', 'submitted_date', 'submitted_date_not', 'submitted_date_in', 'submitted_date_not_in', 'submitted_date_lt', 'submitted_date_lte', 'submitted_date_gt', 'submitted_date_gte', 'passed_syugiin_committee_date', 'passed_syugiin_committee_date_not', 'passed_syugiin_committee_date_in', 'passed_syugiin_committee_date_not_in', 'passed_syugiin_committee_date_lt', 'passed_syugiin_committee_date_lte', 'passed_syugiin_committee_date_gt', 'passed_syugiin_committee_date_gte', 'passed_syugiin_date', 'passed_syugiin_date_not', 'passed_syugiin_date_in', 'passed_syugiin_date_not_in', 'passed_syugiin_date_lt', 'passed_syugiin_date_lte', 'passed_syugiin_date_gt', 'passed_syugiin_date_gte', 'passed_sangiin_committee_date', 'passed_sangiin_committee_date_not', 'passed_sangiin_committee_date_in', 'passed_sangiin_committee_date_not_in', 'passed_sangiin_committee_date_lt', 'passed_sangiin_committee_date_lte', 'passed_sangiin_committee_date_gt', 'passed_sangiin_committee_date_gte', 'passed_sangiin_date', 'passed_sangiin_date_not', 'passed_sangiin_date_in', 'passed_sangiin_date_not_in', 'passed_sangiin_date_lt', 'passed_sangiin_date_lte', 'passed_sangiin_date_gt', 'passed_sangiin_date_gte', 'proclaimed_date', 'proclaimed_date_not', 'proclaimed_date_in', 'proclaimed_date_not_in', 'proclaimed_date_lt', 'proclaimed_date_lte', 'proclaimed_date_gt', 'proclaimed_date_gte', 'urls', 'urls_not', 'urls_in', 'urls_not_in', 'urls_some', 'urls_none', 'urls_single', 'urls_every', 'timelines', 'timelines_not', 'timelines_in', 'timelines_not_in', 'timelines_some', 'timelines_none', 'timelines_single', 'timelines_every')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_BillFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_BillFilter')), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(ID, graphql_name='id_contains')
    id_not_contains = sgqlc.types.Field(ID, graphql_name='id_not_contains')
    id_starts_with = sgqlc.types.Field(ID, graphql_name='id_starts_with')
    id_not_starts_with = sgqlc.types.Field(ID, graphql_name='id_not_starts_with')
    id_ends_with = sgqlc.types.Field(ID, graphql_name='id_ends_with')
    id_not_ends_with = sgqlc.types.Field(ID, graphql_name='id_not_ends_with')
    bill_title = sgqlc.types.Field(String, graphql_name='billTitle')
    bill_title_not = sgqlc.types.Field(String, graphql_name='billTitle_not')
    bill_title_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='billTitle_in')
    bill_title_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='billTitle_not_in')
    bill_title_contains = sgqlc.types.Field(String, graphql_name='billTitle_contains')
    bill_title_not_contains = sgqlc.types.Field(String, graphql_name='billTitle_not_contains')
    bill_title_starts_with = sgqlc.types.Field(String, graphql_name='billTitle_starts_with')
    bill_title_not_starts_with = sgqlc.types.Field(String, graphql_name='billTitle_not_starts_with')
    bill_title_ends_with = sgqlc.types.Field(String, graphql_name='billTitle_ends_with')
    bill_title_not_ends_with = sgqlc.types.Field(String, graphql_name='billTitle_not_ends_with')
    bill_number = sgqlc.types.Field(String, graphql_name='billNumber')
    bill_number_not = sgqlc.types.Field(String, graphql_name='billNumber_not')
    bill_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='billNumber_in')
    bill_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='billNumber_not_in')
    bill_number_contains = sgqlc.types.Field(String, graphql_name='billNumber_contains')
    bill_number_not_contains = sgqlc.types.Field(String, graphql_name='billNumber_not_contains')
    bill_number_starts_with = sgqlc.types.Field(String, graphql_name='billNumber_starts_with')
    bill_number_not_starts_with = sgqlc.types.Field(String, graphql_name='billNumber_not_starts_with')
    bill_number_ends_with = sgqlc.types.Field(String, graphql_name='billNumber_ends_with')
    bill_number_not_ends_with = sgqlc.types.Field(String, graphql_name='billNumber_not_ends_with')
    bill_category = sgqlc.types.Field(BillCategory, graphql_name='billCategory')
    bill_category_not = sgqlc.types.Field(BillCategory, graphql_name='billCategory_not')
    bill_category_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BillCategory)), graphql_name='billCategory_in')
    bill_category_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BillCategory)), graphql_name='billCategory_not_in')
    bill_type = sgqlc.types.Field(BillType, graphql_name='billType')
    bill_type_not = sgqlc.types.Field(BillType, graphql_name='billType_not')
    bill_type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BillType)), graphql_name='billType_in')
    bill_type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BillType)), graphql_name='billType_not_in')
    be_submitted_by_members = sgqlc.types.Field('_MemberFilter', graphql_name='beSubmittedByMembers')
    be_submitted_by_members_not = sgqlc.types.Field('_MemberFilter', graphql_name='beSubmittedByMembers_not')
    be_submitted_by_members_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MemberFilter')), graphql_name='beSubmittedByMembers_in')
    be_submitted_by_members_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MemberFilter')), graphql_name='beSubmittedByMembers_not_in')
    be_submitted_by_members_some = sgqlc.types.Field('_MemberFilter', graphql_name='beSubmittedByMembers_some')
    be_submitted_by_members_none = sgqlc.types.Field('_MemberFilter', graphql_name='beSubmittedByMembers_none')
    be_submitted_by_members_single = sgqlc.types.Field('_MemberFilter', graphql_name='beSubmittedByMembers_single')
    be_submitted_by_members_every = sgqlc.types.Field('_MemberFilter', graphql_name='beSubmittedByMembers_every')
    be_received_by_diet = sgqlc.types.Field('_DietFilter', graphql_name='beReceivedByDiet')
    be_received_by_diet_not = sgqlc.types.Field('_DietFilter', graphql_name='beReceivedByDiet_not')
    be_received_by_diet_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_DietFilter')), graphql_name='beReceivedByDiet_in')
    be_received_by_diet_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_DietFilter')), graphql_name='beReceivedByDiet_not_in')
    be_discussed_by_minutes = sgqlc.types.Field('_MinutesFilter', graphql_name='beDiscussedByMinutes')
    be_discussed_by_minutes_not = sgqlc.types.Field('_MinutesFilter', graphql_name='beDiscussedByMinutes_not')
    be_discussed_by_minutes_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='beDiscussedByMinutes_in')
    be_discussed_by_minutes_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='beDiscussedByMinutes_not_in')
    be_discussed_by_minutes_some = sgqlc.types.Field('_MinutesFilter', graphql_name='beDiscussedByMinutes_some')
    be_discussed_by_minutes_none = sgqlc.types.Field('_MinutesFilter', graphql_name='beDiscussedByMinutes_none')
    be_discussed_by_minutes_single = sgqlc.types.Field('_MinutesFilter', graphql_name='beDiscussedByMinutes_single')
    be_discussed_by_minutes_every = sgqlc.types.Field('_MinutesFilter', graphql_name='beDiscussedByMinutes_every')
    amended_laws = sgqlc.types.Field('_LawFilter', graphql_name='amendedLaws')
    amended_laws_not = sgqlc.types.Field('_LawFilter', graphql_name='amendedLaws_not')
    amended_laws_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_LawFilter')), graphql_name='amendedLaws_in')
    amended_laws_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_LawFilter')), graphql_name='amendedLaws_not_in')
    amended_laws_some = sgqlc.types.Field('_LawFilter', graphql_name='amendedLaws_some')
    amended_laws_none = sgqlc.types.Field('_LawFilter', graphql_name='amendedLaws_none')
    amended_laws_single = sgqlc.types.Field('_LawFilter', graphql_name='amendedLaws_single')
    amended_laws_every = sgqlc.types.Field('_LawFilter', graphql_name='amendedLaws_every')
    submitted_date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='submittedDate')
    submitted_date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='submittedDate_not')
    submitted_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='submittedDate_in')
    submitted_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='submittedDate_not_in')
    submitted_date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='submittedDate_lt')
    submitted_date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='submittedDate_lte')
    submitted_date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='submittedDate_gt')
    submitted_date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='submittedDate_gte')
    passed_syugiin_committee_date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSyugiinCommitteeDate')
    passed_syugiin_committee_date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSyugiinCommitteeDate_not')
    passed_syugiin_committee_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedSyugiinCommitteeDate_in')
    passed_syugiin_committee_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedSyugiinCommitteeDate_not_in')
    passed_syugiin_committee_date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSyugiinCommitteeDate_lt')
    passed_syugiin_committee_date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSyugiinCommitteeDate_lte')
    passed_syugiin_committee_date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSyugiinCommitteeDate_gt')
    passed_syugiin_committee_date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSyugiinCommitteeDate_gte')
    passed_syugiin_date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSyugiinDate')
    passed_syugiin_date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSyugiinDate_not')
    passed_syugiin_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedSyugiinDate_in')
    passed_syugiin_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedSyugiinDate_not_in')
    passed_syugiin_date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSyugiinDate_lt')
    passed_syugiin_date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSyugiinDate_lte')
    passed_syugiin_date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSyugiinDate_gt')
    passed_syugiin_date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSyugiinDate_gte')
    passed_sangiin_committee_date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSangiinCommitteeDate')
    passed_sangiin_committee_date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSangiinCommitteeDate_not')
    passed_sangiin_committee_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedSangiinCommitteeDate_in')
    passed_sangiin_committee_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedSangiinCommitteeDate_not_in')
    passed_sangiin_committee_date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSangiinCommitteeDate_lt')
    passed_sangiin_committee_date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSangiinCommitteeDate_lte')
    passed_sangiin_committee_date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSangiinCommitteeDate_gt')
    passed_sangiin_committee_date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSangiinCommitteeDate_gte')
    passed_sangiin_date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSangiinDate')
    passed_sangiin_date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSangiinDate_not')
    passed_sangiin_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedSangiinDate_in')
    passed_sangiin_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedSangiinDate_not_in')
    passed_sangiin_date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSangiinDate_lt')
    passed_sangiin_date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSangiinDate_lte')
    passed_sangiin_date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSangiinDate_gt')
    passed_sangiin_date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedSangiinDate_gte')
    proclaimed_date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='proclaimedDate')
    proclaimed_date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='proclaimedDate_not')
    proclaimed_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='proclaimedDate_in')
    proclaimed_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='proclaimedDate_not_in')
    proclaimed_date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='proclaimedDate_lt')
    proclaimed_date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='proclaimedDate_lte')
    proclaimed_date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='proclaimedDate_gt')
    proclaimed_date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='proclaimedDate_gte')
    urls = sgqlc.types.Field('_UrlFilter', graphql_name='urls')
    urls_not = sgqlc.types.Field('_UrlFilter', graphql_name='urls_not')
    urls_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='urls_in')
    urls_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='urls_not_in')
    urls_some = sgqlc.types.Field('_UrlFilter', graphql_name='urls_some')
    urls_none = sgqlc.types.Field('_UrlFilter', graphql_name='urls_none')
    urls_single = sgqlc.types.Field('_UrlFilter', graphql_name='urls_single')
    urls_every = sgqlc.types.Field('_UrlFilter', graphql_name='urls_every')
    timelines = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines')
    timelines_not = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_not')
    timelines_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimelineFilter')), graphql_name='timelines_in')
    timelines_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimelineFilter')), graphql_name='timelines_not_in')
    timelines_some = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_some')
    timelines_none = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_none')
    timelines_single = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_single')
    timelines_every = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_every')


class _BillInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _CommitteeFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'house', 'house_not', 'house_in', 'house_not_in', 'members', 'members_not', 'members_in', 'members_not_in', 'members_some', 'members_none', 'members_single', 'members_every', 'minutes', 'minutes_not', 'minutes_in', 'minutes_not_in', 'minutes_some', 'minutes_none', 'minutes_single', 'minutes_every')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_CommitteeFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_CommitteeFilter')), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(ID, graphql_name='id_contains')
    id_not_contains = sgqlc.types.Field(ID, graphql_name='id_not_contains')
    id_starts_with = sgqlc.types.Field(ID, graphql_name='id_starts_with')
    id_not_starts_with = sgqlc.types.Field(ID, graphql_name='id_not_starts_with')
    id_ends_with = sgqlc.types.Field(ID, graphql_name='id_ends_with')
    id_not_ends_with = sgqlc.types.Field(ID, graphql_name='id_not_ends_with')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    house = sgqlc.types.Field(House, graphql_name='house')
    house_not = sgqlc.types.Field(House, graphql_name='house_not')
    house_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(House)), graphql_name='house_in')
    house_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(House)), graphql_name='house_not_in')
    members = sgqlc.types.Field('_MemberFilter', graphql_name='members')
    members_not = sgqlc.types.Field('_MemberFilter', graphql_name='members_not')
    members_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MemberFilter')), graphql_name='members_in')
    members_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MemberFilter')), graphql_name='members_not_in')
    members_some = sgqlc.types.Field('_MemberFilter', graphql_name='members_some')
    members_none = sgqlc.types.Field('_MemberFilter', graphql_name='members_none')
    members_single = sgqlc.types.Field('_MemberFilter', graphql_name='members_single')
    members_every = sgqlc.types.Field('_MemberFilter', graphql_name='members_every')
    minutes = sgqlc.types.Field('_MinutesFilter', graphql_name='minutes')
    minutes_not = sgqlc.types.Field('_MinutesFilter', graphql_name='minutes_not')
    minutes_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='minutes_in')
    minutes_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='minutes_not_in')
    minutes_some = sgqlc.types.Field('_MinutesFilter', graphql_name='minutes_some')
    minutes_none = sgqlc.types.Field('_MinutesFilter', graphql_name='minutes_none')
    minutes_single = sgqlc.types.Field('_MinutesFilter', graphql_name='minutes_single')
    minutes_every = sgqlc.types.Field('_MinutesFilter', graphql_name='minutes_every')


class _CommitteeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _DietFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'number', 'number_not', 'number_in', 'number_not_in', 'number_lt', 'number_lte', 'number_gt', 'number_gte', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'start_date', 'start_date_not', 'start_date_in', 'start_date_not_in', 'start_date_lt', 'start_date_lte', 'start_date_gt', 'start_date_gte', 'end_date', 'end_date_not', 'end_date_in', 'end_date_not_in', 'end_date_lt', 'end_date_lte', 'end_date_gt', 'end_date_gte', 'received_bills', 'received_bills_not', 'received_bills_in', 'received_bills_not_in', 'received_bills_some', 'received_bills_none', 'received_bills_single', 'received_bills_every', 'minutes', 'minutes_not', 'minutes_in', 'minutes_not_in', 'minutes_some', 'minutes_none', 'minutes_single', 'minutes_every')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_DietFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_DietFilter')), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(ID, graphql_name='id_contains')
    id_not_contains = sgqlc.types.Field(ID, graphql_name='id_not_contains')
    id_starts_with = sgqlc.types.Field(ID, graphql_name='id_starts_with')
    id_not_starts_with = sgqlc.types.Field(ID, graphql_name='id_not_starts_with')
    id_ends_with = sgqlc.types.Field(ID, graphql_name='id_ends_with')
    id_not_ends_with = sgqlc.types.Field(ID, graphql_name='id_not_ends_with')
    number = sgqlc.types.Field(Int, graphql_name='number')
    number_not = sgqlc.types.Field(Int, graphql_name='number_not')
    number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='number_in')
    number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='number_not_in')
    number_lt = sgqlc.types.Field(Int, graphql_name='number_lt')
    number_lte = sgqlc.types.Field(Int, graphql_name='number_lte')
    number_gt = sgqlc.types.Field(Int, graphql_name='number_gt')
    number_gte = sgqlc.types.Field(Int, graphql_name='number_gte')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    start_date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='startDate')
    start_date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='startDate_not')
    start_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='startDate_in')
    start_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='startDate_not_in')
    start_date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='startDate_lt')
    start_date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='startDate_lte')
    start_date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='startDate_gt')
    start_date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='startDate_gte')
    end_date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='endDate')
    end_date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='endDate_not')
    end_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='endDate_in')
    end_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='endDate_not_in')
    end_date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='endDate_lt')
    end_date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='endDate_lte')
    end_date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='endDate_gt')
    end_date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='endDate_gte')
    received_bills = sgqlc.types.Field(_BillFilter, graphql_name='receivedBills')
    received_bills_not = sgqlc.types.Field(_BillFilter, graphql_name='receivedBills_not')
    received_bills_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='receivedBills_in')
    received_bills_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='receivedBills_not_in')
    received_bills_some = sgqlc.types.Field(_BillFilter, graphql_name='receivedBills_some')
    received_bills_none = sgqlc.types.Field(_BillFilter, graphql_name='receivedBills_none')
    received_bills_single = sgqlc.types.Field(_BillFilter, graphql_name='receivedBills_single')
    received_bills_every = sgqlc.types.Field(_BillFilter, graphql_name='receivedBills_every')
    minutes = sgqlc.types.Field('_MinutesFilter', graphql_name='minutes')
    minutes_not = sgqlc.types.Field('_MinutesFilter', graphql_name='minutes_not')
    minutes_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='minutes_in')
    minutes_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='minutes_not_in')
    minutes_some = sgqlc.types.Field('_MinutesFilter', graphql_name='minutes_some')
    minutes_none = sgqlc.types.Field('_MinutesFilter', graphql_name='minutes_none')
    minutes_single = sgqlc.types.Field('_MinutesFilter', graphql_name='minutes_single')
    minutes_every = sgqlc.types.Field('_MinutesFilter', graphql_name='minutes_every')


class _DietInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _ElectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'election_type', 'election_type_not', 'election_type_in', 'election_type_not_in', 'district', 'district_not', 'district_in', 'district_not_in', 'district_contains', 'district_not_contains', 'district_starts_with', 'district_not_starts_with', 'district_ends_with', 'district_not_ends_with', 'prefecture', 'prefecture_not', 'prefecture_in', 'prefecture_not_in', 'prefecture_contains', 'prefecture_not_contains', 'prefecture_starts_with', 'prefecture_not_starts_with', 'prefecture_ends_with', 'prefecture_not_ends_with', 'datetime', 'datetime_not', 'datetime_in', 'datetime_not_in', 'datetime_lt', 'datetime_lte', 'datetime_gt', 'datetime_gte', 'elected_members', 'elected_members_not', 'elected_members_in', 'elected_members_not_in', 'elected_members_some', 'elected_members_none', 'elected_members_single', 'elected_members_every')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_ElectionFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_ElectionFilter')), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(ID, graphql_name='id_contains')
    id_not_contains = sgqlc.types.Field(ID, graphql_name='id_not_contains')
    id_starts_with = sgqlc.types.Field(ID, graphql_name='id_starts_with')
    id_not_starts_with = sgqlc.types.Field(ID, graphql_name='id_not_starts_with')
    id_ends_with = sgqlc.types.Field(ID, graphql_name='id_ends_with')
    id_not_ends_with = sgqlc.types.Field(ID, graphql_name='id_not_ends_with')
    election_type = sgqlc.types.Field(ElectionType, graphql_name='electionType')
    election_type_not = sgqlc.types.Field(ElectionType, graphql_name='electionType_not')
    election_type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ElectionType)), graphql_name='electionType_in')
    election_type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ElectionType)), graphql_name='electionType_not_in')
    district = sgqlc.types.Field(String, graphql_name='district')
    district_not = sgqlc.types.Field(String, graphql_name='district_not')
    district_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='district_in')
    district_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='district_not_in')
    district_contains = sgqlc.types.Field(String, graphql_name='district_contains')
    district_not_contains = sgqlc.types.Field(String, graphql_name='district_not_contains')
    district_starts_with = sgqlc.types.Field(String, graphql_name='district_starts_with')
    district_not_starts_with = sgqlc.types.Field(String, graphql_name='district_not_starts_with')
    district_ends_with = sgqlc.types.Field(String, graphql_name='district_ends_with')
    district_not_ends_with = sgqlc.types.Field(String, graphql_name='district_not_ends_with')
    prefecture = sgqlc.types.Field(String, graphql_name='prefecture')
    prefecture_not = sgqlc.types.Field(String, graphql_name='prefecture_not')
    prefecture_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='prefecture_in')
    prefecture_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='prefecture_not_in')
    prefecture_contains = sgqlc.types.Field(String, graphql_name='prefecture_contains')
    prefecture_not_contains = sgqlc.types.Field(String, graphql_name='prefecture_not_contains')
    prefecture_starts_with = sgqlc.types.Field(String, graphql_name='prefecture_starts_with')
    prefecture_not_starts_with = sgqlc.types.Field(String, graphql_name='prefecture_not_starts_with')
    prefecture_ends_with = sgqlc.types.Field(String, graphql_name='prefecture_ends_with')
    prefecture_not_ends_with = sgqlc.types.Field(String, graphql_name='prefecture_not_ends_with')
    datetime = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='datetime')
    datetime_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='datetime_not')
    datetime_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='datetime_in')
    datetime_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='datetime_not_in')
    datetime_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='datetime_lt')
    datetime_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='datetime_lte')
    datetime_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='datetime_gt')
    datetime_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='datetime_gte')
    elected_members = sgqlc.types.Field('_MemberFilter', graphql_name='electedMembers')
    elected_members_not = sgqlc.types.Field('_MemberFilter', graphql_name='electedMembers_not')
    elected_members_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MemberFilter')), graphql_name='electedMembers_in')
    elected_members_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MemberFilter')), graphql_name='electedMembers_not_in')
    elected_members_some = sgqlc.types.Field('_MemberFilter', graphql_name='electedMembers_some')
    elected_members_none = sgqlc.types.Field('_MemberFilter', graphql_name='electedMembers_none')
    elected_members_single = sgqlc.types.Field('_MemberFilter', graphql_name='electedMembers_single')
    elected_members_every = sgqlc.types.Field('_MemberFilter', graphql_name='electedMembers_every')


class _ElectionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _LawFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'law_title', 'law_title_not', 'law_title_in', 'law_title_not_in', 'law_title_contains', 'law_title_not_contains', 'law_title_starts_with', 'law_title_not_starts_with', 'law_title_ends_with', 'law_title_not_ends_with', 'law_number', 'law_number_not', 'law_number_in', 'law_number_not_in', 'law_number_contains', 'law_number_not_contains', 'law_number_starts_with', 'law_number_not_starts_with', 'law_number_ends_with', 'law_number_not_ends_with', 'be_discussed_by_minutes', 'be_discussed_by_minutes_not', 'be_discussed_by_minutes_in', 'be_discussed_by_minutes_not_in', 'be_discussed_by_minutes_some', 'be_discussed_by_minutes_none', 'be_discussed_by_minutes_single', 'be_discussed_by_minutes_every', 'referred_laws', 'referred_laws_not', 'referred_laws_in', 'referred_laws_not_in', 'referred_laws_some', 'referred_laws_none', 'referred_laws_single', 'referred_laws_every', 'be_referred_by_laws', 'be_referred_by_laws_not', 'be_referred_by_laws_in', 'be_referred_by_laws_not_in', 'be_referred_by_laws_some', 'be_referred_by_laws_none', 'be_referred_by_laws_single', 'be_referred_by_laws_every', 'be_amended_by_bills', 'be_amended_by_bills_not', 'be_amended_by_bills_in', 'be_amended_by_bills_not_in', 'be_amended_by_bills_some', 'be_amended_by_bills_none', 'be_amended_by_bills_single', 'be_amended_by_bills_every', 'urls', 'urls_not', 'urls_in', 'urls_not_in', 'urls_some', 'urls_none', 'urls_single', 'urls_every', 'timelines', 'timelines_not', 'timelines_in', 'timelines_not_in', 'timelines_some', 'timelines_none', 'timelines_single', 'timelines_every')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_LawFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_LawFilter')), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(ID, graphql_name='id_contains')
    id_not_contains = sgqlc.types.Field(ID, graphql_name='id_not_contains')
    id_starts_with = sgqlc.types.Field(ID, graphql_name='id_starts_with')
    id_not_starts_with = sgqlc.types.Field(ID, graphql_name='id_not_starts_with')
    id_ends_with = sgqlc.types.Field(ID, graphql_name='id_ends_with')
    id_not_ends_with = sgqlc.types.Field(ID, graphql_name='id_not_ends_with')
    law_title = sgqlc.types.Field(String, graphql_name='lawTitle')
    law_title_not = sgqlc.types.Field(String, graphql_name='lawTitle_not')
    law_title_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lawTitle_in')
    law_title_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lawTitle_not_in')
    law_title_contains = sgqlc.types.Field(String, graphql_name='lawTitle_contains')
    law_title_not_contains = sgqlc.types.Field(String, graphql_name='lawTitle_not_contains')
    law_title_starts_with = sgqlc.types.Field(String, graphql_name='lawTitle_starts_with')
    law_title_not_starts_with = sgqlc.types.Field(String, graphql_name='lawTitle_not_starts_with')
    law_title_ends_with = sgqlc.types.Field(String, graphql_name='lawTitle_ends_with')
    law_title_not_ends_with = sgqlc.types.Field(String, graphql_name='lawTitle_not_ends_with')
    law_number = sgqlc.types.Field(String, graphql_name='lawNumber')
    law_number_not = sgqlc.types.Field(String, graphql_name='lawNumber_not')
    law_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lawNumber_in')
    law_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lawNumber_not_in')
    law_number_contains = sgqlc.types.Field(String, graphql_name='lawNumber_contains')
    law_number_not_contains = sgqlc.types.Field(String, graphql_name='lawNumber_not_contains')
    law_number_starts_with = sgqlc.types.Field(String, graphql_name='lawNumber_starts_with')
    law_number_not_starts_with = sgqlc.types.Field(String, graphql_name='lawNumber_not_starts_with')
    law_number_ends_with = sgqlc.types.Field(String, graphql_name='lawNumber_ends_with')
    law_number_not_ends_with = sgqlc.types.Field(String, graphql_name='lawNumber_not_ends_with')
    be_discussed_by_minutes = sgqlc.types.Field('_MinutesFilter', graphql_name='beDiscussedByMinutes')
    be_discussed_by_minutes_not = sgqlc.types.Field('_MinutesFilter', graphql_name='beDiscussedByMinutes_not')
    be_discussed_by_minutes_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='beDiscussedByMinutes_in')
    be_discussed_by_minutes_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='beDiscussedByMinutes_not_in')
    be_discussed_by_minutes_some = sgqlc.types.Field('_MinutesFilter', graphql_name='beDiscussedByMinutes_some')
    be_discussed_by_minutes_none = sgqlc.types.Field('_MinutesFilter', graphql_name='beDiscussedByMinutes_none')
    be_discussed_by_minutes_single = sgqlc.types.Field('_MinutesFilter', graphql_name='beDiscussedByMinutes_single')
    be_discussed_by_minutes_every = sgqlc.types.Field('_MinutesFilter', graphql_name='beDiscussedByMinutes_every')
    referred_laws = sgqlc.types.Field('_LawFilter', graphql_name='referredLaws')
    referred_laws_not = sgqlc.types.Field('_LawFilter', graphql_name='referredLaws_not')
    referred_laws_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_LawFilter')), graphql_name='referredLaws_in')
    referred_laws_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_LawFilter')), graphql_name='referredLaws_not_in')
    referred_laws_some = sgqlc.types.Field('_LawFilter', graphql_name='referredLaws_some')
    referred_laws_none = sgqlc.types.Field('_LawFilter', graphql_name='referredLaws_none')
    referred_laws_single = sgqlc.types.Field('_LawFilter', graphql_name='referredLaws_single')
    referred_laws_every = sgqlc.types.Field('_LawFilter', graphql_name='referredLaws_every')
    be_referred_by_laws = sgqlc.types.Field('_LawFilter', graphql_name='beReferredByLaws')
    be_referred_by_laws_not = sgqlc.types.Field('_LawFilter', graphql_name='beReferredByLaws_not')
    be_referred_by_laws_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_LawFilter')), graphql_name='beReferredByLaws_in')
    be_referred_by_laws_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_LawFilter')), graphql_name='beReferredByLaws_not_in')
    be_referred_by_laws_some = sgqlc.types.Field('_LawFilter', graphql_name='beReferredByLaws_some')
    be_referred_by_laws_none = sgqlc.types.Field('_LawFilter', graphql_name='beReferredByLaws_none')
    be_referred_by_laws_single = sgqlc.types.Field('_LawFilter', graphql_name='beReferredByLaws_single')
    be_referred_by_laws_every = sgqlc.types.Field('_LawFilter', graphql_name='beReferredByLaws_every')
    be_amended_by_bills = sgqlc.types.Field(_BillFilter, graphql_name='beAmendedByBills')
    be_amended_by_bills_not = sgqlc.types.Field(_BillFilter, graphql_name='beAmendedByBills_not')
    be_amended_by_bills_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='beAmendedByBills_in')
    be_amended_by_bills_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='beAmendedByBills_not_in')
    be_amended_by_bills_some = sgqlc.types.Field(_BillFilter, graphql_name='beAmendedByBills_some')
    be_amended_by_bills_none = sgqlc.types.Field(_BillFilter, graphql_name='beAmendedByBills_none')
    be_amended_by_bills_single = sgqlc.types.Field(_BillFilter, graphql_name='beAmendedByBills_single')
    be_amended_by_bills_every = sgqlc.types.Field(_BillFilter, graphql_name='beAmendedByBills_every')
    urls = sgqlc.types.Field('_UrlFilter', graphql_name='urls')
    urls_not = sgqlc.types.Field('_UrlFilter', graphql_name='urls_not')
    urls_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='urls_in')
    urls_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='urls_not_in')
    urls_some = sgqlc.types.Field('_UrlFilter', graphql_name='urls_some')
    urls_none = sgqlc.types.Field('_UrlFilter', graphql_name='urls_none')
    urls_single = sgqlc.types.Field('_UrlFilter', graphql_name='urls_single')
    urls_every = sgqlc.types.Field('_UrlFilter', graphql_name='urls_every')
    timelines = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines')
    timelines_not = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_not')
    timelines_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimelineFilter')), graphql_name='timelines_in')
    timelines_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimelineFilter')), graphql_name='timelines_not_in')
    timelines_some = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_some')
    timelines_none = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_none')
    timelines_single = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_single')
    timelines_every = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_every')


class _LawInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _MemberFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'name_hira', 'name_hira_not', 'name_hira_in', 'name_hira_not_in', 'name_hira_contains', 'name_hira_not_contains', 'name_hira_starts_with', 'name_hira_not_starts_with', 'name_hira_ends_with', 'name_hira_not_ends_with', 'first_name', 'first_name_not', 'first_name_in', 'first_name_not_in', 'first_name_contains', 'first_name_not_contains', 'first_name_starts_with', 'first_name_not_starts_with', 'first_name_ends_with', 'first_name_not_ends_with', 'first_name_hira', 'first_name_hira_not', 'first_name_hira_in', 'first_name_hira_not_in', 'first_name_hira_contains', 'first_name_hira_not_contains', 'first_name_hira_starts_with', 'first_name_hira_not_starts_with', 'first_name_hira_ends_with', 'first_name_hira_not_ends_with', 'last_name', 'last_name_not', 'last_name_in', 'last_name_not_in', 'last_name_contains', 'last_name_not_contains', 'last_name_starts_with', 'last_name_not_starts_with', 'last_name_ends_with', 'last_name_not_ends_with', 'last_name_hira', 'last_name_hira_not', 'last_name_hira_in', 'last_name_hira_not_in', 'last_name_hira_contains', 'last_name_hira_not_contains', 'last_name_hira_starts_with', 'last_name_hira_not_starts_with', 'last_name_hira_ends_with', 'last_name_hira_not_ends_with', 'house', 'house_not', 'house_in', 'house_not_in', 'be_elected_by_elections', 'be_elected_by_elections_not', 'be_elected_by_elections_in', 'be_elected_by_elections_not_in', 'be_elected_by_elections_some', 'be_elected_by_elections_none', 'be_elected_by_elections_single', 'be_elected_by_elections_every', 'submitted_bills', 'submitted_bills_not', 'submitted_bills_in', 'submitted_bills_not_in', 'submitted_bills_some', 'submitted_bills_none', 'submitted_bills_single', 'submitted_bills_every', 'attended_diets', 'attended_diets_not', 'attended_diets_in', 'attended_diets_not_in', 'attended_diets_some', 'attended_diets_none', 'attended_diets_single', 'attended_diets_every', 'attended_minutes', 'attended_minutes_not', 'attended_minutes_in', 'attended_minutes_not_in', 'attended_minutes_some', 'attended_minutes_none', 'attended_minutes_single', 'attended_minutes_every', 'urls', 'urls_not', 'urls_in', 'urls_not_in', 'urls_some', 'urls_none', 'urls_single', 'urls_every', 'timelines', 'timelines_not', 'timelines_in', 'timelines_not_in', 'timelines_some', 'timelines_none', 'timelines_single', 'timelines_every')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MemberFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MemberFilter')), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(ID, graphql_name='id_contains')
    id_not_contains = sgqlc.types.Field(ID, graphql_name='id_not_contains')
    id_starts_with = sgqlc.types.Field(ID, graphql_name='id_starts_with')
    id_not_starts_with = sgqlc.types.Field(ID, graphql_name='id_not_starts_with')
    id_ends_with = sgqlc.types.Field(ID, graphql_name='id_ends_with')
    id_not_ends_with = sgqlc.types.Field(ID, graphql_name='id_not_ends_with')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_hira = sgqlc.types.Field(String, graphql_name='nameHira')
    name_hira_not = sgqlc.types.Field(String, graphql_name='nameHira_not')
    name_hira_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='nameHira_in')
    name_hira_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='nameHira_not_in')
    name_hira_contains = sgqlc.types.Field(String, graphql_name='nameHira_contains')
    name_hira_not_contains = sgqlc.types.Field(String, graphql_name='nameHira_not_contains')
    name_hira_starts_with = sgqlc.types.Field(String, graphql_name='nameHira_starts_with')
    name_hira_not_starts_with = sgqlc.types.Field(String, graphql_name='nameHira_not_starts_with')
    name_hira_ends_with = sgqlc.types.Field(String, graphql_name='nameHira_ends_with')
    name_hira_not_ends_with = sgqlc.types.Field(String, graphql_name='nameHira_not_ends_with')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    first_name_not = sgqlc.types.Field(String, graphql_name='firstName_not')
    first_name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='firstName_in')
    first_name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='firstName_not_in')
    first_name_contains = sgqlc.types.Field(String, graphql_name='firstName_contains')
    first_name_not_contains = sgqlc.types.Field(String, graphql_name='firstName_not_contains')
    first_name_starts_with = sgqlc.types.Field(String, graphql_name='firstName_starts_with')
    first_name_not_starts_with = sgqlc.types.Field(String, graphql_name='firstName_not_starts_with')
    first_name_ends_with = sgqlc.types.Field(String, graphql_name='firstName_ends_with')
    first_name_not_ends_with = sgqlc.types.Field(String, graphql_name='firstName_not_ends_with')
    first_name_hira = sgqlc.types.Field(String, graphql_name='firstNameHira')
    first_name_hira_not = sgqlc.types.Field(String, graphql_name='firstNameHira_not')
    first_name_hira_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='firstNameHira_in')
    first_name_hira_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='firstNameHira_not_in')
    first_name_hira_contains = sgqlc.types.Field(String, graphql_name='firstNameHira_contains')
    first_name_hira_not_contains = sgqlc.types.Field(String, graphql_name='firstNameHira_not_contains')
    first_name_hira_starts_with = sgqlc.types.Field(String, graphql_name='firstNameHira_starts_with')
    first_name_hira_not_starts_with = sgqlc.types.Field(String, graphql_name='firstNameHira_not_starts_with')
    first_name_hira_ends_with = sgqlc.types.Field(String, graphql_name='firstNameHira_ends_with')
    first_name_hira_not_ends_with = sgqlc.types.Field(String, graphql_name='firstNameHira_not_ends_with')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    last_name_not = sgqlc.types.Field(String, graphql_name='lastName_not')
    last_name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lastName_in')
    last_name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lastName_not_in')
    last_name_contains = sgqlc.types.Field(String, graphql_name='lastName_contains')
    last_name_not_contains = sgqlc.types.Field(String, graphql_name='lastName_not_contains')
    last_name_starts_with = sgqlc.types.Field(String, graphql_name='lastName_starts_with')
    last_name_not_starts_with = sgqlc.types.Field(String, graphql_name='lastName_not_starts_with')
    last_name_ends_with = sgqlc.types.Field(String, graphql_name='lastName_ends_with')
    last_name_not_ends_with = sgqlc.types.Field(String, graphql_name='lastName_not_ends_with')
    last_name_hira = sgqlc.types.Field(String, graphql_name='lastNameHira')
    last_name_hira_not = sgqlc.types.Field(String, graphql_name='lastNameHira_not')
    last_name_hira_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lastNameHira_in')
    last_name_hira_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lastNameHira_not_in')
    last_name_hira_contains = sgqlc.types.Field(String, graphql_name='lastNameHira_contains')
    last_name_hira_not_contains = sgqlc.types.Field(String, graphql_name='lastNameHira_not_contains')
    last_name_hira_starts_with = sgqlc.types.Field(String, graphql_name='lastNameHira_starts_with')
    last_name_hira_not_starts_with = sgqlc.types.Field(String, graphql_name='lastNameHira_not_starts_with')
    last_name_hira_ends_with = sgqlc.types.Field(String, graphql_name='lastNameHira_ends_with')
    last_name_hira_not_ends_with = sgqlc.types.Field(String, graphql_name='lastNameHira_not_ends_with')
    house = sgqlc.types.Field(House, graphql_name='house')
    house_not = sgqlc.types.Field(House, graphql_name='house_not')
    house_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(House)), graphql_name='house_in')
    house_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(House)), graphql_name='house_not_in')
    be_elected_by_elections = sgqlc.types.Field(_ElectionFilter, graphql_name='beElectedByElections')
    be_elected_by_elections_not = sgqlc.types.Field(_ElectionFilter, graphql_name='beElectedByElections_not')
    be_elected_by_elections_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_ElectionFilter)), graphql_name='beElectedByElections_in')
    be_elected_by_elections_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_ElectionFilter)), graphql_name='beElectedByElections_not_in')
    be_elected_by_elections_some = sgqlc.types.Field(_ElectionFilter, graphql_name='beElectedByElections_some')
    be_elected_by_elections_none = sgqlc.types.Field(_ElectionFilter, graphql_name='beElectedByElections_none')
    be_elected_by_elections_single = sgqlc.types.Field(_ElectionFilter, graphql_name='beElectedByElections_single')
    be_elected_by_elections_every = sgqlc.types.Field(_ElectionFilter, graphql_name='beElectedByElections_every')
    submitted_bills = sgqlc.types.Field(_BillFilter, graphql_name='submittedBills')
    submitted_bills_not = sgqlc.types.Field(_BillFilter, graphql_name='submittedBills_not')
    submitted_bills_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='submittedBills_in')
    submitted_bills_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='submittedBills_not_in')
    submitted_bills_some = sgqlc.types.Field(_BillFilter, graphql_name='submittedBills_some')
    submitted_bills_none = sgqlc.types.Field(_BillFilter, graphql_name='submittedBills_none')
    submitted_bills_single = sgqlc.types.Field(_BillFilter, graphql_name='submittedBills_single')
    submitted_bills_every = sgqlc.types.Field(_BillFilter, graphql_name='submittedBills_every')
    attended_diets = sgqlc.types.Field(_DietFilter, graphql_name='attendedDiets')
    attended_diets_not = sgqlc.types.Field(_DietFilter, graphql_name='attendedDiets_not')
    attended_diets_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_DietFilter)), graphql_name='attendedDiets_in')
    attended_diets_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_DietFilter)), graphql_name='attendedDiets_not_in')
    attended_diets_some = sgqlc.types.Field(_DietFilter, graphql_name='attendedDiets_some')
    attended_diets_none = sgqlc.types.Field(_DietFilter, graphql_name='attendedDiets_none')
    attended_diets_single = sgqlc.types.Field(_DietFilter, graphql_name='attendedDiets_single')
    attended_diets_every = sgqlc.types.Field(_DietFilter, graphql_name='attendedDiets_every')
    attended_minutes = sgqlc.types.Field('_MinutesFilter', graphql_name='attendedMinutes')
    attended_minutes_not = sgqlc.types.Field('_MinutesFilter', graphql_name='attendedMinutes_not')
    attended_minutes_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='attendedMinutes_in')
    attended_minutes_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='attendedMinutes_not_in')
    attended_minutes_some = sgqlc.types.Field('_MinutesFilter', graphql_name='attendedMinutes_some')
    attended_minutes_none = sgqlc.types.Field('_MinutesFilter', graphql_name='attendedMinutes_none')
    attended_minutes_single = sgqlc.types.Field('_MinutesFilter', graphql_name='attendedMinutes_single')
    attended_minutes_every = sgqlc.types.Field('_MinutesFilter', graphql_name='attendedMinutes_every')
    urls = sgqlc.types.Field('_UrlFilter', graphql_name='urls')
    urls_not = sgqlc.types.Field('_UrlFilter', graphql_name='urls_not')
    urls_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='urls_in')
    urls_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='urls_not_in')
    urls_some = sgqlc.types.Field('_UrlFilter', graphql_name='urls_some')
    urls_none = sgqlc.types.Field('_UrlFilter', graphql_name='urls_none')
    urls_single = sgqlc.types.Field('_UrlFilter', graphql_name='urls_single')
    urls_every = sgqlc.types.Field('_UrlFilter', graphql_name='urls_every')
    timelines = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines')
    timelines_not = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_not')
    timelines_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimelineFilter')), graphql_name='timelines_in')
    timelines_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimelineFilter')), graphql_name='timelines_not_in')
    timelines_some = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_some')
    timelines_none = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_none')
    timelines_single = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_single')
    timelines_every = sgqlc.types.Field('_TimelineFilter', graphql_name='timelines_every')


class _MemberInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _MinutesFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'minutes_number', 'minutes_number_not', 'minutes_number_in', 'minutes_number_not_in', 'minutes_number_contains', 'minutes_number_not_contains', 'minutes_number_starts_with', 'minutes_number_not_starts_with', 'minutes_number_ends_with', 'minutes_number_not_ends_with', 'start_date_time', 'start_date_time_not', 'start_date_time_in', 'start_date_time_not_in', 'start_date_time_lt', 'start_date_time_lte', 'start_date_time_gt', 'start_date_time_gte', 'end_date_time', 'end_date_time_not', 'end_date_time_in', 'end_date_time_not_in', 'end_date_time_lt', 'end_date_time_lte', 'end_date_time_gt', 'end_date_time_gte', 'belonged_to_diet', 'belonged_to_diet_not', 'belonged_to_diet_in', 'belonged_to_diet_not_in', 'belonged_to_committee', 'belonged_to_committee_not', 'belonged_to_committee_in', 'belonged_to_committee_not_in', 'be_attended_by_members', 'be_attended_by_members_not', 'be_attended_by_members_in', 'be_attended_by_members_not_in', 'be_attended_by_members_some', 'be_attended_by_members_none', 'be_attended_by_members_single', 'be_attended_by_members_every', 'discussed_bills', 'discussed_bills_not', 'discussed_bills_in', 'discussed_bills_not_in', 'discussed_bills_some', 'discussed_bills_none', 'discussed_bills_single', 'discussed_bills_every', 'discussed_laws', 'discussed_laws_not', 'discussed_laws_in', 'discussed_laws_not_in', 'discussed_laws_some', 'discussed_laws_none', 'discussed_laws_single', 'discussed_laws_every')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(ID, graphql_name='id_contains')
    id_not_contains = sgqlc.types.Field(ID, graphql_name='id_not_contains')
    id_starts_with = sgqlc.types.Field(ID, graphql_name='id_starts_with')
    id_not_starts_with = sgqlc.types.Field(ID, graphql_name='id_not_starts_with')
    id_ends_with = sgqlc.types.Field(ID, graphql_name='id_ends_with')
    id_not_ends_with = sgqlc.types.Field(ID, graphql_name='id_not_ends_with')
    minutes_number = sgqlc.types.Field(String, graphql_name='minutesNumber')
    minutes_number_not = sgqlc.types.Field(String, graphql_name='minutesNumber_not')
    minutes_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='minutesNumber_in')
    minutes_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='minutesNumber_not_in')
    minutes_number_contains = sgqlc.types.Field(String, graphql_name='minutesNumber_contains')
    minutes_number_not_contains = sgqlc.types.Field(String, graphql_name='minutesNumber_not_contains')
    minutes_number_starts_with = sgqlc.types.Field(String, graphql_name='minutesNumber_starts_with')
    minutes_number_not_starts_with = sgqlc.types.Field(String, graphql_name='minutesNumber_not_starts_with')
    minutes_number_ends_with = sgqlc.types.Field(String, graphql_name='minutesNumber_ends_with')
    minutes_number_not_ends_with = sgqlc.types.Field(String, graphql_name='minutesNumber_not_ends_with')
    start_date_time = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='startDateTime')
    start_date_time_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='startDateTime_not')
    start_date_time_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='startDateTime_in')
    start_date_time_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='startDateTime_not_in')
    start_date_time_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='startDateTime_lt')
    start_date_time_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='startDateTime_lte')
    start_date_time_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='startDateTime_gt')
    start_date_time_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='startDateTime_gte')
    end_date_time = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='endDateTime')
    end_date_time_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='endDateTime_not')
    end_date_time_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='endDateTime_in')
    end_date_time_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='endDateTime_not_in')
    end_date_time_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='endDateTime_lt')
    end_date_time_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='endDateTime_lte')
    end_date_time_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='endDateTime_gt')
    end_date_time_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='endDateTime_gte')
    belonged_to_diet = sgqlc.types.Field(_DietFilter, graphql_name='belongedToDiet')
    belonged_to_diet_not = sgqlc.types.Field(_DietFilter, graphql_name='belongedToDiet_not')
    belonged_to_diet_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_DietFilter)), graphql_name='belongedToDiet_in')
    belonged_to_diet_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_DietFilter)), graphql_name='belongedToDiet_not_in')
    belonged_to_committee = sgqlc.types.Field(_CommitteeFilter, graphql_name='belongedToCommittee')
    belonged_to_committee_not = sgqlc.types.Field(_CommitteeFilter, graphql_name='belongedToCommittee_not')
    belonged_to_committee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_CommitteeFilter)), graphql_name='belongedToCommittee_in')
    belonged_to_committee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_CommitteeFilter)), graphql_name='belongedToCommittee_not_in')
    be_attended_by_members = sgqlc.types.Field(_MemberFilter, graphql_name='beAttendedByMembers')
    be_attended_by_members_not = sgqlc.types.Field(_MemberFilter, graphql_name='beAttendedByMembers_not')
    be_attended_by_members_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MemberFilter)), graphql_name='beAttendedByMembers_in')
    be_attended_by_members_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MemberFilter)), graphql_name='beAttendedByMembers_not_in')
    be_attended_by_members_some = sgqlc.types.Field(_MemberFilter, graphql_name='beAttendedByMembers_some')
    be_attended_by_members_none = sgqlc.types.Field(_MemberFilter, graphql_name='beAttendedByMembers_none')
    be_attended_by_members_single = sgqlc.types.Field(_MemberFilter, graphql_name='beAttendedByMembers_single')
    be_attended_by_members_every = sgqlc.types.Field(_MemberFilter, graphql_name='beAttendedByMembers_every')
    discussed_bills = sgqlc.types.Field(_BillFilter, graphql_name='discussedBills')
    discussed_bills_not = sgqlc.types.Field(_BillFilter, graphql_name='discussedBills_not')
    discussed_bills_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='discussedBills_in')
    discussed_bills_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='discussedBills_not_in')
    discussed_bills_some = sgqlc.types.Field(_BillFilter, graphql_name='discussedBills_some')
    discussed_bills_none = sgqlc.types.Field(_BillFilter, graphql_name='discussedBills_none')
    discussed_bills_single = sgqlc.types.Field(_BillFilter, graphql_name='discussedBills_single')
    discussed_bills_every = sgqlc.types.Field(_BillFilter, graphql_name='discussedBills_every')
    discussed_laws = sgqlc.types.Field(_LawFilter, graphql_name='discussedLaws')
    discussed_laws_not = sgqlc.types.Field(_LawFilter, graphql_name='discussedLaws_not')
    discussed_laws_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_LawFilter)), graphql_name='discussedLaws_in')
    discussed_laws_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_LawFilter)), graphql_name='discussedLaws_not_in')
    discussed_laws_some = sgqlc.types.Field(_LawFilter, graphql_name='discussedLaws_some')
    discussed_laws_none = sgqlc.types.Field(_LawFilter, graphql_name='discussedLaws_none')
    discussed_laws_single = sgqlc.types.Field(_LawFilter, graphql_name='discussedLaws_single')
    discussed_laws_every = sgqlc.types.Field(_LawFilter, graphql_name='discussedLaws_every')


class _MinutesInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _Neo4jDateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('year', 'month', 'day', 'formatted')
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jDateTimeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('year', 'month', 'day', 'hour', 'minute', 'second', 'millisecond', 'microsecond', 'nanosecond', 'timezone', 'formatted')
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jLocalDateTimeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('year', 'month', 'day', 'hour', 'minute', 'second', 'millisecond', 'microsecond', 'nanosecond', 'formatted')
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jLocalTimeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('hour', 'minute', 'second', 'millisecond', 'microsecond', 'nanosecond', 'formatted')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jPointDistanceFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('point', 'distance')
    point = sgqlc.types.Field(sgqlc.types.non_null('_Neo4jPointInput'), graphql_name='point')
    distance = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='distance')


class _Neo4jPointInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('x', 'y', 'z', 'longitude', 'latitude', 'height', 'crs', 'srid')
    x = sgqlc.types.Field(Float, graphql_name='x')
    y = sgqlc.types.Field(Float, graphql_name='y')
    z = sgqlc.types.Field(Float, graphql_name='z')
    longitude = sgqlc.types.Field(Float, graphql_name='longitude')
    latitude = sgqlc.types.Field(Float, graphql_name='latitude')
    height = sgqlc.types.Field(Float, graphql_name='height')
    crs = sgqlc.types.Field(String, graphql_name='crs')
    srid = sgqlc.types.Field(Int, graphql_name='srid')


class _Neo4jTimeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('hour', 'minute', 'second', 'millisecond', 'microsecond', 'nanosecond', 'timezone', 'formatted')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _TimelineFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'content', 'content_not', 'content_in', 'content_not_in', 'content_contains', 'content_not_contains', 'content_starts_with', 'content_not_starts_with', 'content_ends_with', 'content_not_ends_with', 'datetime', 'datetime_not', 'datetime_in', 'datetime_not_in', 'datetime_lt', 'datetime_lte', 'datetime_gt', 'datetime_gte', 'referred_bills', 'referred_bills_not', 'referred_bills_in', 'referred_bills_not_in', 'referred_bills_some', 'referred_bills_none', 'referred_bills_single', 'referred_bills_every', 'referred_laws', 'referred_laws_not', 'referred_laws_in', 'referred_laws_not_in', 'referred_laws_some', 'referred_laws_none', 'referred_laws_single', 'referred_laws_every', 'referred_members', 'referred_members_not', 'referred_members_in', 'referred_members_not_in', 'referred_members_some', 'referred_members_none', 'referred_members_single', 'referred_members_every')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimelineFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimelineFilter')), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(ID, graphql_name='id_contains')
    id_not_contains = sgqlc.types.Field(ID, graphql_name='id_not_contains')
    id_starts_with = sgqlc.types.Field(ID, graphql_name='id_starts_with')
    id_not_starts_with = sgqlc.types.Field(ID, graphql_name='id_not_starts_with')
    id_ends_with = sgqlc.types.Field(ID, graphql_name='id_ends_with')
    id_not_ends_with = sgqlc.types.Field(ID, graphql_name='id_not_ends_with')
    content = sgqlc.types.Field(String, graphql_name='content')
    content_not = sgqlc.types.Field(String, graphql_name='content_not')
    content_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='content_in')
    content_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='content_not_in')
    content_contains = sgqlc.types.Field(String, graphql_name='content_contains')
    content_not_contains = sgqlc.types.Field(String, graphql_name='content_not_contains')
    content_starts_with = sgqlc.types.Field(String, graphql_name='content_starts_with')
    content_not_starts_with = sgqlc.types.Field(String, graphql_name='content_not_starts_with')
    content_ends_with = sgqlc.types.Field(String, graphql_name='content_ends_with')
    content_not_ends_with = sgqlc.types.Field(String, graphql_name='content_not_ends_with')
    datetime = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='datetime')
    datetime_not = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='datetime_not')
    datetime_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='datetime_in')
    datetime_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='datetime_not_in')
    datetime_lt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='datetime_lt')
    datetime_lte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='datetime_lte')
    datetime_gt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='datetime_gt')
    datetime_gte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='datetime_gte')
    referred_bills = sgqlc.types.Field(_BillFilter, graphql_name='referredBills')
    referred_bills_not = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_not')
    referred_bills_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='referredBills_in')
    referred_bills_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='referredBills_not_in')
    referred_bills_some = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_some')
    referred_bills_none = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_none')
    referred_bills_single = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_single')
    referred_bills_every = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_every')
    referred_laws = sgqlc.types.Field(_LawFilter, graphql_name='referredLaws')
    referred_laws_not = sgqlc.types.Field(_LawFilter, graphql_name='referredLaws_not')
    referred_laws_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_LawFilter)), graphql_name='referredLaws_in')
    referred_laws_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_LawFilter)), graphql_name='referredLaws_not_in')
    referred_laws_some = sgqlc.types.Field(_LawFilter, graphql_name='referredLaws_some')
    referred_laws_none = sgqlc.types.Field(_LawFilter, graphql_name='referredLaws_none')
    referred_laws_single = sgqlc.types.Field(_LawFilter, graphql_name='referredLaws_single')
    referred_laws_every = sgqlc.types.Field(_LawFilter, graphql_name='referredLaws_every')
    referred_members = sgqlc.types.Field(_MemberFilter, graphql_name='referredMembers')
    referred_members_not = sgqlc.types.Field(_MemberFilter, graphql_name='referredMembers_not')
    referred_members_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MemberFilter)), graphql_name='referredMembers_in')
    referred_members_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MemberFilter)), graphql_name='referredMembers_not_in')
    referred_members_some = sgqlc.types.Field(_MemberFilter, graphql_name='referredMembers_some')
    referred_members_none = sgqlc.types.Field(_MemberFilter, graphql_name='referredMembers_none')
    referred_members_single = sgqlc.types.Field(_MemberFilter, graphql_name='referredMembers_single')
    referred_members_every = sgqlc.types.Field(_MemberFilter, graphql_name='referredMembers_every')


class _TimelineInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _UrlFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'url', 'url_not', 'url_in', 'url_not_in', 'url_contains', 'url_not_contains', 'url_starts_with', 'url_not_starts_with', 'url_ends_with', 'url_not_ends_with', 'domain', 'domain_not', 'domain_in', 'domain_not_in', 'domain_contains', 'domain_not_contains', 'domain_starts_with', 'domain_not_starts_with', 'domain_ends_with', 'domain_not_ends_with', 'title', 'title_not', 'title_in', 'title_not_in', 'title_contains', 'title_not_contains', 'title_starts_with', 'title_not_starts_with', 'title_ends_with', 'title_not_ends_with', 'description', 'description_not', 'description_in', 'description_not_in', 'description_contains', 'description_not_contains', 'description_starts_with', 'description_not_starts_with', 'description_ends_with', 'description_not_ends_with', 'referred_bills', 'referred_bills_not', 'referred_bills_in', 'referred_bills_not_in', 'referred_bills_some', 'referred_bills_none', 'referred_bills_single', 'referred_bills_every', 'referred_laws', 'referred_laws_not', 'referred_laws_in', 'referred_laws_not_in', 'referred_laws_some', 'referred_laws_none', 'referred_laws_single', 'referred_laws_every', 'referred_members', 'referred_members_not', 'referred_members_in', 'referred_members_not_in', 'referred_members_some', 'referred_members_none', 'referred_members_single', 'referred_members_every')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(ID, graphql_name='id_contains')
    id_not_contains = sgqlc.types.Field(ID, graphql_name='id_not_contains')
    id_starts_with = sgqlc.types.Field(ID, graphql_name='id_starts_with')
    id_not_starts_with = sgqlc.types.Field(ID, graphql_name='id_not_starts_with')
    id_ends_with = sgqlc.types.Field(ID, graphql_name='id_ends_with')
    id_not_ends_with = sgqlc.types.Field(ID, graphql_name='id_not_ends_with')
    url = sgqlc.types.Field(String, graphql_name='url')
    url_not = sgqlc.types.Field(String, graphql_name='url_not')
    url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='url_in')
    url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='url_not_in')
    url_contains = sgqlc.types.Field(String, graphql_name='url_contains')
    url_not_contains = sgqlc.types.Field(String, graphql_name='url_not_contains')
    url_starts_with = sgqlc.types.Field(String, graphql_name='url_starts_with')
    url_not_starts_with = sgqlc.types.Field(String, graphql_name='url_not_starts_with')
    url_ends_with = sgqlc.types.Field(String, graphql_name='url_ends_with')
    url_not_ends_with = sgqlc.types.Field(String, graphql_name='url_not_ends_with')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    domain_not = sgqlc.types.Field(String, graphql_name='domain_not')
    domain_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='domain_in')
    domain_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='domain_not_in')
    domain_contains = sgqlc.types.Field(String, graphql_name='domain_contains')
    domain_not_contains = sgqlc.types.Field(String, graphql_name='domain_not_contains')
    domain_starts_with = sgqlc.types.Field(String, graphql_name='domain_starts_with')
    domain_not_starts_with = sgqlc.types.Field(String, graphql_name='domain_not_starts_with')
    domain_ends_with = sgqlc.types.Field(String, graphql_name='domain_ends_with')
    domain_not_ends_with = sgqlc.types.Field(String, graphql_name='domain_not_ends_with')
    title = sgqlc.types.Field(String, graphql_name='title')
    title_not = sgqlc.types.Field(String, graphql_name='title_not')
    title_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='title_in')
    title_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='title_not_in')
    title_contains = sgqlc.types.Field(String, graphql_name='title_contains')
    title_not_contains = sgqlc.types.Field(String, graphql_name='title_not_contains')
    title_starts_with = sgqlc.types.Field(String, graphql_name='title_starts_with')
    title_not_starts_with = sgqlc.types.Field(String, graphql_name='title_not_starts_with')
    title_ends_with = sgqlc.types.Field(String, graphql_name='title_ends_with')
    title_not_ends_with = sgqlc.types.Field(String, graphql_name='title_not_ends_with')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_not = sgqlc.types.Field(String, graphql_name='description_not')
    description_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='description_in')
    description_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='description_not_in')
    description_contains = sgqlc.types.Field(String, graphql_name='description_contains')
    description_not_contains = sgqlc.types.Field(String, graphql_name='description_not_contains')
    description_starts_with = sgqlc.types.Field(String, graphql_name='description_starts_with')
    description_not_starts_with = sgqlc.types.Field(String, graphql_name='description_not_starts_with')
    description_ends_with = sgqlc.types.Field(String, graphql_name='description_ends_with')
    description_not_ends_with = sgqlc.types.Field(String, graphql_name='description_not_ends_with')
    referred_bills = sgqlc.types.Field(_BillFilter, graphql_name='referredBills')
    referred_bills_not = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_not')
    referred_bills_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='referredBills_in')
    referred_bills_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='referredBills_not_in')
    referred_bills_some = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_some')
    referred_bills_none = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_none')
    referred_bills_single = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_single')
    referred_bills_every = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_every')
    referred_laws = sgqlc.types.Field(_LawFilter, graphql_name='referredLaws')
    referred_laws_not = sgqlc.types.Field(_LawFilter, graphql_name='referredLaws_not')
    referred_laws_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_LawFilter)), graphql_name='referredLaws_in')
    referred_laws_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_LawFilter)), graphql_name='referredLaws_not_in')
    referred_laws_some = sgqlc.types.Field(_LawFilter, graphql_name='referredLaws_some')
    referred_laws_none = sgqlc.types.Field(_LawFilter, graphql_name='referredLaws_none')
    referred_laws_single = sgqlc.types.Field(_LawFilter, graphql_name='referredLaws_single')
    referred_laws_every = sgqlc.types.Field(_LawFilter, graphql_name='referredLaws_every')
    referred_members = sgqlc.types.Field(_MemberFilter, graphql_name='referredMembers')
    referred_members_not = sgqlc.types.Field(_MemberFilter, graphql_name='referredMembers_not')
    referred_members_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MemberFilter)), graphql_name='referredMembers_in')
    referred_members_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MemberFilter)), graphql_name='referredMembers_not_in')
    referred_members_some = sgqlc.types.Field(_MemberFilter, graphql_name='referredMembers_some')
    referred_members_none = sgqlc.types.Field(_MemberFilter, graphql_name='referredMembers_none')
    referred_members_single = sgqlc.types.Field(_MemberFilter, graphql_name='referredMembers_single')
    referred_members_every = sgqlc.types.Field(_MemberFilter, graphql_name='referredMembers_every')


class _UrlInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')



########################################################################
# Output Objects and Interfaces
########################################################################
class Bill(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'bill_title', 'bill_number', 'bill_category', 'bill_type', 'be_submitted_by_members', 'be_received_by_diet', 'be_discussed_by_minutes', 'amended_laws', 'submitted_date', 'passed_syugiin_committee_date', 'passed_syugiin_date', 'passed_sangiin_committee_date', 'passed_sangiin_date', 'proclaimed_date', 'urls', 'timelines', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    bill_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='billTitle')
    bill_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='billNumber')
    bill_category = sgqlc.types.Field(sgqlc.types.non_null(BillCategory), graphql_name='billCategory')
    bill_type = sgqlc.types.Field(BillType, graphql_name='billType')
    be_submitted_by_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Member'))), graphql_name='beSubmittedByMembers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MemberOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MemberFilter, graphql_name='filter', default=None)),
))
    )
    be_received_by_diet = sgqlc.types.Field('Diet', graphql_name='beReceivedByDiet', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_DietFilter, graphql_name='filter', default=None)),
))
    )
    be_discussed_by_minutes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Minutes'))), graphql_name='beDiscussedByMinutes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MinutesOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MinutesFilter, graphql_name='filter', default=None)),
))
    )
    amended_laws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Law'))), graphql_name='amendedLaws', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_LawOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_LawFilter, graphql_name='filter', default=None)),
))
    )
    submitted_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='submittedDate')
    passed_syugiin_committee_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='passedSyugiinCommitteeDate')
    passed_syugiin_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='passedSyugiinDate')
    passed_sangiin_committee_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='passedSangiinCommitteeDate')
    passed_sangiin_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='passedSangiinDate')
    proclaimed_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='proclaimedDate')
    urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Url'))), graphql_name='urls', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UrlOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UrlFilter, graphql_name='filter', default=None)),
))
    )
    timelines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Timeline'))), graphql_name='timelines', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_TimelineOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_TimelineFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Committee(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'house', 'members', 'minutes', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    house = sgqlc.types.Field(sgqlc.types.non_null(House), graphql_name='house')
    members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Member'))), graphql_name='members', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MemberOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MemberFilter, graphql_name='filter', default=None)),
))
    )
    minutes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Minutes'))), graphql_name='minutes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MinutesOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MinutesFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Diet(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'number', 'name', 'start_date', 'end_date', 'received_bills', 'minutes', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    start_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='startDate')
    end_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='endDate')
    received_bills = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bill))), graphql_name='receivedBills', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    minutes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Minutes'))), graphql_name='minutes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MinutesOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MinutesFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Election(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'election_type', 'district', 'prefecture', 'datetime', 'elected_members', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    election_type = sgqlc.types.Field(sgqlc.types.non_null(ElectionType), graphql_name='electionType')
    district = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='district')
    prefecture = sgqlc.types.Field(String, graphql_name='prefecture')
    datetime = sgqlc.types.Field(sgqlc.types.non_null('_Neo4jDateTime'), graphql_name='datetime')
    elected_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Member'))), graphql_name='electedMembers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MemberOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MemberFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Law(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'law_title', 'law_number', 'be_discussed_by_minutes', 'referred_laws', 'be_referred_by_laws', 'be_amended_by_bills', 'urls', 'timelines', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    law_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lawTitle')
    law_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lawNumber')
    be_discussed_by_minutes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Minutes'))), graphql_name='beDiscussedByMinutes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MinutesOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MinutesFilter, graphql_name='filter', default=None)),
))
    )
    referred_laws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Law'))), graphql_name='referredLaws', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_LawOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_LawFilter, graphql_name='filter', default=None)),
))
    )
    be_referred_by_laws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Law'))), graphql_name='beReferredByLaws', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_LawOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_LawFilter, graphql_name='filter', default=None)),
))
    )
    be_amended_by_bills = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bill))), graphql_name='beAmendedByBills', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Url'))), graphql_name='urls', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UrlOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UrlFilter, graphql_name='filter', default=None)),
))
    )
    timelines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Timeline'))), graphql_name='timelines', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_TimelineOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_TimelineFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Member(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'name_hira', 'first_name', 'first_name_hira', 'last_name', 'last_name_hira', 'house', 'be_elected_by_elections', 'submitted_bills', 'attended_diets', 'attended_minutes', 'urls', 'timelines', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_hira = sgqlc.types.Field(String, graphql_name='nameHira')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    first_name_hira = sgqlc.types.Field(String, graphql_name='firstNameHira')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    last_name_hira = sgqlc.types.Field(String, graphql_name='lastNameHira')
    house = sgqlc.types.Field(House, graphql_name='house')
    be_elected_by_elections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Election))), graphql_name='beElectedByElections', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_ElectionOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_ElectionFilter, graphql_name='filter', default=None)),
))
    )
    submitted_bills = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bill))), graphql_name='submittedBills', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    attended_diets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Diet))), graphql_name='attendedDiets', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_DietOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_DietFilter, graphql_name='filter', default=None)),
))
    )
    attended_minutes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Minutes'))), graphql_name='attendedMinutes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MinutesOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MinutesFilter, graphql_name='filter', default=None)),
))
    )
    urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Url'))), graphql_name='urls', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UrlOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UrlFilter, graphql_name='filter', default=None)),
))
    )
    timelines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Timeline'))), graphql_name='timelines', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_TimelineOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_TimelineFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Minutes(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'minutes_number', 'start_date_time', 'end_date_time', 'belonged_to_diet', 'belonged_to_committee', 'be_attended_by_members', 'topics', 'discussed_bills', 'discussed_laws', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    minutes_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='minutesNumber')
    start_date_time = sgqlc.types.Field('_Neo4jDateTime', graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field('_Neo4jDateTime', graphql_name='endDateTime')
    belonged_to_diet = sgqlc.types.Field(Diet, graphql_name='belongedToDiet', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_DietFilter, graphql_name='filter', default=None)),
))
    )
    belonged_to_committee = sgqlc.types.Field(Committee, graphql_name='belongedToCommittee', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_CommitteeFilter, graphql_name='filter', default=None)),
))
    )
    be_attended_by_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Member))), graphql_name='beAttendedByMembers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MemberOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MemberFilter, graphql_name='filter', default=None)),
))
    )
    topics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='topics')
    discussed_bills = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bill))), graphql_name='discussedBills', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    discussed_laws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Law))), graphql_name='discussedLaws', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_LawOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_LawFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Mutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('add_member_be_elected_by_elections', 'remove_member_be_elected_by_elections', 'merge_member_be_elected_by_elections', 'add_member_submitted_bills', 'remove_member_submitted_bills', 'merge_member_submitted_bills', 'add_member_attended_diets', 'remove_member_attended_diets', 'merge_member_attended_diets', 'add_member_attended_minutes', 'remove_member_attended_minutes', 'merge_member_attended_minutes', 'add_member_urls', 'remove_member_urls', 'merge_member_urls', 'add_member_timelines', 'remove_member_timelines', 'merge_member_timelines', 'create_member', 'update_member', 'delete_member', 'merge_member', 'add_election_elected_members', 'remove_election_elected_members', 'merge_election_elected_members', 'create_election', 'update_election', 'delete_election', 'merge_election', 'add_diet_received_bills', 'remove_diet_received_bills', 'merge_diet_received_bills', 'add_diet_minutes', 'remove_diet_minutes', 'merge_diet_minutes', 'create_diet', 'update_diet', 'delete_diet', 'merge_diet', 'add_law_be_discussed_by_minutes', 'remove_law_be_discussed_by_minutes', 'merge_law_be_discussed_by_minutes', 'add_law_referred_laws', 'remove_law_referred_laws', 'merge_law_referred_laws', 'add_law_be_referred_by_laws', 'remove_law_be_referred_by_laws', 'merge_law_be_referred_by_laws', 'add_law_be_amended_by_bills', 'remove_law_be_amended_by_bills', 'merge_law_be_amended_by_bills', 'add_law_urls', 'remove_law_urls', 'merge_law_urls', 'add_law_timelines', 'remove_law_timelines', 'merge_law_timelines', 'create_law', 'update_law', 'delete_law', 'merge_law', 'add_bill_be_submitted_by_members', 'remove_bill_be_submitted_by_members', 'merge_bill_be_submitted_by_members', 'add_bill_be_received_by_diet', 'remove_bill_be_received_by_diet', 'merge_bill_be_received_by_diet', 'add_bill_be_discussed_by_minutes', 'remove_bill_be_discussed_by_minutes', 'merge_bill_be_discussed_by_minutes', 'add_bill_amended_laws', 'remove_bill_amended_laws', 'merge_bill_amended_laws', 'add_bill_urls', 'remove_bill_urls', 'merge_bill_urls', 'add_bill_timelines', 'remove_bill_timelines', 'merge_bill_timelines', 'create_bill', 'update_bill', 'delete_bill', 'merge_bill', 'add_committee_members', 'remove_committee_members', 'merge_committee_members', 'add_committee_minutes', 'remove_committee_minutes', 'merge_committee_minutes', 'create_committee', 'update_committee', 'delete_committee', 'merge_committee', 'add_minutes_belonged_to_diet', 'remove_minutes_belonged_to_diet', 'merge_minutes_belonged_to_diet', 'add_minutes_belonged_to_committee', 'remove_minutes_belonged_to_committee', 'merge_minutes_belonged_to_committee', 'add_minutes_be_attended_by_members', 'remove_minutes_be_attended_by_members', 'merge_minutes_be_attended_by_members', 'add_minutes_discussed_bills', 'remove_minutes_discussed_bills', 'merge_minutes_discussed_bills', 'add_minutes_discussed_laws', 'remove_minutes_discussed_laws', 'merge_minutes_discussed_laws', 'create_minutes', 'update_minutes', 'delete_minutes', 'merge_minutes', 'add_url_referred_bills', 'remove_url_referred_bills', 'merge_url_referred_bills', 'add_url_referred_laws', 'remove_url_referred_laws', 'merge_url_referred_laws', 'add_url_referred_members', 'remove_url_referred_members', 'merge_url_referred_members', 'create_url', 'update_url', 'delete_url', 'merge_url', 'add_timeline_referred_bills', 'remove_timeline_referred_bills', 'merge_timeline_referred_bills', 'add_timeline_referred_laws', 'remove_timeline_referred_laws', 'merge_timeline_referred_laws', 'add_timeline_referred_members', 'remove_timeline_referred_members', 'merge_timeline_referred_members', 'create_timeline', 'update_timeline', 'delete_timeline', 'merge_timeline')
    add_member_be_elected_by_elections = sgqlc.types.Field('_AddMemberBeElectedByElectionsPayload', graphql_name='AddMemberBeElectedByElections', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    remove_member_be_elected_by_elections = sgqlc.types.Field('_RemoveMemberBeElectedByElectionsPayload', graphql_name='RemoveMemberBeElectedByElections', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    merge_member_be_elected_by_elections = sgqlc.types.Field('_MergeMemberBeElectedByElectionsPayload', graphql_name='MergeMemberBeElectedByElections', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    add_member_submitted_bills = sgqlc.types.Field('_AddMemberSubmittedBillsPayload', graphql_name='AddMemberSubmittedBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_member_submitted_bills = sgqlc.types.Field('_RemoveMemberSubmittedBillsPayload', graphql_name='RemoveMemberSubmittedBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_member_submitted_bills = sgqlc.types.Field('_MergeMemberSubmittedBillsPayload', graphql_name='MergeMemberSubmittedBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    add_member_attended_diets = sgqlc.types.Field('_AddMemberAttendedDietsPayload', graphql_name='AddMemberAttendedDiets', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    remove_member_attended_diets = sgqlc.types.Field('_RemoveMemberAttendedDietsPayload', graphql_name='RemoveMemberAttendedDiets', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    merge_member_attended_diets = sgqlc.types.Field('_MergeMemberAttendedDietsPayload', graphql_name='MergeMemberAttendedDiets', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    add_member_attended_minutes = sgqlc.types.Field('_AddMemberAttendedMinutesPayload', graphql_name='AddMemberAttendedMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    remove_member_attended_minutes = sgqlc.types.Field('_RemoveMemberAttendedMinutesPayload', graphql_name='RemoveMemberAttendedMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    merge_member_attended_minutes = sgqlc.types.Field('_MergeMemberAttendedMinutesPayload', graphql_name='MergeMemberAttendedMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    add_member_urls = sgqlc.types.Field('_AddMemberUrlsPayload', graphql_name='AddMemberUrls', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    remove_member_urls = sgqlc.types.Field('_RemoveMemberUrlsPayload', graphql_name='RemoveMemberUrls', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    merge_member_urls = sgqlc.types.Field('_MergeMemberUrlsPayload', graphql_name='MergeMemberUrls', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    add_member_timelines = sgqlc.types.Field('_AddMemberTimelinesPayload', graphql_name='AddMemberTimelines', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    remove_member_timelines = sgqlc.types.Field('_RemoveMemberTimelinesPayload', graphql_name='RemoveMemberTimelines', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    merge_member_timelines = sgqlc.types.Field('_MergeMemberTimelinesPayload', graphql_name='MergeMemberTimelines', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    create_member = sgqlc.types.Field(Member, graphql_name='CreateMember', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('name_hira', sgqlc.types.Arg(String, graphql_name='nameHira', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('first_name_hira', sgqlc.types.Arg(String, graphql_name='firstNameHira', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
        ('last_name_hira', sgqlc.types.Arg(String, graphql_name='lastNameHira', default=None)),
        ('house', sgqlc.types.Arg(House, graphql_name='house', default=None)),
))
    )
    update_member = sgqlc.types.Field(Member, graphql_name='UpdateMember', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('name_hira', sgqlc.types.Arg(String, graphql_name='nameHira', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('first_name_hira', sgqlc.types.Arg(String, graphql_name='firstNameHira', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
        ('last_name_hira', sgqlc.types.Arg(String, graphql_name='lastNameHira', default=None)),
        ('house', sgqlc.types.Arg(House, graphql_name='house', default=None)),
))
    )
    delete_member = sgqlc.types.Field(Member, graphql_name='DeleteMember', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_member = sgqlc.types.Field(Member, graphql_name='MergeMember', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('name_hira', sgqlc.types.Arg(String, graphql_name='nameHira', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('first_name_hira', sgqlc.types.Arg(String, graphql_name='firstNameHira', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
        ('last_name_hira', sgqlc.types.Arg(String, graphql_name='lastNameHira', default=None)),
        ('house', sgqlc.types.Arg(House, graphql_name='house', default=None)),
))
    )
    add_election_elected_members = sgqlc.types.Field('_AddElectionElectedMembersPayload', graphql_name='AddElectionElectedMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    remove_election_elected_members = sgqlc.types.Field('_RemoveElectionElectedMembersPayload', graphql_name='RemoveElectionElectedMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    merge_election_elected_members = sgqlc.types.Field('_MergeElectionElectedMembersPayload', graphql_name='MergeElectionElectedMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    create_election = sgqlc.types.Field(Election, graphql_name='CreateElection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('election_type', sgqlc.types.Arg(sgqlc.types.non_null(ElectionType), graphql_name='electionType', default=None)),
        ('district', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='district', default=None)),
        ('prefecture', sgqlc.types.Arg(String, graphql_name='prefecture', default=None)),
        ('datetime', sgqlc.types.Arg(sgqlc.types.non_null(_Neo4jDateTimeInput), graphql_name='datetime', default=None)),
))
    )
    update_election = sgqlc.types.Field(Election, graphql_name='UpdateElection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('election_type', sgqlc.types.Arg(ElectionType, graphql_name='electionType', default=None)),
        ('district', sgqlc.types.Arg(String, graphql_name='district', default=None)),
        ('prefecture', sgqlc.types.Arg(String, graphql_name='prefecture', default=None)),
        ('datetime', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='datetime', default=None)),
))
    )
    delete_election = sgqlc.types.Field(Election, graphql_name='DeleteElection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_election = sgqlc.types.Field(Election, graphql_name='MergeElection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('election_type', sgqlc.types.Arg(ElectionType, graphql_name='electionType', default=None)),
        ('district', sgqlc.types.Arg(String, graphql_name='district', default=None)),
        ('prefecture', sgqlc.types.Arg(String, graphql_name='prefecture', default=None)),
        ('datetime', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='datetime', default=None)),
))
    )
    add_diet_received_bills = sgqlc.types.Field('_AddDietReceivedBillsPayload', graphql_name='AddDietReceivedBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_diet_received_bills = sgqlc.types.Field('_RemoveDietReceivedBillsPayload', graphql_name='RemoveDietReceivedBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_diet_received_bills = sgqlc.types.Field('_MergeDietReceivedBillsPayload', graphql_name='MergeDietReceivedBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    add_diet_minutes = sgqlc.types.Field('_AddDietMinutesPayload', graphql_name='AddDietMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    remove_diet_minutes = sgqlc.types.Field('_RemoveDietMinutesPayload', graphql_name='RemoveDietMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    merge_diet_minutes = sgqlc.types.Field('_MergeDietMinutesPayload', graphql_name='MergeDietMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    create_diet = sgqlc.types.Field(Diet, graphql_name='CreateDiet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('start_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startDate', default=None)),
        ('end_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='endDate', default=None)),
))
    )
    update_diet = sgqlc.types.Field(Diet, graphql_name='UpdateDiet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('number', sgqlc.types.Arg(Int, graphql_name='number', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('start_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startDate', default=None)),
        ('end_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='endDate', default=None)),
))
    )
    delete_diet = sgqlc.types.Field(Diet, graphql_name='DeleteDiet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_diet = sgqlc.types.Field(Diet, graphql_name='MergeDiet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('number', sgqlc.types.Arg(Int, graphql_name='number', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('start_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startDate', default=None)),
        ('end_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='endDate', default=None)),
))
    )
    add_law_be_discussed_by_minutes = sgqlc.types.Field('_AddLawBeDiscussedByMinutesPayload', graphql_name='AddLawBeDiscussedByMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    remove_law_be_discussed_by_minutes = sgqlc.types.Field('_RemoveLawBeDiscussedByMinutesPayload', graphql_name='RemoveLawBeDiscussedByMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    merge_law_be_discussed_by_minutes = sgqlc.types.Field('_MergeLawBeDiscussedByMinutesPayload', graphql_name='MergeLawBeDiscussedByMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    add_law_referred_laws = sgqlc.types.Field('_AddLawReferredLawsPayload', graphql_name='AddLawReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    remove_law_referred_laws = sgqlc.types.Field('_RemoveLawReferredLawsPayload', graphql_name='RemoveLawReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    merge_law_referred_laws = sgqlc.types.Field('_MergeLawReferredLawsPayload', graphql_name='MergeLawReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    add_law_be_referred_by_laws = sgqlc.types.Field('_AddLawBeReferredByLawsPayload', graphql_name='AddLawBeReferredByLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    remove_law_be_referred_by_laws = sgqlc.types.Field('_RemoveLawBeReferredByLawsPayload', graphql_name='RemoveLawBeReferredByLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    merge_law_be_referred_by_laws = sgqlc.types.Field('_MergeLawBeReferredByLawsPayload', graphql_name='MergeLawBeReferredByLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    add_law_be_amended_by_bills = sgqlc.types.Field('_AddLawBeAmendedByBillsPayload', graphql_name='AddLawBeAmendedByBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    remove_law_be_amended_by_bills = sgqlc.types.Field('_RemoveLawBeAmendedByBillsPayload', graphql_name='RemoveLawBeAmendedByBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    merge_law_be_amended_by_bills = sgqlc.types.Field('_MergeLawBeAmendedByBillsPayload', graphql_name='MergeLawBeAmendedByBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    add_law_urls = sgqlc.types.Field('_AddLawUrlsPayload', graphql_name='AddLawUrls', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    remove_law_urls = sgqlc.types.Field('_RemoveLawUrlsPayload', graphql_name='RemoveLawUrls', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    merge_law_urls = sgqlc.types.Field('_MergeLawUrlsPayload', graphql_name='MergeLawUrls', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    add_law_timelines = sgqlc.types.Field('_AddLawTimelinesPayload', graphql_name='AddLawTimelines', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    remove_law_timelines = sgqlc.types.Field('_RemoveLawTimelinesPayload', graphql_name='RemoveLawTimelines', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    merge_law_timelines = sgqlc.types.Field('_MergeLawTimelinesPayload', graphql_name='MergeLawTimelines', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    create_law = sgqlc.types.Field(Law, graphql_name='CreateLaw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('law_title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='lawTitle', default=None)),
        ('law_number', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='lawNumber', default=None)),
))
    )
    update_law = sgqlc.types.Field(Law, graphql_name='UpdateLaw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('law_title', sgqlc.types.Arg(String, graphql_name='lawTitle', default=None)),
        ('law_number', sgqlc.types.Arg(String, graphql_name='lawNumber', default=None)),
))
    )
    delete_law = sgqlc.types.Field(Law, graphql_name='DeleteLaw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_law = sgqlc.types.Field(Law, graphql_name='MergeLaw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('law_title', sgqlc.types.Arg(String, graphql_name='lawTitle', default=None)),
        ('law_number', sgqlc.types.Arg(String, graphql_name='lawNumber', default=None)),
))
    )
    add_bill_be_submitted_by_members = sgqlc.types.Field('_AddBillBeSubmittedByMembersPayload', graphql_name='AddBillBeSubmittedByMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_bill_be_submitted_by_members = sgqlc.types.Field('_RemoveBillBeSubmittedByMembersPayload', graphql_name='RemoveBillBeSubmittedByMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_bill_be_submitted_by_members = sgqlc.types.Field('_MergeBillBeSubmittedByMembersPayload', graphql_name='MergeBillBeSubmittedByMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    add_bill_be_received_by_diet = sgqlc.types.Field('_AddBillBeReceivedByDietPayload', graphql_name='AddBillBeReceivedByDiet', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_bill_be_received_by_diet = sgqlc.types.Field('_RemoveBillBeReceivedByDietPayload', graphql_name='RemoveBillBeReceivedByDiet', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_bill_be_received_by_diet = sgqlc.types.Field('_MergeBillBeReceivedByDietPayload', graphql_name='MergeBillBeReceivedByDiet', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    add_bill_be_discussed_by_minutes = sgqlc.types.Field('_AddBillBeDiscussedByMinutesPayload', graphql_name='AddBillBeDiscussedByMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_bill_be_discussed_by_minutes = sgqlc.types.Field('_RemoveBillBeDiscussedByMinutesPayload', graphql_name='RemoveBillBeDiscussedByMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_bill_be_discussed_by_minutes = sgqlc.types.Field('_MergeBillBeDiscussedByMinutesPayload', graphql_name='MergeBillBeDiscussedByMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    add_bill_amended_laws = sgqlc.types.Field('_AddBillAmendedLawsPayload', graphql_name='AddBillAmendedLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    remove_bill_amended_laws = sgqlc.types.Field('_RemoveBillAmendedLawsPayload', graphql_name='RemoveBillAmendedLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    merge_bill_amended_laws = sgqlc.types.Field('_MergeBillAmendedLawsPayload', graphql_name='MergeBillAmendedLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    add_bill_urls = sgqlc.types.Field('_AddBillUrlsPayload', graphql_name='AddBillUrls', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_bill_urls = sgqlc.types.Field('_RemoveBillUrlsPayload', graphql_name='RemoveBillUrls', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_bill_urls = sgqlc.types.Field('_MergeBillUrlsPayload', graphql_name='MergeBillUrls', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    add_bill_timelines = sgqlc.types.Field('_AddBillTimelinesPayload', graphql_name='AddBillTimelines', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_bill_timelines = sgqlc.types.Field('_RemoveBillTimelinesPayload', graphql_name='RemoveBillTimelines', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_bill_timelines = sgqlc.types.Field('_MergeBillTimelinesPayload', graphql_name='MergeBillTimelines', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    create_bill = sgqlc.types.Field(Bill, graphql_name='CreateBill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('bill_title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='billTitle', default=None)),
        ('bill_number', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='billNumber', default=None)),
        ('bill_category', sgqlc.types.Arg(sgqlc.types.non_null(BillCategory), graphql_name='billCategory', default=None)),
        ('bill_type', sgqlc.types.Arg(BillType, graphql_name='billType', default=None)),
        ('submitted_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='submittedDate', default=None)),
        ('passed_syugiin_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSyugiinCommitteeDate', default=None)),
        ('passed_syugiin_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSyugiinDate', default=None)),
        ('passed_sangiin_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSangiinCommitteeDate', default=None)),
        ('passed_sangiin_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSangiinDate', default=None)),
        ('proclaimed_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='proclaimedDate', default=None)),
))
    )
    update_bill = sgqlc.types.Field(Bill, graphql_name='UpdateBill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('bill_title', sgqlc.types.Arg(String, graphql_name='billTitle', default=None)),
        ('bill_number', sgqlc.types.Arg(String, graphql_name='billNumber', default=None)),
        ('bill_category', sgqlc.types.Arg(BillCategory, graphql_name='billCategory', default=None)),
        ('bill_type', sgqlc.types.Arg(BillType, graphql_name='billType', default=None)),
        ('submitted_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='submittedDate', default=None)),
        ('passed_syugiin_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSyugiinCommitteeDate', default=None)),
        ('passed_syugiin_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSyugiinDate', default=None)),
        ('passed_sangiin_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSangiinCommitteeDate', default=None)),
        ('passed_sangiin_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSangiinDate', default=None)),
        ('proclaimed_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='proclaimedDate', default=None)),
))
    )
    delete_bill = sgqlc.types.Field(Bill, graphql_name='DeleteBill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_bill = sgqlc.types.Field(Bill, graphql_name='MergeBill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('bill_title', sgqlc.types.Arg(String, graphql_name='billTitle', default=None)),
        ('bill_number', sgqlc.types.Arg(String, graphql_name='billNumber', default=None)),
        ('bill_category', sgqlc.types.Arg(BillCategory, graphql_name='billCategory', default=None)),
        ('bill_type', sgqlc.types.Arg(BillType, graphql_name='billType', default=None)),
        ('submitted_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='submittedDate', default=None)),
        ('passed_syugiin_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSyugiinCommitteeDate', default=None)),
        ('passed_syugiin_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSyugiinDate', default=None)),
        ('passed_sangiin_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSangiinCommitteeDate', default=None)),
        ('passed_sangiin_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSangiinDate', default=None)),
        ('proclaimed_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='proclaimedDate', default=None)),
))
    )
    add_committee_members = sgqlc.types.Field('_AddCommitteeMembersPayload', graphql_name='AddCommitteeMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_CommitteeInput), graphql_name='to', default=None)),
))
    )
    remove_committee_members = sgqlc.types.Field('_RemoveCommitteeMembersPayload', graphql_name='RemoveCommitteeMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_CommitteeInput), graphql_name='to', default=None)),
))
    )
    merge_committee_members = sgqlc.types.Field('_MergeCommitteeMembersPayload', graphql_name='MergeCommitteeMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_CommitteeInput), graphql_name='to', default=None)),
))
    )
    add_committee_minutes = sgqlc.types.Field('_AddCommitteeMinutesPayload', graphql_name='AddCommitteeMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_CommitteeInput), graphql_name='to', default=None)),
))
    )
    remove_committee_minutes = sgqlc.types.Field('_RemoveCommitteeMinutesPayload', graphql_name='RemoveCommitteeMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_CommitteeInput), graphql_name='to', default=None)),
))
    )
    merge_committee_minutes = sgqlc.types.Field('_MergeCommitteeMinutesPayload', graphql_name='MergeCommitteeMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_CommitteeInput), graphql_name='to', default=None)),
))
    )
    create_committee = sgqlc.types.Field(Committee, graphql_name='CreateCommittee', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('house', sgqlc.types.Arg(sgqlc.types.non_null(House), graphql_name='house', default=None)),
))
    )
    update_committee = sgqlc.types.Field(Committee, graphql_name='UpdateCommittee', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('house', sgqlc.types.Arg(House, graphql_name='house', default=None)),
))
    )
    delete_committee = sgqlc.types.Field(Committee, graphql_name='DeleteCommittee', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_committee = sgqlc.types.Field(Committee, graphql_name='MergeCommittee', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('house', sgqlc.types.Arg(House, graphql_name='house', default=None)),
))
    )
    add_minutes_belonged_to_diet = sgqlc.types.Field('_AddMinutesBelongedToDietPayload', graphql_name='AddMinutesBelongedToDiet', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    remove_minutes_belonged_to_diet = sgqlc.types.Field('_RemoveMinutesBelongedToDietPayload', graphql_name='RemoveMinutesBelongedToDiet', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    merge_minutes_belonged_to_diet = sgqlc.types.Field('_MergeMinutesBelongedToDietPayload', graphql_name='MergeMinutesBelongedToDiet', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    add_minutes_belonged_to_committee = sgqlc.types.Field('_AddMinutesBelongedToCommitteePayload', graphql_name='AddMinutesBelongedToCommittee', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_CommitteeInput), graphql_name='to', default=None)),
))
    )
    remove_minutes_belonged_to_committee = sgqlc.types.Field('_RemoveMinutesBelongedToCommitteePayload', graphql_name='RemoveMinutesBelongedToCommittee', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_CommitteeInput), graphql_name='to', default=None)),
))
    )
    merge_minutes_belonged_to_committee = sgqlc.types.Field('_MergeMinutesBelongedToCommitteePayload', graphql_name='MergeMinutesBelongedToCommittee', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_CommitteeInput), graphql_name='to', default=None)),
))
    )
    add_minutes_be_attended_by_members = sgqlc.types.Field('_AddMinutesBeAttendedByMembersPayload', graphql_name='AddMinutesBeAttendedByMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    remove_minutes_be_attended_by_members = sgqlc.types.Field('_RemoveMinutesBeAttendedByMembersPayload', graphql_name='RemoveMinutesBeAttendedByMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    merge_minutes_be_attended_by_members = sgqlc.types.Field('_MergeMinutesBeAttendedByMembersPayload', graphql_name='MergeMinutesBeAttendedByMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    add_minutes_discussed_bills = sgqlc.types.Field('_AddMinutesDiscussedBillsPayload', graphql_name='AddMinutesDiscussedBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_minutes_discussed_bills = sgqlc.types.Field('_RemoveMinutesDiscussedBillsPayload', graphql_name='RemoveMinutesDiscussedBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_minutes_discussed_bills = sgqlc.types.Field('_MergeMinutesDiscussedBillsPayload', graphql_name='MergeMinutesDiscussedBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    add_minutes_discussed_laws = sgqlc.types.Field('_AddMinutesDiscussedLawsPayload', graphql_name='AddMinutesDiscussedLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    remove_minutes_discussed_laws = sgqlc.types.Field('_RemoveMinutesDiscussedLawsPayload', graphql_name='RemoveMinutesDiscussedLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    merge_minutes_discussed_laws = sgqlc.types.Field('_MergeMinutesDiscussedLawsPayload', graphql_name='MergeMinutesDiscussedLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    create_minutes = sgqlc.types.Field(Minutes, graphql_name='CreateMinutes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('minutes_number', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='minutesNumber', default=None)),
        ('start_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startDateTime', default=None)),
        ('end_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='endDateTime', default=None)),
        ('topics', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='topics', default=None)),
))
    )
    update_minutes = sgqlc.types.Field(Minutes, graphql_name='UpdateMinutes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('minutes_number', sgqlc.types.Arg(String, graphql_name='minutesNumber', default=None)),
        ('start_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startDateTime', default=None)),
        ('end_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='endDateTime', default=None)),
        ('topics', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='topics', default=None)),
))
    )
    delete_minutes = sgqlc.types.Field(Minutes, graphql_name='DeleteMinutes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_minutes = sgqlc.types.Field(Minutes, graphql_name='MergeMinutes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('minutes_number', sgqlc.types.Arg(String, graphql_name='minutesNumber', default=None)),
        ('start_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startDateTime', default=None)),
        ('end_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='endDateTime', default=None)),
        ('topics', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='topics', default=None)),
))
    )
    add_url_referred_bills = sgqlc.types.Field('_AddUrlReferredBillsPayload', graphql_name='AddUrlReferredBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_url_referred_bills = sgqlc.types.Field('_RemoveUrlReferredBillsPayload', graphql_name='RemoveUrlReferredBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_url_referred_bills = sgqlc.types.Field('_MergeUrlReferredBillsPayload', graphql_name='MergeUrlReferredBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    add_url_referred_laws = sgqlc.types.Field('_AddUrlReferredLawsPayload', graphql_name='AddUrlReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    remove_url_referred_laws = sgqlc.types.Field('_RemoveUrlReferredLawsPayload', graphql_name='RemoveUrlReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    merge_url_referred_laws = sgqlc.types.Field('_MergeUrlReferredLawsPayload', graphql_name='MergeUrlReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    add_url_referred_members = sgqlc.types.Field('_AddUrlReferredMembersPayload', graphql_name='AddUrlReferredMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    remove_url_referred_members = sgqlc.types.Field('_RemoveUrlReferredMembersPayload', graphql_name='RemoveUrlReferredMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    merge_url_referred_members = sgqlc.types.Field('_MergeUrlReferredMembersPayload', graphql_name='MergeUrlReferredMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    create_url = sgqlc.types.Field('Url', graphql_name='CreateUrl', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
        ('domain', sgqlc.types.Arg(String, graphql_name='domain', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
))
    )
    update_url = sgqlc.types.Field('Url', graphql_name='UpdateUrl', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('domain', sgqlc.types.Arg(String, graphql_name='domain', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
))
    )
    delete_url = sgqlc.types.Field('Url', graphql_name='DeleteUrl', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_url = sgqlc.types.Field('Url', graphql_name='MergeUrl', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('domain', sgqlc.types.Arg(String, graphql_name='domain', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
))
    )
    add_timeline_referred_bills = sgqlc.types.Field('_AddTimelineReferredBillsPayload', graphql_name='AddTimelineReferredBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_timeline_referred_bills = sgqlc.types.Field('_RemoveTimelineReferredBillsPayload', graphql_name='RemoveTimelineReferredBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_timeline_referred_bills = sgqlc.types.Field('_MergeTimelineReferredBillsPayload', graphql_name='MergeTimelineReferredBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    add_timeline_referred_laws = sgqlc.types.Field('_AddTimelineReferredLawsPayload', graphql_name='AddTimelineReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    remove_timeline_referred_laws = sgqlc.types.Field('_RemoveTimelineReferredLawsPayload', graphql_name='RemoveTimelineReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    merge_timeline_referred_laws = sgqlc.types.Field('_MergeTimelineReferredLawsPayload', graphql_name='MergeTimelineReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    add_timeline_referred_members = sgqlc.types.Field('_AddTimelineReferredMembersPayload', graphql_name='AddTimelineReferredMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    remove_timeline_referred_members = sgqlc.types.Field('_RemoveTimelineReferredMembersPayload', graphql_name='RemoveTimelineReferredMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    merge_timeline_referred_members = sgqlc.types.Field('_MergeTimelineReferredMembersPayload', graphql_name='MergeTimelineReferredMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    create_timeline = sgqlc.types.Field('Timeline', graphql_name='CreateTimeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('content', sgqlc.types.Arg(String, graphql_name='content', default=None)),
        ('datetime', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='datetime', default=None)),
))
    )
    update_timeline = sgqlc.types.Field('Timeline', graphql_name='UpdateTimeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('content', sgqlc.types.Arg(String, graphql_name='content', default=None)),
        ('datetime', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='datetime', default=None)),
))
    )
    delete_timeline = sgqlc.types.Field('Timeline', graphql_name='DeleteTimeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_timeline = sgqlc.types.Field('Timeline', graphql_name='MergeTimeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('content', sgqlc.types.Arg(String, graphql_name='content', default=None)),
        ('datetime', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='datetime', default=None)),
))
    )


class Query(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('total_members', 'all_members', 'total_elections', 'all_elections', 'total_diets', 'all_diets', 'total_laws', 'all_laws', 'total_bills', 'all_bills', 'total_committees', 'all_committees', 'total_minutes', 'all_minutes', 'member', 'election', 'diet', 'law', 'bill', 'committee', 'minutes', 'url', 'timeline')
    total_members = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalMembers')
    all_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Member'))), graphql_name='allMembers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MemberOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MemberFilter, graphql_name='filter', default=None)),
))
    )
    total_elections = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalElections')
    all_elections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Election'))), graphql_name='allElections', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_ElectionOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_ElectionFilter, graphql_name='filter', default=None)),
))
    )
    total_diets = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalDiets')
    all_diets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Diet'))), graphql_name='allDiets', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_DietOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_DietFilter, graphql_name='filter', default=None)),
))
    )
    total_laws = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalLaws')
    all_laws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Law'))), graphql_name='allLaws', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_LawOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_LawFilter, graphql_name='filter', default=None)),
))
    )
    total_bills = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalBills')
    all_bills = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Bill'))), graphql_name='allBills', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    total_committees = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCommittees')
    all_committees = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Committee'))), graphql_name='allCommittees', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_CommitteeOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_CommitteeFilter, graphql_name='filter', default=None)),
))
    )
    total_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalMinutes')
    all_minutes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Minutes'))), graphql_name='allMinutes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MinutesOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MinutesFilter, graphql_name='filter', default=None)),
))
    )
    member = sgqlc.types.Field(sgqlc.types.list_of('Member'), graphql_name='Member', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('name_hira', sgqlc.types.Arg(String, graphql_name='nameHira', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('first_name_hira', sgqlc.types.Arg(String, graphql_name='firstNameHira', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
        ('last_name_hira', sgqlc.types.Arg(String, graphql_name='lastNameHira', default=None)),
        ('house', sgqlc.types.Arg(House, graphql_name='house', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MemberOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MemberFilter, graphql_name='filter', default=None)),
))
    )
    election = sgqlc.types.Field(sgqlc.types.list_of('Election'), graphql_name='Election', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('election_type', sgqlc.types.Arg(ElectionType, graphql_name='electionType', default=None)),
        ('district', sgqlc.types.Arg(String, graphql_name='district', default=None)),
        ('prefecture', sgqlc.types.Arg(String, graphql_name='prefecture', default=None)),
        ('datetime', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='datetime', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_ElectionOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_ElectionFilter, graphql_name='filter', default=None)),
))
    )
    diet = sgqlc.types.Field(sgqlc.types.list_of('Diet'), graphql_name='Diet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('number', sgqlc.types.Arg(Int, graphql_name='number', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('start_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startDate', default=None)),
        ('end_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='endDate', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_DietOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_DietFilter, graphql_name='filter', default=None)),
))
    )
    law = sgqlc.types.Field(sgqlc.types.list_of('Law'), graphql_name='Law', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('law_title', sgqlc.types.Arg(String, graphql_name='lawTitle', default=None)),
        ('law_number', sgqlc.types.Arg(String, graphql_name='lawNumber', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_LawOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_LawFilter, graphql_name='filter', default=None)),
))
    )
    bill = sgqlc.types.Field(sgqlc.types.list_of('Bill'), graphql_name='Bill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('bill_title', sgqlc.types.Arg(String, graphql_name='billTitle', default=None)),
        ('bill_number', sgqlc.types.Arg(String, graphql_name='billNumber', default=None)),
        ('bill_category', sgqlc.types.Arg(BillCategory, graphql_name='billCategory', default=None)),
        ('bill_type', sgqlc.types.Arg(BillType, graphql_name='billType', default=None)),
        ('submitted_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='submittedDate', default=None)),
        ('passed_syugiin_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSyugiinCommitteeDate', default=None)),
        ('passed_syugiin_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSyugiinDate', default=None)),
        ('passed_sangiin_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSangiinCommitteeDate', default=None)),
        ('passed_sangiin_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedSangiinDate', default=None)),
        ('proclaimed_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='proclaimedDate', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    committee = sgqlc.types.Field(sgqlc.types.list_of('Committee'), graphql_name='Committee', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('house', sgqlc.types.Arg(House, graphql_name='house', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_CommitteeOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_CommitteeFilter, graphql_name='filter', default=None)),
))
    )
    minutes = sgqlc.types.Field(sgqlc.types.list_of('Minutes'), graphql_name='Minutes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('minutes_number', sgqlc.types.Arg(String, graphql_name='minutesNumber', default=None)),
        ('start_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startDateTime', default=None)),
        ('end_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='endDateTime', default=None)),
        ('topics', sgqlc.types.Arg(String, graphql_name='topics', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MinutesOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MinutesFilter, graphql_name='filter', default=None)),
))
    )
    url = sgqlc.types.Field(sgqlc.types.list_of('Url'), graphql_name='Url', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('domain', sgqlc.types.Arg(String, graphql_name='domain', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UrlOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UrlFilter, graphql_name='filter', default=None)),
))
    )
    timeline = sgqlc.types.Field(sgqlc.types.list_of('Timeline'), graphql_name='Timeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('content', sgqlc.types.Arg(String, graphql_name='content', default=None)),
        ('datetime', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='datetime', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_TimelineOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_TimelineFilter, graphql_name='filter', default=None)),
))
    )


class Timeline(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'content', 'datetime', 'referred_bills', 'referred_laws', 'referred_members', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    content = sgqlc.types.Field(String, graphql_name='content')
    datetime = sgqlc.types.Field('_Neo4jDateTime', graphql_name='datetime')
    referred_bills = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bill))), graphql_name='referredBills', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    referred_laws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Law))), graphql_name='referredLaws', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_LawOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_LawFilter, graphql_name='filter', default=None)),
))
    )
    referred_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Member))), graphql_name='referredMembers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MemberOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MemberFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Url(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'url', 'domain', 'title', 'description', 'referred_bills', 'referred_laws', 'referred_members', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    title = sgqlc.types.Field(String, graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    referred_bills = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bill))), graphql_name='referredBills', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    referred_laws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Law))), graphql_name='referredLaws', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_LawOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_LawFilter, graphql_name='filter', default=None)),
))
    )
    referred_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Member))), graphql_name='referredMembers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MemberOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MemberFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class _AddBillAmendedLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _AddBillBeDiscussedByMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddBillBeReceivedByDietPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Diet, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddBillBeSubmittedByMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddBillTimelinesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddBillUrlsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddCommitteeMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Committee, graphql_name='to')


class _AddCommitteeMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Committee, graphql_name='to')


class _AddDietMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _AddDietReceivedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Diet, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddElectionElectedMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Election, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _AddLawBeAmendedByBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _AddLawBeDiscussedByMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _AddLawBeReferredByLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _AddLawReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _AddLawTimelinesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _AddLawUrlsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _AddMemberAttendedDietsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _AddMemberAttendedMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _AddMemberBeElectedByElectionsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Election, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _AddMemberSubmittedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddMemberTimelinesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _AddMemberUrlsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _AddMinutesBeAttendedByMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _AddMinutesBelongedToCommitteePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Committee, graphql_name='to')


class _AddMinutesBelongedToDietPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _AddMinutesDiscussedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddMinutesDiscussedLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _AddTimelineReferredBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddTimelineReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _AddTimelineReferredMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _AddUrlReferredBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddUrlReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _AddUrlReferredMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _MergeBillAmendedLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _MergeBillBeDiscussedByMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeBillBeReceivedByDietPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Diet, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeBillBeSubmittedByMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeBillTimelinesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeBillUrlsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeCommitteeMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Committee, graphql_name='to')


class _MergeCommitteeMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Committee, graphql_name='to')


class _MergeDietMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _MergeDietReceivedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Diet, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeElectionElectedMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Election, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _MergeLawBeAmendedByBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _MergeLawBeDiscussedByMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _MergeLawBeReferredByLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _MergeLawReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _MergeLawTimelinesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _MergeLawUrlsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _MergeMemberAttendedDietsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _MergeMemberAttendedMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _MergeMemberBeElectedByElectionsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Election, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _MergeMemberSubmittedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeMemberTimelinesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _MergeMemberUrlsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _MergeMinutesBeAttendedByMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _MergeMinutesBelongedToCommitteePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Committee, graphql_name='to')


class _MergeMinutesBelongedToDietPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _MergeMinutesDiscussedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeMinutesDiscussedLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _MergeTimelineReferredBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeTimelineReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _MergeTimelineReferredMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _MergeUrlReferredBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeUrlReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _MergeUrlReferredMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _Neo4jDate(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('year', 'month', 'day', 'formatted')
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jDateTime(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('year', 'month', 'day', 'hour', 'minute', 'second', 'millisecond', 'microsecond', 'nanosecond', 'timezone', 'formatted')
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jLocalDateTime(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('year', 'month', 'day', 'hour', 'minute', 'second', 'millisecond', 'microsecond', 'nanosecond', 'formatted')
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jLocalTime(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('hour', 'minute', 'second', 'millisecond', 'microsecond', 'nanosecond', 'formatted')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jPoint(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('x', 'y', 'z', 'longitude', 'latitude', 'height', 'crs', 'srid')
    x = sgqlc.types.Field(Float, graphql_name='x')
    y = sgqlc.types.Field(Float, graphql_name='y')
    z = sgqlc.types.Field(Float, graphql_name='z')
    longitude = sgqlc.types.Field(Float, graphql_name='longitude')
    latitude = sgqlc.types.Field(Float, graphql_name='latitude')
    height = sgqlc.types.Field(Float, graphql_name='height')
    crs = sgqlc.types.Field(String, graphql_name='crs')
    srid = sgqlc.types.Field(Int, graphql_name='srid')


class _Neo4jTime(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('hour', 'minute', 'second', 'millisecond', 'microsecond', 'nanosecond', 'timezone', 'formatted')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _RemoveBillAmendedLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _RemoveBillBeDiscussedByMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveBillBeReceivedByDietPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Diet, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveBillBeSubmittedByMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveBillTimelinesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveBillUrlsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveCommitteeMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Committee, graphql_name='to')


class _RemoveCommitteeMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Committee, graphql_name='to')


class _RemoveDietMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _RemoveDietReceivedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Diet, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveElectionElectedMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Election, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _RemoveLawBeAmendedByBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _RemoveLawBeDiscussedByMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _RemoveLawBeReferredByLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _RemoveLawReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _RemoveLawTimelinesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _RemoveLawUrlsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _RemoveMemberAttendedDietsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _RemoveMemberAttendedMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _RemoveMemberBeElectedByElectionsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Election, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _RemoveMemberSubmittedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveMemberTimelinesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _RemoveMemberUrlsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _RemoveMinutesBeAttendedByMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _RemoveMinutesBelongedToCommitteePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Committee, graphql_name='to')


class _RemoveMinutesBelongedToDietPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _RemoveMinutesDiscussedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveMinutesDiscussedLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _RemoveTimelineReferredBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveTimelineReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _RemoveTimelineReferredMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Timeline, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _RemoveUrlReferredBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveUrlReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _RemoveUrlReferredMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None

