import sgqlc.types


schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class BillCategory(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('KAKUHOU', 'SHUHOU', 'SANHOU')


Boolean = sgqlc.types.Boolean

class DietCategory(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ORDINARY', 'EXTRAORDINARY', 'SPECIAL')


class ElectionSystem(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CONSTITUENCY', 'PROPORTIONAL')


Float = sgqlc.types.Float

class House(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('REPRESENTATIVES', 'COUNCILORS')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

String = sgqlc.types.String

class _BillOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'name_asc', 'name_desc', 'billNumber_asc', 'billNumber_desc', 'category_asc', 'category_desc', 'isAmendment_asc', 'isAmendment_desc', 'isPassed_asc', 'isPassed_desc', 'reason_asc', 'reason_desc', 'summary_asc', 'summary_desc', 'firstHouse_asc', 'firstHouse_desc', 'submittedDate_asc', 'submittedDate_desc', 'passedRepresentativesCommitteeDate_asc', 'passedRepresentativesCommitteeDate_desc', 'passedRepresentativesDate_asc', 'passedRepresentativesDate_desc', 'passedCouncilorsCommitteeDate_asc', 'passedCouncilorsCommitteeDate_desc', 'passedCouncilorsDate_asc', 'passedCouncilorsDate_desc', 'proclaimedDate_asc', 'proclaimedDate_desc', 'totalNews_asc', 'totalNews_desc', 'totalMinutes_asc', 'totalMinutes_desc', '_id_asc', '_id_desc')


class _CommitteeOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'name_asc', 'name_desc', 'numMembers_asc', 'numMembers_desc', 'house_asc', 'house_desc', 'description_asc', 'description_desc', 'totalMinutes_asc', 'totalMinutes_desc', '_id_asc', '_id_desc')


class _DietOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'name_asc', 'name_desc', 'number_asc', 'number_desc', 'category_asc', 'category_desc', 'startDate_asc', 'startDate_desc', 'endDate_asc', 'endDate_desc', '_id_asc', '_id_desc')


class _ElectionOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'name_asc', 'name_desc', 'date_asc', 'date_desc', '_id_asc', '_id_desc')


class _ElectionResultOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'name_asc', 'name_desc', 'system_asc', 'system_desc', 'district_asc', 'district_desc', 'prefecture_asc', 'prefecture_desc', '_id_asc', '_id_desc')


class _LawOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'name_asc', 'name_desc', 'lawNumber_asc', 'lawNumber_desc', 'summary_asc', 'summary_desc', '_id_asc', '_id_desc')


class _MemberOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'name_asc', 'name_desc', 'nameHira_asc', 'nameHira_desc', 'firstName_asc', 'firstName_desc', 'firstNameHira_asc', 'firstNameHira_desc', 'lastName_asc', 'lastName_desc', 'lastNameHira_asc', 'lastNameHira_desc', 'house_asc', 'house_desc', 'description_asc', 'description_desc', '_id_asc', '_id_desc')


class _MinutesOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'name_asc', 'name_desc', 'startDateTime_asc', 'startDateTime_desc', 'endDateTime_asc', 'endDateTime_desc', 'summary_asc', 'summary_desc', 'totalNews_asc', 'totalNews_desc', 'totalBills_asc', 'totalBills_desc', '_id_asc', '_id_desc')


class _NewsOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'url_asc', 'url_desc', 'publisher_asc', 'publisher_desc', 'thumbnail_asc', 'thumbnail_desc', 'title_asc', 'title_desc', 'publishedAt_asc', 'publishedAt_desc', 'lastModifiedAt_asc', 'lastModifiedAt_desc', 'isPaid_asc', 'isPaid_desc', '_id_asc', '_id_desc')


class _RelationDirections(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('IN', 'OUT')


class _SpeechOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'name_asc', 'name_desc', 'speakerName_asc', 'speakerName_desc', 'orderInMinutes_asc', 'orderInMinutes_desc', '_id_asc', '_id_desc')


class _TimelineOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'date_asc', 'date_desc', 'totalBills_asc', 'totalBills_desc', 'totalMinutes_asc', 'totalMinutes_desc', 'totalNews_asc', 'totalNews_desc', '_id_asc', '_id_desc')


class _UrlOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'url_asc', 'url_desc', 'domain_asc', 'domain_desc', 'title_asc', 'title_desc', 'description_asc', 'description_desc', '_id_asc', '_id_desc')



########################################################################
# Input Objects
########################################################################
class _BillFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'bill_number', 'bill_number_not', 'bill_number_in', 'bill_number_not_in', 'bill_number_contains', 'bill_number_not_contains', 'bill_number_starts_with', 'bill_number_not_starts_with', 'bill_number_ends_with', 'bill_number_not_ends_with', 'category', 'category_not', 'category_in', 'category_not_in', 'is_amendment', 'is_amendment_not', 'is_passed', 'is_passed_not', 'reason', 'reason_not', 'reason_in', 'reason_not_in', 'reason_contains', 'reason_not_contains', 'reason_starts_with', 'reason_not_starts_with', 'reason_ends_with', 'reason_not_ends_with', 'summary', 'summary_not', 'summary_in', 'summary_not_in', 'summary_contains', 'summary_not_contains', 'summary_starts_with', 'summary_not_starts_with', 'summary_ends_with', 'summary_not_ends_with', 'first_house', 'first_house_not', 'first_house_in', 'first_house_not_in', 'be_submitted_by_members', 'be_submitted_by_members_not', 'be_submitted_by_members_in', 'be_submitted_by_members_not_in', 'be_submitted_by_members_some', 'be_submitted_by_members_none', 'be_submitted_by_members_single', 'be_submitted_by_members_every', 'be_received_by_diet', 'be_received_by_diet_not', 'be_received_by_diet_in', 'be_received_by_diet_not_in', 'be_discussed_by_minutes', 'be_discussed_by_minutes_not', 'be_discussed_by_minutes_in', 'be_discussed_by_minutes_not_in', 'be_discussed_by_minutes_some', 'be_discussed_by_minutes_none', 'be_discussed_by_minutes_single', 'be_discussed_by_minutes_every', 'amended_laws', 'amended_laws_not', 'amended_laws_in', 'amended_laws_not_in', 'amended_laws_some', 'amended_laws_none', 'amended_laws_single', 'amended_laws_every', 'urls', 'urls_not', 'urls_in', 'urls_not_in', 'urls_some', 'urls_none', 'urls_single', 'urls_every', 'news', 'news_not', 'news_in', 'news_not_in', 'news_some', 'news_none', 'news_single', 'news_every', 'submitted_date', 'submitted_date_not', 'submitted_date_in', 'submitted_date_not_in', 'submitted_date_lt', 'submitted_date_lte', 'submitted_date_gt', 'submitted_date_gte', 'passed_representatives_committee_date', 'passed_representatives_committee_date_not', 'passed_representatives_committee_date_in', 'passed_representatives_committee_date_not_in', 'passed_representatives_committee_date_lt', 'passed_representatives_committee_date_lte', 'passed_representatives_committee_date_gt', 'passed_representatives_committee_date_gte', 'passed_representatives_date', 'passed_representatives_date_not', 'passed_representatives_date_in', 'passed_representatives_date_not_in', 'passed_representatives_date_lt', 'passed_representatives_date_lte', 'passed_representatives_date_gt', 'passed_representatives_date_gte', 'passed_councilors_committee_date', 'passed_councilors_committee_date_not', 'passed_councilors_committee_date_in', 'passed_councilors_committee_date_not_in', 'passed_councilors_committee_date_lt', 'passed_councilors_committee_date_lte', 'passed_councilors_committee_date_gt', 'passed_councilors_committee_date_gte', 'passed_councilors_date', 'passed_councilors_date_not', 'passed_councilors_date_in', 'passed_councilors_date_not_in', 'passed_councilors_date_lt', 'passed_councilors_date_lte', 'passed_councilors_date_gt', 'passed_councilors_date_gte', 'proclaimed_date', 'proclaimed_date_not', 'proclaimed_date_in', 'proclaimed_date_not_in', 'proclaimed_date_lt', 'proclaimed_date_lte', 'proclaimed_date_gt', 'proclaimed_date_gte')
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
    category = sgqlc.types.Field(BillCategory, graphql_name='category')
    category_not = sgqlc.types.Field(BillCategory, graphql_name='category_not')
    category_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BillCategory)), graphql_name='category_in')
    category_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BillCategory)), graphql_name='category_not_in')
    is_amendment = sgqlc.types.Field(Boolean, graphql_name='isAmendment')
    is_amendment_not = sgqlc.types.Field(Boolean, graphql_name='isAmendment_not')
    is_passed = sgqlc.types.Field(Boolean, graphql_name='isPassed')
    is_passed_not = sgqlc.types.Field(Boolean, graphql_name='isPassed_not')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    reason_not = sgqlc.types.Field(String, graphql_name='reason_not')
    reason_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='reason_in')
    reason_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='reason_not_in')
    reason_contains = sgqlc.types.Field(String, graphql_name='reason_contains')
    reason_not_contains = sgqlc.types.Field(String, graphql_name='reason_not_contains')
    reason_starts_with = sgqlc.types.Field(String, graphql_name='reason_starts_with')
    reason_not_starts_with = sgqlc.types.Field(String, graphql_name='reason_not_starts_with')
    reason_ends_with = sgqlc.types.Field(String, graphql_name='reason_ends_with')
    reason_not_ends_with = sgqlc.types.Field(String, graphql_name='reason_not_ends_with')
    summary = sgqlc.types.Field(String, graphql_name='summary')
    summary_not = sgqlc.types.Field(String, graphql_name='summary_not')
    summary_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='summary_in')
    summary_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='summary_not_in')
    summary_contains = sgqlc.types.Field(String, graphql_name='summary_contains')
    summary_not_contains = sgqlc.types.Field(String, graphql_name='summary_not_contains')
    summary_starts_with = sgqlc.types.Field(String, graphql_name='summary_starts_with')
    summary_not_starts_with = sgqlc.types.Field(String, graphql_name='summary_not_starts_with')
    summary_ends_with = sgqlc.types.Field(String, graphql_name='summary_ends_with')
    summary_not_ends_with = sgqlc.types.Field(String, graphql_name='summary_not_ends_with')
    first_house = sgqlc.types.Field(House, graphql_name='firstHouse')
    first_house_not = sgqlc.types.Field(House, graphql_name='firstHouse_not')
    first_house_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(House)), graphql_name='firstHouse_in')
    first_house_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(House)), graphql_name='firstHouse_not_in')
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
    urls = sgqlc.types.Field('_UrlFilter', graphql_name='urls')
    urls_not = sgqlc.types.Field('_UrlFilter', graphql_name='urls_not')
    urls_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='urls_in')
    urls_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='urls_not_in')
    urls_some = sgqlc.types.Field('_UrlFilter', graphql_name='urls_some')
    urls_none = sgqlc.types.Field('_UrlFilter', graphql_name='urls_none')
    urls_single = sgqlc.types.Field('_UrlFilter', graphql_name='urls_single')
    urls_every = sgqlc.types.Field('_UrlFilter', graphql_name='urls_every')
    news = sgqlc.types.Field('_NewsFilter', graphql_name='news')
    news_not = sgqlc.types.Field('_NewsFilter', graphql_name='news_not')
    news_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_NewsFilter')), graphql_name='news_in')
    news_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_NewsFilter')), graphql_name='news_not_in')
    news_some = sgqlc.types.Field('_NewsFilter', graphql_name='news_some')
    news_none = sgqlc.types.Field('_NewsFilter', graphql_name='news_none')
    news_single = sgqlc.types.Field('_NewsFilter', graphql_name='news_single')
    news_every = sgqlc.types.Field('_NewsFilter', graphql_name='news_every')
    submitted_date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='submittedDate')
    submitted_date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='submittedDate_not')
    submitted_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='submittedDate_in')
    submitted_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='submittedDate_not_in')
    submitted_date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='submittedDate_lt')
    submitted_date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='submittedDate_lte')
    submitted_date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='submittedDate_gt')
    submitted_date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='submittedDate_gte')
    passed_representatives_committee_date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedRepresentativesCommitteeDate')
    passed_representatives_committee_date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedRepresentativesCommitteeDate_not')
    passed_representatives_committee_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedRepresentativesCommitteeDate_in')
    passed_representatives_committee_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedRepresentativesCommitteeDate_not_in')
    passed_representatives_committee_date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedRepresentativesCommitteeDate_lt')
    passed_representatives_committee_date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedRepresentativesCommitteeDate_lte')
    passed_representatives_committee_date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedRepresentativesCommitteeDate_gt')
    passed_representatives_committee_date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedRepresentativesCommitteeDate_gte')
    passed_representatives_date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedRepresentativesDate')
    passed_representatives_date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedRepresentativesDate_not')
    passed_representatives_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedRepresentativesDate_in')
    passed_representatives_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedRepresentativesDate_not_in')
    passed_representatives_date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedRepresentativesDate_lt')
    passed_representatives_date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedRepresentativesDate_lte')
    passed_representatives_date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedRepresentativesDate_gt')
    passed_representatives_date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedRepresentativesDate_gte')
    passed_councilors_committee_date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedCouncilorsCommitteeDate')
    passed_councilors_committee_date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedCouncilorsCommitteeDate_not')
    passed_councilors_committee_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedCouncilorsCommitteeDate_in')
    passed_councilors_committee_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedCouncilorsCommitteeDate_not_in')
    passed_councilors_committee_date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedCouncilorsCommitteeDate_lt')
    passed_councilors_committee_date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedCouncilorsCommitteeDate_lte')
    passed_councilors_committee_date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedCouncilorsCommitteeDate_gt')
    passed_councilors_committee_date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedCouncilorsCommitteeDate_gte')
    passed_councilors_date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedCouncilorsDate')
    passed_councilors_date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedCouncilorsDate_not')
    passed_councilors_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedCouncilorsDate_in')
    passed_councilors_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='passedCouncilorsDate_not_in')
    passed_councilors_date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedCouncilorsDate_lt')
    passed_councilors_date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedCouncilorsDate_lte')
    passed_councilors_date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedCouncilorsDate_gt')
    passed_councilors_date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='passedCouncilorsDate_gte')
    proclaimed_date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='proclaimedDate')
    proclaimed_date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='proclaimedDate_not')
    proclaimed_date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='proclaimedDate_in')
    proclaimed_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='proclaimedDate_not_in')
    proclaimed_date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='proclaimedDate_lt')
    proclaimed_date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='proclaimedDate_lte')
    proclaimed_date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='proclaimedDate_gt')
    proclaimed_date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='proclaimedDate_gte')


class _BillInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _CommitteeFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'num_members', 'num_members_not', 'num_members_in', 'num_members_not_in', 'num_members_lt', 'num_members_lte', 'num_members_gt', 'num_members_gte', 'house', 'house_not', 'house_in', 'house_not_in', 'description', 'description_not', 'description_in', 'description_not_in', 'description_contains', 'description_not_contains', 'description_starts_with', 'description_not_starts_with', 'description_ends_with', 'description_not_ends_with', 'members', 'members_not', 'members_in', 'members_not_in', 'members_some', 'members_none', 'members_single', 'members_every', 'minutes', 'minutes_not', 'minutes_in', 'minutes_not_in', 'minutes_some', 'minutes_none', 'minutes_single', 'minutes_every')
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
    num_members = sgqlc.types.Field(Int, graphql_name='numMembers')
    num_members_not = sgqlc.types.Field(Int, graphql_name='numMembers_not')
    num_members_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='numMembers_in')
    num_members_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='numMembers_not_in')
    num_members_lt = sgqlc.types.Field(Int, graphql_name='numMembers_lt')
    num_members_lte = sgqlc.types.Field(Int, graphql_name='numMembers_lte')
    num_members_gt = sgqlc.types.Field(Int, graphql_name='numMembers_gt')
    num_members_gte = sgqlc.types.Field(Int, graphql_name='numMembers_gte')
    house = sgqlc.types.Field(House, graphql_name='house')
    house_not = sgqlc.types.Field(House, graphql_name='house_not')
    house_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(House)), graphql_name='house_in')
    house_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(House)), graphql_name='house_not_in')
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
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'number', 'number_not', 'number_in', 'number_not_in', 'number_lt', 'number_lte', 'number_gt', 'number_gte', 'category', 'category_not', 'category_in', 'category_not_in', 'start_date', 'start_date_not', 'start_date_in', 'start_date_not_in', 'start_date_lt', 'start_date_lte', 'start_date_gt', 'start_date_gte', 'end_date', 'end_date_not', 'end_date_in', 'end_date_not_in', 'end_date_lt', 'end_date_lte', 'end_date_gt', 'end_date_gte', 'received_bills', 'received_bills_not', 'received_bills_in', 'received_bills_not_in', 'received_bills_some', 'received_bills_none', 'received_bills_single', 'received_bills_every', 'minutes', 'minutes_not', 'minutes_in', 'minutes_not_in', 'minutes_some', 'minutes_none', 'minutes_single', 'minutes_every')
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
    number = sgqlc.types.Field(Int, graphql_name='number')
    number_not = sgqlc.types.Field(Int, graphql_name='number_not')
    number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='number_in')
    number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='number_not_in')
    number_lt = sgqlc.types.Field(Int, graphql_name='number_lt')
    number_lte = sgqlc.types.Field(Int, graphql_name='number_lte')
    number_gt = sgqlc.types.Field(Int, graphql_name='number_gt')
    number_gte = sgqlc.types.Field(Int, graphql_name='number_gte')
    category = sgqlc.types.Field(DietCategory, graphql_name='category')
    category_not = sgqlc.types.Field(DietCategory, graphql_name='category_not')
    category_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DietCategory)), graphql_name='category_in')
    category_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DietCategory)), graphql_name='category_not_in')
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
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'date', 'date_not', 'date_in', 'date_not_in', 'date_lt', 'date_lte', 'date_gt', 'date_gte', 'election_results', 'election_results_not', 'election_results_in', 'election_results_not_in', 'election_results_some', 'election_results_none', 'election_results_single', 'election_results_every')
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
    date = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='date')
    date_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='date_not')
    date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='date_in')
    date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='date_not_in')
    date_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='date_lt')
    date_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='date_lte')
    date_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='date_gt')
    date_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='date_gte')
    election_results = sgqlc.types.Field('_ElectionResultFilter', graphql_name='electionResults')
    election_results_not = sgqlc.types.Field('_ElectionResultFilter', graphql_name='electionResults_not')
    election_results_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_ElectionResultFilter')), graphql_name='electionResults_in')
    election_results_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_ElectionResultFilter')), graphql_name='electionResults_not_in')
    election_results_some = sgqlc.types.Field('_ElectionResultFilter', graphql_name='electionResults_some')
    election_results_none = sgqlc.types.Field('_ElectionResultFilter', graphql_name='electionResults_none')
    election_results_single = sgqlc.types.Field('_ElectionResultFilter', graphql_name='electionResults_single')
    election_results_every = sgqlc.types.Field('_ElectionResultFilter', graphql_name='electionResults_every')


class _ElectionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _ElectionResultFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'system', 'system_not', 'system_in', 'system_not_in', 'district', 'district_not', 'district_in', 'district_not_in', 'district_contains', 'district_not_contains', 'district_starts_with', 'district_not_starts_with', 'district_ends_with', 'district_not_ends_with', 'prefecture', 'prefecture_not', 'prefecture_in', 'prefecture_not_in', 'prefecture_contains', 'prefecture_not_contains', 'prefecture_starts_with', 'prefecture_not_starts_with', 'prefecture_ends_with', 'prefecture_not_ends_with', 'belonged_to_election', 'belonged_to_election_not', 'belonged_to_election_in', 'belonged_to_election_not_in', 'elected_members', 'elected_members_not', 'elected_members_in', 'elected_members_not_in', 'elected_members_some', 'elected_members_none', 'elected_members_single', 'elected_members_every')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_ElectionResultFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_ElectionResultFilter')), graphql_name='OR')
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
    system = sgqlc.types.Field(ElectionSystem, graphql_name='system')
    system_not = sgqlc.types.Field(ElectionSystem, graphql_name='system_not')
    system_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ElectionSystem)), graphql_name='system_in')
    system_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ElectionSystem)), graphql_name='system_not_in')
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
    belonged_to_election = sgqlc.types.Field(_ElectionFilter, graphql_name='belongedToElection')
    belonged_to_election_not = sgqlc.types.Field(_ElectionFilter, graphql_name='belongedToElection_not')
    belonged_to_election_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_ElectionFilter)), graphql_name='belongedToElection_in')
    belonged_to_election_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_ElectionFilter)), graphql_name='belongedToElection_not_in')
    elected_members = sgqlc.types.Field('_MemberFilter', graphql_name='electedMembers')
    elected_members_not = sgqlc.types.Field('_MemberFilter', graphql_name='electedMembers_not')
    elected_members_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MemberFilter')), graphql_name='electedMembers_in')
    elected_members_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MemberFilter')), graphql_name='electedMembers_not_in')
    elected_members_some = sgqlc.types.Field('_MemberFilter', graphql_name='electedMembers_some')
    elected_members_none = sgqlc.types.Field('_MemberFilter', graphql_name='electedMembers_none')
    elected_members_single = sgqlc.types.Field('_MemberFilter', graphql_name='electedMembers_single')
    elected_members_every = sgqlc.types.Field('_MemberFilter', graphql_name='electedMembers_every')


class _ElectionResultInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _LawFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'law_number', 'law_number_not', 'law_number_in', 'law_number_not_in', 'law_number_contains', 'law_number_not_contains', 'law_number_starts_with', 'law_number_not_starts_with', 'law_number_ends_with', 'law_number_not_ends_with', 'summary', 'summary_not', 'summary_in', 'summary_not_in', 'summary_contains', 'summary_not_contains', 'summary_starts_with', 'summary_not_starts_with', 'summary_ends_with', 'summary_not_ends_with', 'be_discussed_by_minutes', 'be_discussed_by_minutes_not', 'be_discussed_by_minutes_in', 'be_discussed_by_minutes_not_in', 'be_discussed_by_minutes_some', 'be_discussed_by_minutes_none', 'be_discussed_by_minutes_single', 'be_discussed_by_minutes_every', 'referred_laws', 'referred_laws_not', 'referred_laws_in', 'referred_laws_not_in', 'referred_laws_some', 'referred_laws_none', 'referred_laws_single', 'referred_laws_every', 'be_referred_by_laws', 'be_referred_by_laws_not', 'be_referred_by_laws_in', 'be_referred_by_laws_not_in', 'be_referred_by_laws_some', 'be_referred_by_laws_none', 'be_referred_by_laws_single', 'be_referred_by_laws_every', 'be_amended_by_bills', 'be_amended_by_bills_not', 'be_amended_by_bills_in', 'be_amended_by_bills_not_in', 'be_amended_by_bills_some', 'be_amended_by_bills_none', 'be_amended_by_bills_single', 'be_amended_by_bills_every', 'urls', 'urls_not', 'urls_in', 'urls_not_in', 'urls_some', 'urls_none', 'urls_single', 'urls_every', 'news', 'news_not', 'news_in', 'news_not_in', 'news_some', 'news_none', 'news_single', 'news_every')
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
    summary = sgqlc.types.Field(String, graphql_name='summary')
    summary_not = sgqlc.types.Field(String, graphql_name='summary_not')
    summary_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='summary_in')
    summary_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='summary_not_in')
    summary_contains = sgqlc.types.Field(String, graphql_name='summary_contains')
    summary_not_contains = sgqlc.types.Field(String, graphql_name='summary_not_contains')
    summary_starts_with = sgqlc.types.Field(String, graphql_name='summary_starts_with')
    summary_not_starts_with = sgqlc.types.Field(String, graphql_name='summary_not_starts_with')
    summary_ends_with = sgqlc.types.Field(String, graphql_name='summary_ends_with')
    summary_not_ends_with = sgqlc.types.Field(String, graphql_name='summary_not_ends_with')
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
    news = sgqlc.types.Field('_NewsFilter', graphql_name='news')
    news_not = sgqlc.types.Field('_NewsFilter', graphql_name='news_not')
    news_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_NewsFilter')), graphql_name='news_in')
    news_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_NewsFilter')), graphql_name='news_not_in')
    news_some = sgqlc.types.Field('_NewsFilter', graphql_name='news_some')
    news_none = sgqlc.types.Field('_NewsFilter', graphql_name='news_none')
    news_single = sgqlc.types.Field('_NewsFilter', graphql_name='news_single')
    news_every = sgqlc.types.Field('_NewsFilter', graphql_name='news_every')


class _LawInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _MemberFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'name_hira', 'name_hira_not', 'name_hira_in', 'name_hira_not_in', 'name_hira_contains', 'name_hira_not_contains', 'name_hira_starts_with', 'name_hira_not_starts_with', 'name_hira_ends_with', 'name_hira_not_ends_with', 'first_name', 'first_name_not', 'first_name_in', 'first_name_not_in', 'first_name_contains', 'first_name_not_contains', 'first_name_starts_with', 'first_name_not_starts_with', 'first_name_ends_with', 'first_name_not_ends_with', 'first_name_hira', 'first_name_hira_not', 'first_name_hira_in', 'first_name_hira_not_in', 'first_name_hira_contains', 'first_name_hira_not_contains', 'first_name_hira_starts_with', 'first_name_hira_not_starts_with', 'first_name_hira_ends_with', 'first_name_hira_not_ends_with', 'last_name', 'last_name_not', 'last_name_in', 'last_name_not_in', 'last_name_contains', 'last_name_not_contains', 'last_name_starts_with', 'last_name_not_starts_with', 'last_name_ends_with', 'last_name_not_ends_with', 'last_name_hira', 'last_name_hira_not', 'last_name_hira_in', 'last_name_hira_not_in', 'last_name_hira_contains', 'last_name_hira_not_contains', 'last_name_hira_starts_with', 'last_name_hira_not_starts_with', 'last_name_hira_ends_with', 'last_name_hira_not_ends_with', 'house', 'house_not', 'house_in', 'house_not_in', 'description', 'description_not', 'description_in', 'description_not_in', 'description_contains', 'description_not_contains', 'description_starts_with', 'description_not_starts_with', 'description_ends_with', 'description_not_ends_with', 'be_elected_by_elections', 'be_elected_by_elections_not', 'be_elected_by_elections_in', 'be_elected_by_elections_not_in', 'be_elected_by_elections_some', 'be_elected_by_elections_none', 'be_elected_by_elections_single', 'be_elected_by_elections_every', 'submitted_bills', 'submitted_bills_not', 'submitted_bills_in', 'submitted_bills_not_in', 'submitted_bills_some', 'submitted_bills_none', 'submitted_bills_single', 'submitted_bills_every', 'attended_diets', 'attended_diets_not', 'attended_diets_in', 'attended_diets_not_in', 'attended_diets_some', 'attended_diets_none', 'attended_diets_single', 'attended_diets_every', 'attended_minutes', 'attended_minutes_not', 'attended_minutes_in', 'attended_minutes_not_in', 'attended_minutes_some', 'attended_minutes_none', 'attended_minutes_single', 'attended_minutes_every', 'delivered_speeches', 'delivered_speeches_not', 'delivered_speeches_in', 'delivered_speeches_not_in', 'delivered_speeches_some', 'delivered_speeches_none', 'delivered_speeches_single', 'delivered_speeches_every', 'urls', 'urls_not', 'urls_in', 'urls_not_in', 'urls_some', 'urls_none', 'urls_single', 'urls_every', 'news', 'news_not', 'news_in', 'news_not_in', 'news_some', 'news_none', 'news_single', 'news_every')
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
    delivered_speeches = sgqlc.types.Field('_SpeechFilter', graphql_name='deliveredSpeeches')
    delivered_speeches_not = sgqlc.types.Field('_SpeechFilter', graphql_name='deliveredSpeeches_not')
    delivered_speeches_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SpeechFilter')), graphql_name='deliveredSpeeches_in')
    delivered_speeches_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SpeechFilter')), graphql_name='deliveredSpeeches_not_in')
    delivered_speeches_some = sgqlc.types.Field('_SpeechFilter', graphql_name='deliveredSpeeches_some')
    delivered_speeches_none = sgqlc.types.Field('_SpeechFilter', graphql_name='deliveredSpeeches_none')
    delivered_speeches_single = sgqlc.types.Field('_SpeechFilter', graphql_name='deliveredSpeeches_single')
    delivered_speeches_every = sgqlc.types.Field('_SpeechFilter', graphql_name='deliveredSpeeches_every')
    urls = sgqlc.types.Field('_UrlFilter', graphql_name='urls')
    urls_not = sgqlc.types.Field('_UrlFilter', graphql_name='urls_not')
    urls_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='urls_in')
    urls_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='urls_not_in')
    urls_some = sgqlc.types.Field('_UrlFilter', graphql_name='urls_some')
    urls_none = sgqlc.types.Field('_UrlFilter', graphql_name='urls_none')
    urls_single = sgqlc.types.Field('_UrlFilter', graphql_name='urls_single')
    urls_every = sgqlc.types.Field('_UrlFilter', graphql_name='urls_every')
    news = sgqlc.types.Field('_NewsFilter', graphql_name='news')
    news_not = sgqlc.types.Field('_NewsFilter', graphql_name='news_not')
    news_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_NewsFilter')), graphql_name='news_in')
    news_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_NewsFilter')), graphql_name='news_not_in')
    news_some = sgqlc.types.Field('_NewsFilter', graphql_name='news_some')
    news_none = sgqlc.types.Field('_NewsFilter', graphql_name='news_none')
    news_single = sgqlc.types.Field('_NewsFilter', graphql_name='news_single')
    news_every = sgqlc.types.Field('_NewsFilter', graphql_name='news_every')


class _MemberInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _MinutesFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'start_date_time', 'start_date_time_not', 'start_date_time_in', 'start_date_time_not_in', 'start_date_time_lt', 'start_date_time_lte', 'start_date_time_gt', 'start_date_time_gte', 'end_date_time', 'end_date_time_not', 'end_date_time_in', 'end_date_time_not_in', 'end_date_time_lt', 'end_date_time_lte', 'end_date_time_gt', 'end_date_time_gte', 'belonged_to_diet', 'belonged_to_diet_not', 'belonged_to_diet_in', 'belonged_to_diet_not_in', 'belonged_to_committee', 'belonged_to_committee_not', 'belonged_to_committee_in', 'belonged_to_committee_not_in', 'be_attended_by_members', 'be_attended_by_members_not', 'be_attended_by_members_in', 'be_attended_by_members_not_in', 'be_attended_by_members_some', 'be_attended_by_members_none', 'be_attended_by_members_single', 'be_attended_by_members_every', 'summary', 'summary_not', 'summary_in', 'summary_not_in', 'summary_contains', 'summary_not_contains', 'summary_starts_with', 'summary_not_starts_with', 'summary_ends_with', 'summary_not_ends_with', 'urls', 'urls_not', 'urls_in', 'urls_not_in', 'urls_some', 'urls_none', 'urls_single', 'urls_every', 'news', 'news_not', 'news_in', 'news_not_in', 'news_some', 'news_none', 'news_single', 'news_every', 'speeches', 'speeches_not', 'speeches_in', 'speeches_not_in', 'speeches_some', 'speeches_none', 'speeches_single', 'speeches_every', 'discussed_bills', 'discussed_bills_not', 'discussed_bills_in', 'discussed_bills_not_in', 'discussed_bills_some', 'discussed_bills_none', 'discussed_bills_single', 'discussed_bills_every', 'discussed_laws', 'discussed_laws_not', 'discussed_laws_in', 'discussed_laws_not_in', 'discussed_laws_some', 'discussed_laws_none', 'discussed_laws_single', 'discussed_laws_every')
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
    summary = sgqlc.types.Field(String, graphql_name='summary')
    summary_not = sgqlc.types.Field(String, graphql_name='summary_not')
    summary_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='summary_in')
    summary_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='summary_not_in')
    summary_contains = sgqlc.types.Field(String, graphql_name='summary_contains')
    summary_not_contains = sgqlc.types.Field(String, graphql_name='summary_not_contains')
    summary_starts_with = sgqlc.types.Field(String, graphql_name='summary_starts_with')
    summary_not_starts_with = sgqlc.types.Field(String, graphql_name='summary_not_starts_with')
    summary_ends_with = sgqlc.types.Field(String, graphql_name='summary_ends_with')
    summary_not_ends_with = sgqlc.types.Field(String, graphql_name='summary_not_ends_with')
    urls = sgqlc.types.Field('_UrlFilter', graphql_name='urls')
    urls_not = sgqlc.types.Field('_UrlFilter', graphql_name='urls_not')
    urls_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='urls_in')
    urls_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='urls_not_in')
    urls_some = sgqlc.types.Field('_UrlFilter', graphql_name='urls_some')
    urls_none = sgqlc.types.Field('_UrlFilter', graphql_name='urls_none')
    urls_single = sgqlc.types.Field('_UrlFilter', graphql_name='urls_single')
    urls_every = sgqlc.types.Field('_UrlFilter', graphql_name='urls_every')
    news = sgqlc.types.Field('_NewsFilter', graphql_name='news')
    news_not = sgqlc.types.Field('_NewsFilter', graphql_name='news_not')
    news_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_NewsFilter')), graphql_name='news_in')
    news_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_NewsFilter')), graphql_name='news_not_in')
    news_some = sgqlc.types.Field('_NewsFilter', graphql_name='news_some')
    news_none = sgqlc.types.Field('_NewsFilter', graphql_name='news_none')
    news_single = sgqlc.types.Field('_NewsFilter', graphql_name='news_single')
    news_every = sgqlc.types.Field('_NewsFilter', graphql_name='news_every')
    speeches = sgqlc.types.Field('_SpeechFilter', graphql_name='speeches')
    speeches_not = sgqlc.types.Field('_SpeechFilter', graphql_name='speeches_not')
    speeches_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SpeechFilter')), graphql_name='speeches_in')
    speeches_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SpeechFilter')), graphql_name='speeches_not_in')
    speeches_some = sgqlc.types.Field('_SpeechFilter', graphql_name='speeches_some')
    speeches_none = sgqlc.types.Field('_SpeechFilter', graphql_name='speeches_none')
    speeches_single = sgqlc.types.Field('_SpeechFilter', graphql_name='speeches_single')
    speeches_every = sgqlc.types.Field('_SpeechFilter', graphql_name='speeches_every')
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


class _NewsFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'url', 'url_not', 'url_in', 'url_not_in', 'url_contains', 'url_not_contains', 'url_starts_with', 'url_not_starts_with', 'url_ends_with', 'url_not_ends_with', 'publisher', 'publisher_not', 'publisher_in', 'publisher_not_in', 'publisher_contains', 'publisher_not_contains', 'publisher_starts_with', 'publisher_not_starts_with', 'publisher_ends_with', 'publisher_not_ends_with', 'thumbnail', 'thumbnail_not', 'thumbnail_in', 'thumbnail_not_in', 'thumbnail_contains', 'thumbnail_not_contains', 'thumbnail_starts_with', 'thumbnail_not_starts_with', 'thumbnail_ends_with', 'thumbnail_not_ends_with', 'title', 'title_not', 'title_in', 'title_not_in', 'title_contains', 'title_not_contains', 'title_starts_with', 'title_not_starts_with', 'title_ends_with', 'title_not_ends_with', 'published_at', 'published_at_not', 'published_at_in', 'published_at_not_in', 'published_at_lt', 'published_at_lte', 'published_at_gt', 'published_at_gte', 'last_modified_at', 'last_modified_at_not', 'last_modified_at_in', 'last_modified_at_not_in', 'last_modified_at_lt', 'last_modified_at_lte', 'last_modified_at_gt', 'last_modified_at_gte', 'is_paid', 'is_paid_not', 'referred_bills', 'referred_bills_not', 'referred_bills_in', 'referred_bills_not_in', 'referred_bills_some', 'referred_bills_none', 'referred_bills_single', 'referred_bills_every', 'referred_laws', 'referred_laws_not', 'referred_laws_in', 'referred_laws_not_in', 'referred_laws_some', 'referred_laws_none', 'referred_laws_single', 'referred_laws_every', 'referred_members', 'referred_members_not', 'referred_members_in', 'referred_members_not_in', 'referred_members_some', 'referred_members_none', 'referred_members_single', 'referred_members_every', 'referred_minutes', 'referred_minutes_not', 'referred_minutes_in', 'referred_minutes_not_in', 'referred_minutes_some', 'referred_minutes_none', 'referred_minutes_single', 'referred_minutes_every')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_NewsFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_NewsFilter')), graphql_name='OR')
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
    publisher = sgqlc.types.Field(String, graphql_name='publisher')
    publisher_not = sgqlc.types.Field(String, graphql_name='publisher_not')
    publisher_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='publisher_in')
    publisher_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='publisher_not_in')
    publisher_contains = sgqlc.types.Field(String, graphql_name='publisher_contains')
    publisher_not_contains = sgqlc.types.Field(String, graphql_name='publisher_not_contains')
    publisher_starts_with = sgqlc.types.Field(String, graphql_name='publisher_starts_with')
    publisher_not_starts_with = sgqlc.types.Field(String, graphql_name='publisher_not_starts_with')
    publisher_ends_with = sgqlc.types.Field(String, graphql_name='publisher_ends_with')
    publisher_not_ends_with = sgqlc.types.Field(String, graphql_name='publisher_not_ends_with')
    thumbnail = sgqlc.types.Field(String, graphql_name='thumbnail')
    thumbnail_not = sgqlc.types.Field(String, graphql_name='thumbnail_not')
    thumbnail_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='thumbnail_in')
    thumbnail_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='thumbnail_not_in')
    thumbnail_contains = sgqlc.types.Field(String, graphql_name='thumbnail_contains')
    thumbnail_not_contains = sgqlc.types.Field(String, graphql_name='thumbnail_not_contains')
    thumbnail_starts_with = sgqlc.types.Field(String, graphql_name='thumbnail_starts_with')
    thumbnail_not_starts_with = sgqlc.types.Field(String, graphql_name='thumbnail_not_starts_with')
    thumbnail_ends_with = sgqlc.types.Field(String, graphql_name='thumbnail_ends_with')
    thumbnail_not_ends_with = sgqlc.types.Field(String, graphql_name='thumbnail_not_ends_with')
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
    published_at = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='publishedAt')
    published_at_not = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='publishedAt_not')
    published_at_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='publishedAt_in')
    published_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='publishedAt_not_in')
    published_at_lt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='publishedAt_lt')
    published_at_lte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='publishedAt_lte')
    published_at_gt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='publishedAt_gt')
    published_at_gte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='publishedAt_gte')
    last_modified_at = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='lastModifiedAt')
    last_modified_at_not = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='lastModifiedAt_not')
    last_modified_at_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='lastModifiedAt_in')
    last_modified_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='lastModifiedAt_not_in')
    last_modified_at_lt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='lastModifiedAt_lt')
    last_modified_at_lte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='lastModifiedAt_lte')
    last_modified_at_gt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='lastModifiedAt_gt')
    last_modified_at_gte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='lastModifiedAt_gte')
    is_paid = sgqlc.types.Field(Boolean, graphql_name='isPaid')
    is_paid_not = sgqlc.types.Field(Boolean, graphql_name='isPaid_not')
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
    referred_minutes = sgqlc.types.Field(_MinutesFilter, graphql_name='referredMinutes')
    referred_minutes_not = sgqlc.types.Field(_MinutesFilter, graphql_name='referredMinutes_not')
    referred_minutes_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MinutesFilter)), graphql_name='referredMinutes_in')
    referred_minutes_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MinutesFilter)), graphql_name='referredMinutes_not_in')
    referred_minutes_some = sgqlc.types.Field(_MinutesFilter, graphql_name='referredMinutes_some')
    referred_minutes_none = sgqlc.types.Field(_MinutesFilter, graphql_name='referredMinutes_none')
    referred_minutes_single = sgqlc.types.Field(_MinutesFilter, graphql_name='referredMinutes_single')
    referred_minutes_every = sgqlc.types.Field(_MinutesFilter, graphql_name='referredMinutes_every')


class _NewsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _SpeechFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'speaker_name', 'speaker_name_not', 'speaker_name_in', 'speaker_name_not_in', 'speaker_name_contains', 'speaker_name_not_contains', 'speaker_name_starts_with', 'speaker_name_not_starts_with', 'speaker_name_ends_with', 'speaker_name_not_ends_with', 'order_in_minutes', 'order_in_minutes_not', 'order_in_minutes_in', 'order_in_minutes_not_in', 'order_in_minutes_lt', 'order_in_minutes_lte', 'order_in_minutes_gt', 'order_in_minutes_gte', 'belonged_to_minutes', 'belonged_to_minutes_not', 'belonged_to_minutes_in', 'belonged_to_minutes_not_in', 'be_delivered_by_member', 'be_delivered_by_member_not', 'be_delivered_by_member_in', 'be_delivered_by_member_not_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SpeechFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SpeechFilter')), graphql_name='OR')
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
    speaker_name = sgqlc.types.Field(String, graphql_name='speakerName')
    speaker_name_not = sgqlc.types.Field(String, graphql_name='speakerName_not')
    speaker_name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='speakerName_in')
    speaker_name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='speakerName_not_in')
    speaker_name_contains = sgqlc.types.Field(String, graphql_name='speakerName_contains')
    speaker_name_not_contains = sgqlc.types.Field(String, graphql_name='speakerName_not_contains')
    speaker_name_starts_with = sgqlc.types.Field(String, graphql_name='speakerName_starts_with')
    speaker_name_not_starts_with = sgqlc.types.Field(String, graphql_name='speakerName_not_starts_with')
    speaker_name_ends_with = sgqlc.types.Field(String, graphql_name='speakerName_ends_with')
    speaker_name_not_ends_with = sgqlc.types.Field(String, graphql_name='speakerName_not_ends_with')
    order_in_minutes = sgqlc.types.Field(Int, graphql_name='orderInMinutes')
    order_in_minutes_not = sgqlc.types.Field(Int, graphql_name='orderInMinutes_not')
    order_in_minutes_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='orderInMinutes_in')
    order_in_minutes_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='orderInMinutes_not_in')
    order_in_minutes_lt = sgqlc.types.Field(Int, graphql_name='orderInMinutes_lt')
    order_in_minutes_lte = sgqlc.types.Field(Int, graphql_name='orderInMinutes_lte')
    order_in_minutes_gt = sgqlc.types.Field(Int, graphql_name='orderInMinutes_gt')
    order_in_minutes_gte = sgqlc.types.Field(Int, graphql_name='orderInMinutes_gte')
    belonged_to_minutes = sgqlc.types.Field(_MinutesFilter, graphql_name='belongedToMinutes')
    belonged_to_minutes_not = sgqlc.types.Field(_MinutesFilter, graphql_name='belongedToMinutes_not')
    belonged_to_minutes_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MinutesFilter)), graphql_name='belongedToMinutes_in')
    belonged_to_minutes_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MinutesFilter)), graphql_name='belongedToMinutes_not_in')
    be_delivered_by_member = sgqlc.types.Field(_MemberFilter, graphql_name='beDeliveredByMember')
    be_delivered_by_member_not = sgqlc.types.Field(_MemberFilter, graphql_name='beDeliveredByMember_not')
    be_delivered_by_member_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MemberFilter)), graphql_name='beDeliveredByMember_in')
    be_delivered_by_member_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MemberFilter)), graphql_name='beDeliveredByMember_not_in')


class _SpeechInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _TimelineFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'date', 'date_not', 'date_in', 'date_not_in', 'date_lt', 'date_lte', 'date_gt', 'date_gte', 'bills', 'bills_not', 'bills_in', 'bills_not_in', 'bills_some', 'bills_none', 'bills_single', 'bills_every', 'minutes', 'minutes_not', 'minutes_in', 'minutes_not_in', 'minutes_some', 'minutes_none', 'minutes_single', 'minutes_every', 'news', 'news_not', 'news_in', 'news_not_in', 'news_some', 'news_none', 'news_single', 'news_every')
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
    date = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='date')
    date_not = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='date_not')
    date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='date_in')
    date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='date_not_in')
    date_lt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='date_lt')
    date_lte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='date_lte')
    date_gt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='date_gt')
    date_gte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='date_gte')
    bills = sgqlc.types.Field(_BillFilter, graphql_name='bills')
    bills_not = sgqlc.types.Field(_BillFilter, graphql_name='bills_not')
    bills_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='bills_in')
    bills_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='bills_not_in')
    bills_some = sgqlc.types.Field(_BillFilter, graphql_name='bills_some')
    bills_none = sgqlc.types.Field(_BillFilter, graphql_name='bills_none')
    bills_single = sgqlc.types.Field(_BillFilter, graphql_name='bills_single')
    bills_every = sgqlc.types.Field(_BillFilter, graphql_name='bills_every')
    minutes = sgqlc.types.Field(_MinutesFilter, graphql_name='minutes')
    minutes_not = sgqlc.types.Field(_MinutesFilter, graphql_name='minutes_not')
    minutes_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MinutesFilter)), graphql_name='minutes_in')
    minutes_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MinutesFilter)), graphql_name='minutes_not_in')
    minutes_some = sgqlc.types.Field(_MinutesFilter, graphql_name='minutes_some')
    minutes_none = sgqlc.types.Field(_MinutesFilter, graphql_name='minutes_none')
    minutes_single = sgqlc.types.Field(_MinutesFilter, graphql_name='minutes_single')
    minutes_every = sgqlc.types.Field(_MinutesFilter, graphql_name='minutes_every')
    news = sgqlc.types.Field(_NewsFilter, graphql_name='news')
    news_not = sgqlc.types.Field(_NewsFilter, graphql_name='news_not')
    news_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_NewsFilter)), graphql_name='news_in')
    news_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_NewsFilter)), graphql_name='news_not_in')
    news_some = sgqlc.types.Field(_NewsFilter, graphql_name='news_some')
    news_none = sgqlc.types.Field(_NewsFilter, graphql_name='news_none')
    news_single = sgqlc.types.Field(_NewsFilter, graphql_name='news_single')
    news_every = sgqlc.types.Field(_NewsFilter, graphql_name='news_every')


class _TimelineInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _UrlFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'url', 'url_not', 'url_in', 'url_not_in', 'url_contains', 'url_not_contains', 'url_starts_with', 'url_not_starts_with', 'url_ends_with', 'url_not_ends_with', 'domain', 'domain_not', 'domain_in', 'domain_not_in', 'domain_contains', 'domain_not_contains', 'domain_starts_with', 'domain_not_starts_with', 'domain_ends_with', 'domain_not_ends_with', 'title', 'title_not', 'title_in', 'title_not_in', 'title_contains', 'title_not_contains', 'title_starts_with', 'title_not_starts_with', 'title_ends_with', 'title_not_ends_with', 'description', 'description_not', 'description_in', 'description_not_in', 'description_contains', 'description_not_contains', 'description_starts_with', 'description_not_starts_with', 'description_ends_with', 'description_not_ends_with', 'referred_bills', 'referred_bills_not', 'referred_bills_in', 'referred_bills_not_in', 'referred_bills_some', 'referred_bills_none', 'referred_bills_single', 'referred_bills_every', 'referred_laws', 'referred_laws_not', 'referred_laws_in', 'referred_laws_not_in', 'referred_laws_some', 'referred_laws_none', 'referred_laws_single', 'referred_laws_every', 'referred_members', 'referred_members_not', 'referred_members_in', 'referred_members_not_in', 'referred_members_some', 'referred_members_none', 'referred_members_single', 'referred_members_every', 'referred_minutes', 'referred_minutes_not', 'referred_minutes_in', 'referred_minutes_not_in', 'referred_minutes_some', 'referred_minutes_none', 'referred_minutes_single', 'referred_minutes_every')
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
    referred_minutes = sgqlc.types.Field(_MinutesFilter, graphql_name='referredMinutes')
    referred_minutes_not = sgqlc.types.Field(_MinutesFilter, graphql_name='referredMinutes_not')
    referred_minutes_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MinutesFilter)), graphql_name='referredMinutes_in')
    referred_minutes_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MinutesFilter)), graphql_name='referredMinutes_not_in')
    referred_minutes_some = sgqlc.types.Field(_MinutesFilter, graphql_name='referredMinutes_some')
    referred_minutes_none = sgqlc.types.Field(_MinutesFilter, graphql_name='referredMinutes_none')
    referred_minutes_single = sgqlc.types.Field(_MinutesFilter, graphql_name='referredMinutes_single')
    referred_minutes_every = sgqlc.types.Field(_MinutesFilter, graphql_name='referredMinutes_every')


class _UrlInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')



########################################################################
# Output Objects and Interfaces
########################################################################
class Bill(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'bill_number', 'category', 'is_amendment', 'is_passed', 'reason', 'summary', 'aliases', 'tags', 'first_house', 'be_submitted_by_members', 'be_received_by_diet', 'be_discussed_by_minutes', 'amended_laws', 'urls', 'news', 'submitted_date', 'passed_representatives_committee_date', 'passed_representatives_date', 'passed_councilors_committee_date', 'passed_councilors_date', 'proclaimed_date', 'total_news', 'total_minutes', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    bill_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='billNumber')
    category = sgqlc.types.Field(BillCategory, graphql_name='category')
    is_amendment = sgqlc.types.Field(Boolean, graphql_name='isAmendment')
    is_passed = sgqlc.types.Field(Boolean, graphql_name='isPassed')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    summary = sgqlc.types.Field(String, graphql_name='summary')
    aliases = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='aliases')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    first_house = sgqlc.types.Field(House, graphql_name='firstHouse')
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
    urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Url'))), graphql_name='urls', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UrlOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UrlFilter, graphql_name='filter', default=None)),
))
    )
    news = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('News'))), graphql_name='news', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_NewsOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_NewsFilter, graphql_name='filter', default=None)),
))
    )
    submitted_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='submittedDate')
    passed_representatives_committee_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='passedRepresentativesCommitteeDate')
    passed_representatives_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='passedRepresentativesDate')
    passed_councilors_committee_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='passedCouncilorsCommitteeDate')
    passed_councilors_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='passedCouncilorsDate')
    proclaimed_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='proclaimedDate')
    total_news = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalNews')
    total_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalMinutes')
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Committee(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'topics', 'num_members', 'house', 'description', 'aliases', 'tags', 'members', 'minutes', 'total_minutes', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    topics = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='topics')
    num_members = sgqlc.types.Field(Int, graphql_name='numMembers')
    house = sgqlc.types.Field(House, graphql_name='house')
    description = sgqlc.types.Field(String, graphql_name='description')
    aliases = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='aliases')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
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
    total_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalMinutes')
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Diet(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'number', 'category', 'start_date', 'end_date', 'received_bills', 'minutes', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    number = sgqlc.types.Field(Int, graphql_name='number')
    category = sgqlc.types.Field(DietCategory, graphql_name='category')
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
    __field_names__ = ('id', 'name', 'date', 'election_results', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='date')
    election_results = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ElectionResult'))), graphql_name='electionResults', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_ElectionResultOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_ElectionResultFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class ElectionResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'system', 'district', 'prefecture', 'belonged_to_election', 'elected_members', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    system = sgqlc.types.Field(ElectionSystem, graphql_name='system')
    district = sgqlc.types.Field(String, graphql_name='district')
    prefecture = sgqlc.types.Field(String, graphql_name='prefecture')
    belonged_to_election = sgqlc.types.Field(Election, graphql_name='belongedToElection', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_ElectionFilter, graphql_name='filter', default=None)),
))
    )
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
    __field_names__ = ('id', 'name', 'law_number', 'summary', 'tags', 'be_discussed_by_minutes', 'referred_laws', 'be_referred_by_laws', 'be_amended_by_bills', 'urls', 'news', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    law_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lawNumber')
    summary = sgqlc.types.Field(String, graphql_name='summary')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
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
    news = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('News'))), graphql_name='news', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_NewsOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_NewsFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Member(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'name_hira', 'first_name', 'first_name_hira', 'last_name', 'last_name_hira', 'house', 'description', 'tags', 'be_elected_by_elections', 'submitted_bills', 'attended_diets', 'attended_minutes', 'delivered_speeches', 'urls', 'news', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_hira = sgqlc.types.Field(String, graphql_name='nameHira')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    first_name_hira = sgqlc.types.Field(String, graphql_name='firstNameHira')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    last_name_hira = sgqlc.types.Field(String, graphql_name='lastNameHira')
    house = sgqlc.types.Field(House, graphql_name='house')
    description = sgqlc.types.Field(String, graphql_name='description')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
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
    delivered_speeches = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Speech'))), graphql_name='deliveredSpeeches', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_SpeechOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_SpeechFilter, graphql_name='filter', default=None)),
))
    )
    urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Url'))), graphql_name='urls', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UrlOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UrlFilter, graphql_name='filter', default=None)),
))
    )
    news = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('News'))), graphql_name='news', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_NewsOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_NewsFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Minutes(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'start_date_time', 'end_date_time', 'belonged_to_diet', 'belonged_to_committee', 'be_attended_by_members', 'topics', 'summary', 'tags', 'urls', 'news', 'speeches', 'discussed_bills', 'discussed_laws', 'total_news', 'total_bills', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
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
    topics = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='topics')
    summary = sgqlc.types.Field(String, graphql_name='summary')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Url'))), graphql_name='urls', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UrlOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UrlFilter, graphql_name='filter', default=None)),
))
    )
    news = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('News'))), graphql_name='news', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_NewsOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_NewsFilter, graphql_name='filter', default=None)),
))
    )
    speeches = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Speech'))), graphql_name='speeches', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_SpeechOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_SpeechFilter, graphql_name='filter', default=None)),
))
    )
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
    total_news = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalNews')
    total_bills = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalBills')
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Mutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('delete_all_members', 'delete_all_elections', 'delete_all_election_results', 'delete_all_diets', 'delete_all_laws', 'delete_all_bills', 'delete_all_committees', 'delete_all_minutes', 'delete_all_speeches', 'delete_all_urls', 'delete_all_news', 'delete_all_timelines', 'delete_all_news_reference', 'add_member_be_elected_by_elections', 'remove_member_be_elected_by_elections', 'merge_member_be_elected_by_elections', 'add_member_submitted_bills', 'remove_member_submitted_bills', 'merge_member_submitted_bills', 'add_member_attended_diets', 'remove_member_attended_diets', 'merge_member_attended_diets', 'add_member_attended_minutes', 'remove_member_attended_minutes', 'merge_member_attended_minutes', 'add_member_delivered_speeches', 'remove_member_delivered_speeches', 'merge_member_delivered_speeches', 'add_member_urls', 'remove_member_urls', 'merge_member_urls', 'add_member_news', 'remove_member_news', 'merge_member_news', 'create_member', 'update_member', 'delete_member', 'merge_member', 'add_election_election_results', 'remove_election_election_results', 'merge_election_election_results', 'create_election', 'update_election', 'delete_election', 'merge_election', 'add_election_result_belonged_to_election', 'remove_election_result_belonged_to_election', 'merge_election_result_belonged_to_election', 'add_election_result_elected_members', 'remove_election_result_elected_members', 'merge_election_result_elected_members', 'create_election_result', 'update_election_result', 'delete_election_result', 'merge_election_result', 'add_diet_received_bills', 'remove_diet_received_bills', 'merge_diet_received_bills', 'add_diet_minutes', 'remove_diet_minutes', 'merge_diet_minutes', 'create_diet', 'update_diet', 'delete_diet', 'merge_diet', 'add_law_be_discussed_by_minutes', 'remove_law_be_discussed_by_minutes', 'merge_law_be_discussed_by_minutes', 'add_law_referred_laws', 'remove_law_referred_laws', 'merge_law_referred_laws', 'add_law_be_referred_by_laws', 'remove_law_be_referred_by_laws', 'merge_law_be_referred_by_laws', 'add_law_be_amended_by_bills', 'remove_law_be_amended_by_bills', 'merge_law_be_amended_by_bills', 'add_law_urls', 'remove_law_urls', 'merge_law_urls', 'add_law_news', 'remove_law_news', 'merge_law_news', 'create_law', 'update_law', 'delete_law', 'merge_law', 'add_bill_be_submitted_by_members', 'remove_bill_be_submitted_by_members', 'merge_bill_be_submitted_by_members', 'add_bill_be_received_by_diet', 'remove_bill_be_received_by_diet', 'merge_bill_be_received_by_diet', 'add_bill_be_discussed_by_minutes', 'remove_bill_be_discussed_by_minutes', 'merge_bill_be_discussed_by_minutes', 'add_bill_amended_laws', 'remove_bill_amended_laws', 'merge_bill_amended_laws', 'add_bill_urls', 'remove_bill_urls', 'merge_bill_urls', 'add_bill_news', 'remove_bill_news', 'merge_bill_news', 'create_bill', 'update_bill', 'delete_bill', 'merge_bill', 'add_committee_members', 'remove_committee_members', 'merge_committee_members', 'add_committee_minutes', 'remove_committee_minutes', 'merge_committee_minutes', 'create_committee', 'update_committee', 'delete_committee', 'merge_committee', 'add_minutes_belonged_to_diet', 'remove_minutes_belonged_to_diet', 'merge_minutes_belonged_to_diet', 'add_minutes_belonged_to_committee', 'remove_minutes_belonged_to_committee', 'merge_minutes_belonged_to_committee', 'add_minutes_be_attended_by_members', 'remove_minutes_be_attended_by_members', 'merge_minutes_be_attended_by_members', 'add_minutes_urls', 'remove_minutes_urls', 'merge_minutes_urls', 'add_minutes_news', 'remove_minutes_news', 'merge_minutes_news', 'add_minutes_speeches', 'remove_minutes_speeches', 'merge_minutes_speeches', 'add_minutes_discussed_bills', 'remove_minutes_discussed_bills', 'merge_minutes_discussed_bills', 'add_minutes_discussed_laws', 'remove_minutes_discussed_laws', 'merge_minutes_discussed_laws', 'create_minutes', 'update_minutes', 'delete_minutes', 'merge_minutes', 'add_speech_belonged_to_minutes', 'remove_speech_belonged_to_minutes', 'merge_speech_belonged_to_minutes', 'add_speech_be_delivered_by_member', 'remove_speech_be_delivered_by_member', 'merge_speech_be_delivered_by_member', 'create_speech', 'update_speech', 'delete_speech', 'merge_speech', 'add_url_referred_bills', 'remove_url_referred_bills', 'merge_url_referred_bills', 'add_url_referred_laws', 'remove_url_referred_laws', 'merge_url_referred_laws', 'add_url_referred_members', 'remove_url_referred_members', 'merge_url_referred_members', 'add_url_referred_minutes', 'remove_url_referred_minutes', 'merge_url_referred_minutes', 'create_url', 'update_url', 'delete_url', 'merge_url', 'add_news_referred_bills', 'remove_news_referred_bills', 'merge_news_referred_bills', 'add_news_referred_laws', 'remove_news_referred_laws', 'merge_news_referred_laws', 'add_news_referred_members', 'remove_news_referred_members', 'merge_news_referred_members', 'add_news_referred_minutes', 'remove_news_referred_minutes', 'merge_news_referred_minutes', 'create_news', 'update_news', 'delete_news', 'merge_news', 'add_timeline_bills', 'remove_timeline_bills', 'merge_timeline_bills', 'add_timeline_minutes', 'remove_timeline_minutes', 'merge_timeline_minutes', 'add_timeline_news', 'remove_timeline_news', 'merge_timeline_news', 'create_timeline', 'update_timeline', 'delete_timeline', 'merge_timeline')
    delete_all_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='DeleteAllMembers')
    delete_all_elections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='DeleteAllElections')
    delete_all_election_results = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='DeleteAllElectionResults')
    delete_all_diets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='DeleteAllDiets')
    delete_all_laws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='DeleteAllLaws')
    delete_all_bills = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='DeleteAllBills')
    delete_all_committees = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='DeleteAllCommittees')
    delete_all_minutes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='DeleteAllMinutes')
    delete_all_speeches = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='DeleteAllSpeeches')
    delete_all_urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='DeleteAllUrls')
    delete_all_news = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='DeleteAllNews')
    delete_all_timelines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='DeleteAllTimelines')
    delete_all_news_reference = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='DeleteAllNewsReference')
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
    add_member_delivered_speeches = sgqlc.types.Field('_AddMemberDeliveredSpeechesPayload', graphql_name='AddMemberDeliveredSpeeches', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SpeechInput), graphql_name='to', default=None)),
))
    )
    remove_member_delivered_speeches = sgqlc.types.Field('_RemoveMemberDeliveredSpeechesPayload', graphql_name='RemoveMemberDeliveredSpeeches', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SpeechInput), graphql_name='to', default=None)),
))
    )
    merge_member_delivered_speeches = sgqlc.types.Field('_MergeMemberDeliveredSpeechesPayload', graphql_name='MergeMemberDeliveredSpeeches', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SpeechInput), graphql_name='to', default=None)),
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
    add_member_news = sgqlc.types.Field('_AddMemberNewsPayload', graphql_name='AddMemberNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    remove_member_news = sgqlc.types.Field('_RemoveMemberNewsPayload', graphql_name='RemoveMemberNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    merge_member_news = sgqlc.types.Field('_MergeMemberNewsPayload', graphql_name='MergeMemberNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
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
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags', default=None)),
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
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
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
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
))
    )
    add_election_election_results = sgqlc.types.Field('_AddElectionElectionResultsPayload', graphql_name='AddElectionElectionResults', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionResultInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionInput), graphql_name='to', default=None)),
))
    )
    remove_election_election_results = sgqlc.types.Field('_RemoveElectionElectionResultsPayload', graphql_name='RemoveElectionElectionResults', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionResultInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionInput), graphql_name='to', default=None)),
))
    )
    merge_election_election_results = sgqlc.types.Field('_MergeElectionElectionResultsPayload', graphql_name='MergeElectionElectionResults', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionResultInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionInput), graphql_name='to', default=None)),
))
    )
    create_election = sgqlc.types.Field(Election, graphql_name='CreateElection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='date', default=None)),
))
    )
    update_election = sgqlc.types.Field(Election, graphql_name='UpdateElection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='date', default=None)),
))
    )
    delete_election = sgqlc.types.Field(Election, graphql_name='DeleteElection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_election = sgqlc.types.Field(Election, graphql_name='MergeElection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='date', default=None)),
))
    )
    add_election_result_belonged_to_election = sgqlc.types.Field('_AddElectionResultBelongedToElectionPayload', graphql_name='AddElectionResultBelongedToElection', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionResultInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionInput), graphql_name='to', default=None)),
))
    )
    remove_election_result_belonged_to_election = sgqlc.types.Field('_RemoveElectionResultBelongedToElectionPayload', graphql_name='RemoveElectionResultBelongedToElection', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionResultInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionInput), graphql_name='to', default=None)),
))
    )
    merge_election_result_belonged_to_election = sgqlc.types.Field('_MergeElectionResultBelongedToElectionPayload', graphql_name='MergeElectionResultBelongedToElection', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionResultInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionInput), graphql_name='to', default=None)),
))
    )
    add_election_result_elected_members = sgqlc.types.Field('_AddElectionResultElectedMembersPayload', graphql_name='AddElectionResultElectedMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionResultInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    remove_election_result_elected_members = sgqlc.types.Field('_RemoveElectionResultElectedMembersPayload', graphql_name='RemoveElectionResultElectedMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionResultInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    merge_election_result_elected_members = sgqlc.types.Field('_MergeElectionResultElectedMembersPayload', graphql_name='MergeElectionResultElectedMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionResultInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    create_election_result = sgqlc.types.Field(ElectionResult, graphql_name='CreateElectionResult', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('system', sgqlc.types.Arg(ElectionSystem, graphql_name='system', default=None)),
        ('district', sgqlc.types.Arg(String, graphql_name='district', default=None)),
        ('prefecture', sgqlc.types.Arg(String, graphql_name='prefecture', default=None)),
))
    )
    update_election_result = sgqlc.types.Field(ElectionResult, graphql_name='UpdateElectionResult', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('system', sgqlc.types.Arg(ElectionSystem, graphql_name='system', default=None)),
        ('district', sgqlc.types.Arg(String, graphql_name='district', default=None)),
        ('prefecture', sgqlc.types.Arg(String, graphql_name='prefecture', default=None)),
))
    )
    delete_election_result = sgqlc.types.Field(ElectionResult, graphql_name='DeleteElectionResult', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_election_result = sgqlc.types.Field(ElectionResult, graphql_name='MergeElectionResult', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('system', sgqlc.types.Arg(ElectionSystem, graphql_name='system', default=None)),
        ('district', sgqlc.types.Arg(String, graphql_name='district', default=None)),
        ('prefecture', sgqlc.types.Arg(String, graphql_name='prefecture', default=None)),
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
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('number', sgqlc.types.Arg(Int, graphql_name='number', default=None)),
        ('category', sgqlc.types.Arg(DietCategory, graphql_name='category', default=None)),
        ('start_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startDate', default=None)),
        ('end_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='endDate', default=None)),
))
    )
    update_diet = sgqlc.types.Field(Diet, graphql_name='UpdateDiet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('number', sgqlc.types.Arg(Int, graphql_name='number', default=None)),
        ('category', sgqlc.types.Arg(DietCategory, graphql_name='category', default=None)),
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
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('number', sgqlc.types.Arg(Int, graphql_name='number', default=None)),
        ('category', sgqlc.types.Arg(DietCategory, graphql_name='category', default=None)),
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
    add_law_news = sgqlc.types.Field('_AddLawNewsPayload', graphql_name='AddLawNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    remove_law_news = sgqlc.types.Field('_RemoveLawNewsPayload', graphql_name='RemoveLawNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    merge_law_news = sgqlc.types.Field('_MergeLawNewsPayload', graphql_name='MergeLawNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    create_law = sgqlc.types.Field(Law, graphql_name='CreateLaw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('law_number', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='lawNumber', default=None)),
        ('summary', sgqlc.types.Arg(String, graphql_name='summary', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags', default=None)),
))
    )
    update_law = sgqlc.types.Field(Law, graphql_name='UpdateLaw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('law_number', sgqlc.types.Arg(String, graphql_name='lawNumber', default=None)),
        ('summary', sgqlc.types.Arg(String, graphql_name='summary', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
))
    )
    delete_law = sgqlc.types.Field(Law, graphql_name='DeleteLaw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_law = sgqlc.types.Field(Law, graphql_name='MergeLaw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('law_number', sgqlc.types.Arg(String, graphql_name='lawNumber', default=None)),
        ('summary', sgqlc.types.Arg(String, graphql_name='summary', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
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
    add_bill_news = sgqlc.types.Field('_AddBillNewsPayload', graphql_name='AddBillNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_bill_news = sgqlc.types.Field('_RemoveBillNewsPayload', graphql_name='RemoveBillNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_bill_news = sgqlc.types.Field('_MergeBillNewsPayload', graphql_name='MergeBillNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    create_bill = sgqlc.types.Field(Bill, graphql_name='CreateBill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('bill_number', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='billNumber', default=None)),
        ('category', sgqlc.types.Arg(BillCategory, graphql_name='category', default=None)),
        ('is_amendment', sgqlc.types.Arg(Boolean, graphql_name='isAmendment', default=None)),
        ('is_passed', sgqlc.types.Arg(Boolean, graphql_name='isPassed', default=None)),
        ('reason', sgqlc.types.Arg(String, graphql_name='reason', default=None)),
        ('summary', sgqlc.types.Arg(String, graphql_name='summary', default=None)),
        ('aliases', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='aliases', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags', default=None)),
        ('first_house', sgqlc.types.Arg(House, graphql_name='firstHouse', default=None)),
        ('submitted_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='submittedDate', default=None)),
        ('passed_representatives_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedRepresentativesCommitteeDate', default=None)),
        ('passed_representatives_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedRepresentativesDate', default=None)),
        ('passed_councilors_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedCouncilorsCommitteeDate', default=None)),
        ('passed_councilors_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedCouncilorsDate', default=None)),
        ('proclaimed_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='proclaimedDate', default=None)),
))
    )
    update_bill = sgqlc.types.Field(Bill, graphql_name='UpdateBill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('bill_number', sgqlc.types.Arg(String, graphql_name='billNumber', default=None)),
        ('category', sgqlc.types.Arg(BillCategory, graphql_name='category', default=None)),
        ('is_amendment', sgqlc.types.Arg(Boolean, graphql_name='isAmendment', default=None)),
        ('is_passed', sgqlc.types.Arg(Boolean, graphql_name='isPassed', default=None)),
        ('reason', sgqlc.types.Arg(String, graphql_name='reason', default=None)),
        ('summary', sgqlc.types.Arg(String, graphql_name='summary', default=None)),
        ('aliases', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='aliases', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
        ('first_house', sgqlc.types.Arg(House, graphql_name='firstHouse', default=None)),
        ('submitted_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='submittedDate', default=None)),
        ('passed_representatives_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedRepresentativesCommitteeDate', default=None)),
        ('passed_representatives_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedRepresentativesDate', default=None)),
        ('passed_councilors_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedCouncilorsCommitteeDate', default=None)),
        ('passed_councilors_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedCouncilorsDate', default=None)),
        ('proclaimed_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='proclaimedDate', default=None)),
))
    )
    delete_bill = sgqlc.types.Field(Bill, graphql_name='DeleteBill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_bill = sgqlc.types.Field(Bill, graphql_name='MergeBill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('bill_number', sgqlc.types.Arg(String, graphql_name='billNumber', default=None)),
        ('category', sgqlc.types.Arg(BillCategory, graphql_name='category', default=None)),
        ('is_amendment', sgqlc.types.Arg(Boolean, graphql_name='isAmendment', default=None)),
        ('is_passed', sgqlc.types.Arg(Boolean, graphql_name='isPassed', default=None)),
        ('reason', sgqlc.types.Arg(String, graphql_name='reason', default=None)),
        ('summary', sgqlc.types.Arg(String, graphql_name='summary', default=None)),
        ('aliases', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='aliases', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
        ('first_house', sgqlc.types.Arg(House, graphql_name='firstHouse', default=None)),
        ('submitted_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='submittedDate', default=None)),
        ('passed_representatives_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedRepresentativesCommitteeDate', default=None)),
        ('passed_representatives_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedRepresentativesDate', default=None)),
        ('passed_councilors_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedCouncilorsCommitteeDate', default=None)),
        ('passed_councilors_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedCouncilorsDate', default=None)),
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
        ('topics', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='topics', default=None)),
        ('num_members', sgqlc.types.Arg(Int, graphql_name='numMembers', default=None)),
        ('house', sgqlc.types.Arg(House, graphql_name='house', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('aliases', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='aliases', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags', default=None)),
))
    )
    update_committee = sgqlc.types.Field(Committee, graphql_name='UpdateCommittee', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('topics', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='topics', default=None)),
        ('num_members', sgqlc.types.Arg(Int, graphql_name='numMembers', default=None)),
        ('house', sgqlc.types.Arg(House, graphql_name='house', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('aliases', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='aliases', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
))
    )
    delete_committee = sgqlc.types.Field(Committee, graphql_name='DeleteCommittee', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_committee = sgqlc.types.Field(Committee, graphql_name='MergeCommittee', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('topics', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='topics', default=None)),
        ('num_members', sgqlc.types.Arg(Int, graphql_name='numMembers', default=None)),
        ('house', sgqlc.types.Arg(House, graphql_name='house', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('aliases', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='aliases', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
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
    add_minutes_urls = sgqlc.types.Field('_AddMinutesUrlsPayload', graphql_name='AddMinutesUrls', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    remove_minutes_urls = sgqlc.types.Field('_RemoveMinutesUrlsPayload', graphql_name='RemoveMinutesUrls', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    merge_minutes_urls = sgqlc.types.Field('_MergeMinutesUrlsPayload', graphql_name='MergeMinutesUrls', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    add_minutes_news = sgqlc.types.Field('_AddMinutesNewsPayload', graphql_name='AddMinutesNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    remove_minutes_news = sgqlc.types.Field('_RemoveMinutesNewsPayload', graphql_name='RemoveMinutesNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    merge_minutes_news = sgqlc.types.Field('_MergeMinutesNewsPayload', graphql_name='MergeMinutesNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    add_minutes_speeches = sgqlc.types.Field('_AddMinutesSpeechesPayload', graphql_name='AddMinutesSpeeches', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SpeechInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    remove_minutes_speeches = sgqlc.types.Field('_RemoveMinutesSpeechesPayload', graphql_name='RemoveMinutesSpeeches', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SpeechInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    merge_minutes_speeches = sgqlc.types.Field('_MergeMinutesSpeechesPayload', graphql_name='MergeMinutesSpeeches', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SpeechInput), graphql_name='from', default=None)),
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
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('start_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startDateTime', default=None)),
        ('end_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='endDateTime', default=None)),
        ('topics', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='topics', default=None)),
        ('summary', sgqlc.types.Arg(String, graphql_name='summary', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags', default=None)),
))
    )
    update_minutes = sgqlc.types.Field(Minutes, graphql_name='UpdateMinutes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('start_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startDateTime', default=None)),
        ('end_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='endDateTime', default=None)),
        ('topics', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='topics', default=None)),
        ('summary', sgqlc.types.Arg(String, graphql_name='summary', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
))
    )
    delete_minutes = sgqlc.types.Field(Minutes, graphql_name='DeleteMinutes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_minutes = sgqlc.types.Field(Minutes, graphql_name='MergeMinutes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('start_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startDateTime', default=None)),
        ('end_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='endDateTime', default=None)),
        ('topics', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='topics', default=None)),
        ('summary', sgqlc.types.Arg(String, graphql_name='summary', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
))
    )
    add_speech_belonged_to_minutes = sgqlc.types.Field('_AddSpeechBelongedToMinutesPayload', graphql_name='AddSpeechBelongedToMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SpeechInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    remove_speech_belonged_to_minutes = sgqlc.types.Field('_RemoveSpeechBelongedToMinutesPayload', graphql_name='RemoveSpeechBelongedToMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SpeechInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    merge_speech_belonged_to_minutes = sgqlc.types.Field('_MergeSpeechBelongedToMinutesPayload', graphql_name='MergeSpeechBelongedToMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SpeechInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    add_speech_be_delivered_by_member = sgqlc.types.Field('_AddSpeechBeDeliveredByMemberPayload', graphql_name='AddSpeechBeDeliveredByMember', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SpeechInput), graphql_name='to', default=None)),
))
    )
    remove_speech_be_delivered_by_member = sgqlc.types.Field('_RemoveSpeechBeDeliveredByMemberPayload', graphql_name='RemoveSpeechBeDeliveredByMember', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SpeechInput), graphql_name='to', default=None)),
))
    )
    merge_speech_be_delivered_by_member = sgqlc.types.Field('_MergeSpeechBeDeliveredByMemberPayload', graphql_name='MergeSpeechBeDeliveredByMember', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SpeechInput), graphql_name='to', default=None)),
))
    )
    create_speech = sgqlc.types.Field('Speech', graphql_name='CreateSpeech', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('speaker_name', sgqlc.types.Arg(String, graphql_name='speakerName', default=None)),
        ('order_in_minutes', sgqlc.types.Arg(Int, graphql_name='orderInMinutes', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags', default=None)),
))
    )
    update_speech = sgqlc.types.Field('Speech', graphql_name='UpdateSpeech', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('speaker_name', sgqlc.types.Arg(String, graphql_name='speakerName', default=None)),
        ('order_in_minutes', sgqlc.types.Arg(Int, graphql_name='orderInMinutes', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
))
    )
    delete_speech = sgqlc.types.Field('Speech', graphql_name='DeleteSpeech', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_speech = sgqlc.types.Field('Speech', graphql_name='MergeSpeech', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('speaker_name', sgqlc.types.Arg(String, graphql_name='speakerName', default=None)),
        ('order_in_minutes', sgqlc.types.Arg(Int, graphql_name='orderInMinutes', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
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
    add_url_referred_minutes = sgqlc.types.Field('_AddUrlReferredMinutesPayload', graphql_name='AddUrlReferredMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    remove_url_referred_minutes = sgqlc.types.Field('_RemoveUrlReferredMinutesPayload', graphql_name='RemoveUrlReferredMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    merge_url_referred_minutes = sgqlc.types.Field('_MergeUrlReferredMinutesPayload', graphql_name='MergeUrlReferredMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
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
    add_news_referred_bills = sgqlc.types.Field('_AddNewsReferredBillsPayload', graphql_name='AddNewsReferredBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_news_referred_bills = sgqlc.types.Field('_RemoveNewsReferredBillsPayload', graphql_name='RemoveNewsReferredBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_news_referred_bills = sgqlc.types.Field('_MergeNewsReferredBillsPayload', graphql_name='MergeNewsReferredBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    add_news_referred_laws = sgqlc.types.Field('_AddNewsReferredLawsPayload', graphql_name='AddNewsReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    remove_news_referred_laws = sgqlc.types.Field('_RemoveNewsReferredLawsPayload', graphql_name='RemoveNewsReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    merge_news_referred_laws = sgqlc.types.Field('_MergeNewsReferredLawsPayload', graphql_name='MergeNewsReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    add_news_referred_members = sgqlc.types.Field('_AddNewsReferredMembersPayload', graphql_name='AddNewsReferredMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    remove_news_referred_members = sgqlc.types.Field('_RemoveNewsReferredMembersPayload', graphql_name='RemoveNewsReferredMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    merge_news_referred_members = sgqlc.types.Field('_MergeNewsReferredMembersPayload', graphql_name='MergeNewsReferredMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    add_news_referred_minutes = sgqlc.types.Field('_AddNewsReferredMinutesPayload', graphql_name='AddNewsReferredMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    remove_news_referred_minutes = sgqlc.types.Field('_RemoveNewsReferredMinutesPayload', graphql_name='RemoveNewsReferredMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    merge_news_referred_minutes = sgqlc.types.Field('_MergeNewsReferredMinutesPayload', graphql_name='MergeNewsReferredMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    create_news = sgqlc.types.Field('News', graphql_name='CreateNews', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
        ('publisher', sgqlc.types.Arg(String, graphql_name='publisher', default=None)),
        ('thumbnail', sgqlc.types.Arg(String, graphql_name='thumbnail', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('published_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='publishedAt', default=None)),
        ('last_modified_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='lastModifiedAt', default=None)),
        ('is_paid', sgqlc.types.Arg(Boolean, graphql_name='isPaid', default=None)),
))
    )
    update_news = sgqlc.types.Field('News', graphql_name='UpdateNews', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('publisher', sgqlc.types.Arg(String, graphql_name='publisher', default=None)),
        ('thumbnail', sgqlc.types.Arg(String, graphql_name='thumbnail', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('published_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='publishedAt', default=None)),
        ('last_modified_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='lastModifiedAt', default=None)),
        ('is_paid', sgqlc.types.Arg(Boolean, graphql_name='isPaid', default=None)),
))
    )
    delete_news = sgqlc.types.Field('News', graphql_name='DeleteNews', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_news = sgqlc.types.Field('News', graphql_name='MergeNews', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('publisher', sgqlc.types.Arg(String, graphql_name='publisher', default=None)),
        ('thumbnail', sgqlc.types.Arg(String, graphql_name='thumbnail', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('published_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='publishedAt', default=None)),
        ('last_modified_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='lastModifiedAt', default=None)),
        ('is_paid', sgqlc.types.Arg(Boolean, graphql_name='isPaid', default=None)),
))
    )
    add_timeline_bills = sgqlc.types.Field('_AddTimelineBillsPayload', graphql_name='AddTimelineBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    remove_timeline_bills = sgqlc.types.Field('_RemoveTimelineBillsPayload', graphql_name='RemoveTimelineBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    merge_timeline_bills = sgqlc.types.Field('_MergeTimelineBillsPayload', graphql_name='MergeTimelineBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    add_timeline_minutes = sgqlc.types.Field('_AddTimelineMinutesPayload', graphql_name='AddTimelineMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    remove_timeline_minutes = sgqlc.types.Field('_RemoveTimelineMinutesPayload', graphql_name='RemoveTimelineMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    merge_timeline_minutes = sgqlc.types.Field('_MergeTimelineMinutesPayload', graphql_name='MergeTimelineMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    add_timeline_news = sgqlc.types.Field('_AddTimelineNewsPayload', graphql_name='AddTimelineNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    remove_timeline_news = sgqlc.types.Field('_RemoveTimelineNewsPayload', graphql_name='RemoveTimelineNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    merge_timeline_news = sgqlc.types.Field('_MergeTimelineNewsPayload', graphql_name='MergeTimelineNews', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_NewsInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    create_timeline = sgqlc.types.Field('Timeline', graphql_name='CreateTimeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='date', default=None)),
))
    )
    update_timeline = sgqlc.types.Field('Timeline', graphql_name='UpdateTimeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='date', default=None)),
))
    )
    delete_timeline = sgqlc.types.Field('Timeline', graphql_name='DeleteTimeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_timeline = sgqlc.types.Field('Timeline', graphql_name='MergeTimeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='date', default=None)),
))
    )


class News(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'url', 'publisher', 'thumbnail', 'title', 'published_at', 'last_modified_at', 'is_paid', 'referred_bills', 'referred_laws', 'referred_members', 'referred_minutes', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    publisher = sgqlc.types.Field(String, graphql_name='publisher')
    thumbnail = sgqlc.types.Field(String, graphql_name='thumbnail')
    title = sgqlc.types.Field(String, graphql_name='title')
    published_at = sgqlc.types.Field('_Neo4jDateTime', graphql_name='publishedAt')
    last_modified_at = sgqlc.types.Field('_Neo4jDateTime', graphql_name='lastModifiedAt')
    is_paid = sgqlc.types.Field(Boolean, graphql_name='isPaid')
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
    referred_minutes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Minutes))), graphql_name='referredMinutes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MinutesOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MinutesFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Query(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('total_members', 'total_elections', 'total_election_results', 'total_diets', 'total_laws', 'total_bills', 'total_committees', 'total_minutes', 'total_speeches', 'total_urls', 'total_news', 'total_timelines', 'member', 'election', 'election_result', 'diet', 'law', 'bill', 'committee', 'minutes', 'speech', 'url', 'news', 'timeline')
    total_members = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='TotalMembers')
    total_elections = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='TotalElections')
    total_election_results = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='TotalElectionResults')
    total_diets = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='TotalDiets')
    total_laws = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='TotalLaws')
    total_bills = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='TotalBills')
    total_committees = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='TotalCommittees')
    total_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='TotalMinutes')
    total_speeches = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='TotalSpeeches')
    total_urls = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='TotalUrls')
    total_news = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='TotalNews')
    total_timelines = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='TotalTimelines')
    member = sgqlc.types.Field(sgqlc.types.list_of('Member'), graphql_name='Member', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('name_hira', sgqlc.types.Arg(String, graphql_name='nameHira', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('first_name_hira', sgqlc.types.Arg(String, graphql_name='firstNameHira', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
        ('last_name_hira', sgqlc.types.Arg(String, graphql_name='lastNameHira', default=None)),
        ('house', sgqlc.types.Arg(House, graphql_name='house', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('tags', sgqlc.types.Arg(String, graphql_name='tags', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MemberOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MemberFilter, graphql_name='filter', default=None)),
))
    )
    election = sgqlc.types.Field(sgqlc.types.list_of('Election'), graphql_name='Election', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='date', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_ElectionOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_ElectionFilter, graphql_name='filter', default=None)),
))
    )
    election_result = sgqlc.types.Field(sgqlc.types.list_of('ElectionResult'), graphql_name='ElectionResult', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('system', sgqlc.types.Arg(ElectionSystem, graphql_name='system', default=None)),
        ('district', sgqlc.types.Arg(String, graphql_name='district', default=None)),
        ('prefecture', sgqlc.types.Arg(String, graphql_name='prefecture', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_ElectionResultOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_ElectionResultFilter, graphql_name='filter', default=None)),
))
    )
    diet = sgqlc.types.Field(sgqlc.types.list_of('Diet'), graphql_name='Diet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('number', sgqlc.types.Arg(Int, graphql_name='number', default=None)),
        ('category', sgqlc.types.Arg(DietCategory, graphql_name='category', default=None)),
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
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('law_number', sgqlc.types.Arg(String, graphql_name='lawNumber', default=None)),
        ('summary', sgqlc.types.Arg(String, graphql_name='summary', default=None)),
        ('tags', sgqlc.types.Arg(String, graphql_name='tags', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_LawOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_LawFilter, graphql_name='filter', default=None)),
))
    )
    bill = sgqlc.types.Field(sgqlc.types.list_of('Bill'), graphql_name='Bill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('bill_number', sgqlc.types.Arg(String, graphql_name='billNumber', default=None)),
        ('category', sgqlc.types.Arg(BillCategory, graphql_name='category', default=None)),
        ('is_amendment', sgqlc.types.Arg(Boolean, graphql_name='isAmendment', default=None)),
        ('is_passed', sgqlc.types.Arg(Boolean, graphql_name='isPassed', default=None)),
        ('reason', sgqlc.types.Arg(String, graphql_name='reason', default=None)),
        ('summary', sgqlc.types.Arg(String, graphql_name='summary', default=None)),
        ('aliases', sgqlc.types.Arg(String, graphql_name='aliases', default=None)),
        ('tags', sgqlc.types.Arg(String, graphql_name='tags', default=None)),
        ('first_house', sgqlc.types.Arg(House, graphql_name='firstHouse', default=None)),
        ('submitted_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='submittedDate', default=None)),
        ('passed_representatives_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedRepresentativesCommitteeDate', default=None)),
        ('passed_representatives_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedRepresentativesDate', default=None)),
        ('passed_councilors_committee_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedCouncilorsCommitteeDate', default=None)),
        ('passed_councilors_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='passedCouncilorsDate', default=None)),
        ('proclaimed_date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='proclaimedDate', default=None)),
        ('total_news', sgqlc.types.Arg(Int, graphql_name='totalNews', default=None)),
        ('total_minutes', sgqlc.types.Arg(Int, graphql_name='totalMinutes', default=None)),
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
        ('topics', sgqlc.types.Arg(String, graphql_name='topics', default=None)),
        ('num_members', sgqlc.types.Arg(Int, graphql_name='numMembers', default=None)),
        ('house', sgqlc.types.Arg(House, graphql_name='house', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('aliases', sgqlc.types.Arg(String, graphql_name='aliases', default=None)),
        ('tags', sgqlc.types.Arg(String, graphql_name='tags', default=None)),
        ('total_minutes', sgqlc.types.Arg(Int, graphql_name='totalMinutes', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_CommitteeOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_CommitteeFilter, graphql_name='filter', default=None)),
))
    )
    minutes = sgqlc.types.Field(sgqlc.types.list_of('Minutes'), graphql_name='Minutes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('start_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startDateTime', default=None)),
        ('end_date_time', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='endDateTime', default=None)),
        ('topics', sgqlc.types.Arg(String, graphql_name='topics', default=None)),
        ('summary', sgqlc.types.Arg(String, graphql_name='summary', default=None)),
        ('tags', sgqlc.types.Arg(String, graphql_name='tags', default=None)),
        ('total_news', sgqlc.types.Arg(Int, graphql_name='totalNews', default=None)),
        ('total_bills', sgqlc.types.Arg(Int, graphql_name='totalBills', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MinutesOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MinutesFilter, graphql_name='filter', default=None)),
))
    )
    speech = sgqlc.types.Field(sgqlc.types.list_of('Speech'), graphql_name='Speech', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('speaker_name', sgqlc.types.Arg(String, graphql_name='speakerName', default=None)),
        ('order_in_minutes', sgqlc.types.Arg(Int, graphql_name='orderInMinutes', default=None)),
        ('tags', sgqlc.types.Arg(String, graphql_name='tags', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_SpeechOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_SpeechFilter, graphql_name='filter', default=None)),
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
    news = sgqlc.types.Field(sgqlc.types.list_of('News'), graphql_name='News', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('publisher', sgqlc.types.Arg(String, graphql_name='publisher', default=None)),
        ('thumbnail', sgqlc.types.Arg(String, graphql_name='thumbnail', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('published_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='publishedAt', default=None)),
        ('last_modified_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='lastModifiedAt', default=None)),
        ('is_paid', sgqlc.types.Arg(Boolean, graphql_name='isPaid', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_NewsOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_NewsFilter, graphql_name='filter', default=None)),
))
    )
    timeline = sgqlc.types.Field(sgqlc.types.list_of('Timeline'), graphql_name='Timeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('date', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='date', default=None)),
        ('total_bills', sgqlc.types.Arg(Int, graphql_name='totalBills', default=None)),
        ('total_minutes', sgqlc.types.Arg(Int, graphql_name='totalMinutes', default=None)),
        ('total_news', sgqlc.types.Arg(Int, graphql_name='totalNews', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_TimelineOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_TimelineFilter, graphql_name='filter', default=None)),
))
    )


class Speech(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'speaker_name', 'order_in_minutes', 'tags', 'belonged_to_minutes', 'be_delivered_by_member', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    speaker_name = sgqlc.types.Field(String, graphql_name='speakerName')
    order_in_minutes = sgqlc.types.Field(Int, graphql_name='orderInMinutes')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    belonged_to_minutes = sgqlc.types.Field(Minutes, graphql_name='belongedToMinutes', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_MinutesFilter, graphql_name='filter', default=None)),
))
    )
    be_delivered_by_member = sgqlc.types.Field(Member, graphql_name='beDeliveredByMember', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_MemberFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Timeline(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'date', 'bills', 'minutes', 'news', 'total_bills', 'total_minutes', 'total_news', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='date')
    bills = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bill))), graphql_name='bills', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    minutes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Minutes))), graphql_name='minutes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MinutesOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MinutesFilter, graphql_name='filter', default=None)),
))
    )
    news = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(News))), graphql_name='news', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_NewsOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_NewsFilter, graphql_name='filter', default=None)),
))
    )
    total_bills = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalBills')
    total_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalMinutes')
    total_news = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalNews')
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Url(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'url', 'domain', 'title', 'description', 'referred_bills', 'referred_laws', 'referred_members', 'referred_minutes', '_id')
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
    referred_minutes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Minutes))), graphql_name='referredMinutes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MinutesOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MinutesFilter, graphql_name='filter', default=None)),
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


class _AddBillNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
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


class _AddElectionElectionResultsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(ElectionResult, graphql_name='from')
    to = sgqlc.types.Field(Election, graphql_name='to')


class _AddElectionResultBelongedToElectionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(ElectionResult, graphql_name='from')
    to = sgqlc.types.Field(Election, graphql_name='to')


class _AddElectionResultElectedMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(ElectionResult, graphql_name='from')
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


class _AddLawNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _AddLawReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
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


class _AddMemberDeliveredSpeechesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Speech, graphql_name='to')


class _AddMemberNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _AddMemberSubmittedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


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


class _AddMinutesNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _AddMinutesSpeechesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Speech, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _AddMinutesUrlsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _AddNewsReferredBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddNewsReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _AddNewsReferredMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _AddNewsReferredMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _AddSpeechBeDeliveredByMemberPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Speech, graphql_name='to')


class _AddSpeechBelongedToMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Speech, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _AddTimelineBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _AddTimelineMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _AddTimelineNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


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


class _AddUrlReferredMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


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


class _MergeBillNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
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


class _MergeElectionElectionResultsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(ElectionResult, graphql_name='from')
    to = sgqlc.types.Field(Election, graphql_name='to')


class _MergeElectionResultBelongedToElectionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(ElectionResult, graphql_name='from')
    to = sgqlc.types.Field(Election, graphql_name='to')


class _MergeElectionResultElectedMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(ElectionResult, graphql_name='from')
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


class _MergeLawNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _MergeLawReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
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


class _MergeMemberDeliveredSpeechesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Speech, graphql_name='to')


class _MergeMemberNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _MergeMemberSubmittedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


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


class _MergeMinutesNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _MergeMinutesSpeechesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Speech, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _MergeMinutesUrlsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _MergeNewsReferredBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeNewsReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _MergeNewsReferredMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _MergeNewsReferredMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _MergeSpeechBeDeliveredByMemberPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Speech, graphql_name='to')


class _MergeSpeechBelongedToMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Speech, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _MergeTimelineBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _MergeTimelineMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _MergeTimelineNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


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


class _MergeUrlReferredMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


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


class _RemoveBillNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
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


class _RemoveElectionElectionResultsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(ElectionResult, graphql_name='from')
    to = sgqlc.types.Field(Election, graphql_name='to')


class _RemoveElectionResultBelongedToElectionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(ElectionResult, graphql_name='from')
    to = sgqlc.types.Field(Election, graphql_name='to')


class _RemoveElectionResultElectedMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(ElectionResult, graphql_name='from')
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


class _RemoveLawNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _RemoveLawReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
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


class _RemoveMemberDeliveredSpeechesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Speech, graphql_name='to')


class _RemoveMemberNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _RemoveMemberSubmittedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


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


class _RemoveMinutesNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _RemoveMinutesSpeechesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Speech, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _RemoveMinutesUrlsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _RemoveNewsReferredBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveNewsReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _RemoveNewsReferredMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _RemoveNewsReferredMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _RemoveSpeechBeDeliveredByMemberPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Speech, graphql_name='to')


class _RemoveSpeechBelongedToMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Speech, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _RemoveTimelineBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _RemoveTimelineMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _RemoveTimelineNewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(News, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


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


class _RemoveUrlReferredMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Url, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None

