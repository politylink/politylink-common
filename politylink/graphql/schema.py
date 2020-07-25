import sgqlc.types


schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class BillCategory(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('KAKUHOU', 'SYUHOU', 'SANHOU')


class BillStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('IN_REVIEW', 'ACCEPTED', 'WITHDRAWN')


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
    __choices__ = ('id_asc', 'id_desc', 'ndlId_asc', 'ndlId_desc', 'ndlUrl_asc', 'ndlUrl_desc', 'billTitle_asc', 'billTitle_desc', 'billNumber_asc', 'billNumber_desc', 'billCategory_asc', 'billCategory_desc', 'billType_asc', 'billType_desc', 'billStatus_asc', 'billStatus_desc', 'syugiinUrl_asc', 'syugiinUrl_desc', 'sangiinUrl_asc', 'sangiinUrl_desc', 'overviewUrl_asc', 'overviewUrl_desc', 'essentialUrl_asc', 'essentialUrl_desc', 'comparisonUrl_asc', 'comparisonUrl_desc', 'pullRequestUrl_asc', 'pullRequestUrl_desc', '_id_asc', '_id_desc')


class _DietOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'number_asc', 'number_desc', 'name_asc', 'name_desc', 'startDate_asc', 'startDate_desc', 'endDate_asc', 'endDate_desc', '_id_asc', '_id_desc')


class _ElectionOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'electionType_asc', 'electionType_desc', 'district_asc', 'district_desc', 'prefecture_asc', 'prefecture_desc', 'datetime_asc', 'datetime_desc', '_id_asc', '_id_desc')


class _LawOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'ndlId_asc', 'ndlId_desc', 'eGovId_asc', 'eGovId_desc', 'eGovUrl_asc', 'eGovUrl_desc', 'lawTitle_asc', 'lawTitle_desc', 'lawNumber_asc', 'lawNumber_desc', '_id_asc', '_id_desc')


class _MeetingOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'name_asc', 'name_desc', '_id_asc', '_id_desc')


class _MemberOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'name_asc', 'name_desc', 'firstName_asc', 'firstName_desc', 'lastName_asc', 'lastName_desc', 'nameHira_asc', 'nameHira_desc', 'firstNameHira_asc', 'firstNameHira_desc', 'lastNameHira_asc', 'lastNameHira_desc', 'current_asc', 'current_desc', 'house_asc', 'house_desc', '_id_asc', '_id_desc')


class _MinutesOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'ndlId_asc', 'ndlId_desc', 'ndlUrl_asc', 'ndlUrl_desc', 'minutesNumber_asc', 'minutesNumber_desc', 'start_asc', 'start_desc', 'end_asc', 'end_desc', '_id_asc', '_id_desc')


class _RelationDirections(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('IN', 'OUT')


class _TimelineOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'content_asc', 'content_desc', 'startedOn_asc', 'startedOn_desc', '_id_asc', '_id_desc')


class _UrlOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'url_asc', 'url_desc', 'text_asc', 'text_desc', 'type_asc', 'type_desc', 'domain_asc', 'domain_desc', 'accessedOn_asc', 'accessedOn_desc', '_id_asc', '_id_desc')



########################################################################
# Input Objects
########################################################################
class _BillFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'ndl_id', 'ndl_id_not', 'ndl_id_in', 'ndl_id_not_in', 'ndl_id_contains', 'ndl_id_not_contains', 'ndl_id_starts_with', 'ndl_id_not_starts_with', 'ndl_id_ends_with', 'ndl_id_not_ends_with', 'ndl_url', 'ndl_url_not', 'ndl_url_in', 'ndl_url_not_in', 'ndl_url_contains', 'ndl_url_not_contains', 'ndl_url_starts_with', 'ndl_url_not_starts_with', 'ndl_url_ends_with', 'ndl_url_not_ends_with', 'bill_title', 'bill_title_not', 'bill_title_in', 'bill_title_not_in', 'bill_title_contains', 'bill_title_not_contains', 'bill_title_starts_with', 'bill_title_not_starts_with', 'bill_title_ends_with', 'bill_title_not_ends_with', 'bill_number', 'bill_number_not', 'bill_number_in', 'bill_number_not_in', 'bill_number_contains', 'bill_number_not_contains', 'bill_number_starts_with', 'bill_number_not_starts_with', 'bill_number_ends_with', 'bill_number_not_ends_with', 'bill_category', 'bill_category_not', 'bill_category_in', 'bill_category_not_in', 'bill_type', 'bill_type_not', 'bill_type_in', 'bill_type_not_in', 'bill_status', 'bill_status_not', 'bill_status_in', 'bill_status_not_in', 'submitted_by', 'submitted_by_not', 'submitted_by_in', 'submitted_by_not_in', 'submitted_by_some', 'submitted_by_none', 'submitted_by_single', 'submitted_by_every', 'submitted_to', 'submitted_to_not', 'submitted_to_in', 'submitted_to_not_in', 'discussed_at', 'discussed_at_not', 'discussed_at_in', 'discussed_at_not_in', 'discussed_at_some', 'discussed_at_none', 'discussed_at_single', 'discussed_at_every', 'ammends', 'ammends_not', 'ammends_in', 'ammends_not_in', 'ammends_some', 'ammends_none', 'ammends_single', 'ammends_every', 'syugiin_url', 'syugiin_url_not', 'syugiin_url_in', 'syugiin_url_not_in', 'syugiin_url_contains', 'syugiin_url_not_contains', 'syugiin_url_starts_with', 'syugiin_url_not_starts_with', 'syugiin_url_ends_with', 'syugiin_url_not_ends_with', 'sangiin_url', 'sangiin_url_not', 'sangiin_url_in', 'sangiin_url_not_in', 'sangiin_url_contains', 'sangiin_url_not_contains', 'sangiin_url_starts_with', 'sangiin_url_not_starts_with', 'sangiin_url_ends_with', 'sangiin_url_not_ends_with', 'overview_url', 'overview_url_not', 'overview_url_in', 'overview_url_not_in', 'overview_url_contains', 'overview_url_not_contains', 'overview_url_starts_with', 'overview_url_not_starts_with', 'overview_url_ends_with', 'overview_url_not_ends_with', 'essential_url', 'essential_url_not', 'essential_url_in', 'essential_url_not_in', 'essential_url_contains', 'essential_url_not_contains', 'essential_url_starts_with', 'essential_url_not_starts_with', 'essential_url_ends_with', 'essential_url_not_ends_with', 'comparison_url', 'comparison_url_not', 'comparison_url_in', 'comparison_url_not_in', 'comparison_url_contains', 'comparison_url_not_contains', 'comparison_url_starts_with', 'comparison_url_not_starts_with', 'comparison_url_ends_with', 'comparison_url_not_ends_with', 'pull_request_url', 'pull_request_url_not', 'pull_request_url_in', 'pull_request_url_not_in', 'pull_request_url_contains', 'pull_request_url_not_contains', 'pull_request_url_starts_with', 'pull_request_url_not_starts_with', 'pull_request_url_ends_with', 'pull_request_url_not_ends_with', 'refer_url', 'refer_url_not', 'refer_url_in', 'refer_url_not_in', 'refer_url_some', 'refer_url_none', 'refer_url_single', 'refer_url_every', 'related_time_line', 'related_time_line_not', 'related_time_line_in', 'related_time_line_not_in', 'related_time_line_some', 'related_time_line_none', 'related_time_line_single', 'related_time_line_every')
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
    ndl_id = sgqlc.types.Field(String, graphql_name='ndlId')
    ndl_id_not = sgqlc.types.Field(String, graphql_name='ndlId_not')
    ndl_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ndlId_in')
    ndl_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ndlId_not_in')
    ndl_id_contains = sgqlc.types.Field(String, graphql_name='ndlId_contains')
    ndl_id_not_contains = sgqlc.types.Field(String, graphql_name='ndlId_not_contains')
    ndl_id_starts_with = sgqlc.types.Field(String, graphql_name='ndlId_starts_with')
    ndl_id_not_starts_with = sgqlc.types.Field(String, graphql_name='ndlId_not_starts_with')
    ndl_id_ends_with = sgqlc.types.Field(String, graphql_name='ndlId_ends_with')
    ndl_id_not_ends_with = sgqlc.types.Field(String, graphql_name='ndlId_not_ends_with')
    ndl_url = sgqlc.types.Field(String, graphql_name='ndlUrl')
    ndl_url_not = sgqlc.types.Field(String, graphql_name='ndlUrl_not')
    ndl_url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ndlUrl_in')
    ndl_url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ndlUrl_not_in')
    ndl_url_contains = sgqlc.types.Field(String, graphql_name='ndlUrl_contains')
    ndl_url_not_contains = sgqlc.types.Field(String, graphql_name='ndlUrl_not_contains')
    ndl_url_starts_with = sgqlc.types.Field(String, graphql_name='ndlUrl_starts_with')
    ndl_url_not_starts_with = sgqlc.types.Field(String, graphql_name='ndlUrl_not_starts_with')
    ndl_url_ends_with = sgqlc.types.Field(String, graphql_name='ndlUrl_ends_with')
    ndl_url_not_ends_with = sgqlc.types.Field(String, graphql_name='ndlUrl_not_ends_with')
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
    bill_status = sgqlc.types.Field(BillStatus, graphql_name='billStatus')
    bill_status_not = sgqlc.types.Field(BillStatus, graphql_name='billStatus_not')
    bill_status_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BillStatus)), graphql_name='billStatus_in')
    bill_status_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BillStatus)), graphql_name='billStatus_not_in')
    submitted_by = sgqlc.types.Field('_MemberFilter', graphql_name='submittedBy')
    submitted_by_not = sgqlc.types.Field('_MemberFilter', graphql_name='submittedBy_not')
    submitted_by_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MemberFilter')), graphql_name='submittedBy_in')
    submitted_by_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MemberFilter')), graphql_name='submittedBy_not_in')
    submitted_by_some = sgqlc.types.Field('_MemberFilter', graphql_name='submittedBy_some')
    submitted_by_none = sgqlc.types.Field('_MemberFilter', graphql_name='submittedBy_none')
    submitted_by_single = sgqlc.types.Field('_MemberFilter', graphql_name='submittedBy_single')
    submitted_by_every = sgqlc.types.Field('_MemberFilter', graphql_name='submittedBy_every')
    submitted_to = sgqlc.types.Field('_DietFilter', graphql_name='submittedTo')
    submitted_to_not = sgqlc.types.Field('_DietFilter', graphql_name='submittedTo_not')
    submitted_to_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_DietFilter')), graphql_name='submittedTo_in')
    submitted_to_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_DietFilter')), graphql_name='submittedTo_not_in')
    discussed_at = sgqlc.types.Field('_MinutesFilter', graphql_name='discussedAt')
    discussed_at_not = sgqlc.types.Field('_MinutesFilter', graphql_name='discussedAt_not')
    discussed_at_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='discussedAt_in')
    discussed_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='discussedAt_not_in')
    discussed_at_some = sgqlc.types.Field('_MinutesFilter', graphql_name='discussedAt_some')
    discussed_at_none = sgqlc.types.Field('_MinutesFilter', graphql_name='discussedAt_none')
    discussed_at_single = sgqlc.types.Field('_MinutesFilter', graphql_name='discussedAt_single')
    discussed_at_every = sgqlc.types.Field('_MinutesFilter', graphql_name='discussedAt_every')
    ammends = sgqlc.types.Field('_LawFilter', graphql_name='ammends')
    ammends_not = sgqlc.types.Field('_LawFilter', graphql_name='ammends_not')
    ammends_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_LawFilter')), graphql_name='ammends_in')
    ammends_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_LawFilter')), graphql_name='ammends_not_in')
    ammends_some = sgqlc.types.Field('_LawFilter', graphql_name='ammends_some')
    ammends_none = sgqlc.types.Field('_LawFilter', graphql_name='ammends_none')
    ammends_single = sgqlc.types.Field('_LawFilter', graphql_name='ammends_single')
    ammends_every = sgqlc.types.Field('_LawFilter', graphql_name='ammends_every')
    syugiin_url = sgqlc.types.Field(String, graphql_name='syugiinUrl')
    syugiin_url_not = sgqlc.types.Field(String, graphql_name='syugiinUrl_not')
    syugiin_url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='syugiinUrl_in')
    syugiin_url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='syugiinUrl_not_in')
    syugiin_url_contains = sgqlc.types.Field(String, graphql_name='syugiinUrl_contains')
    syugiin_url_not_contains = sgqlc.types.Field(String, graphql_name='syugiinUrl_not_contains')
    syugiin_url_starts_with = sgqlc.types.Field(String, graphql_name='syugiinUrl_starts_with')
    syugiin_url_not_starts_with = sgqlc.types.Field(String, graphql_name='syugiinUrl_not_starts_with')
    syugiin_url_ends_with = sgqlc.types.Field(String, graphql_name='syugiinUrl_ends_with')
    syugiin_url_not_ends_with = sgqlc.types.Field(String, graphql_name='syugiinUrl_not_ends_with')
    sangiin_url = sgqlc.types.Field(String, graphql_name='sangiinUrl')
    sangiin_url_not = sgqlc.types.Field(String, graphql_name='sangiinUrl_not')
    sangiin_url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sangiinUrl_in')
    sangiin_url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sangiinUrl_not_in')
    sangiin_url_contains = sgqlc.types.Field(String, graphql_name='sangiinUrl_contains')
    sangiin_url_not_contains = sgqlc.types.Field(String, graphql_name='sangiinUrl_not_contains')
    sangiin_url_starts_with = sgqlc.types.Field(String, graphql_name='sangiinUrl_starts_with')
    sangiin_url_not_starts_with = sgqlc.types.Field(String, graphql_name='sangiinUrl_not_starts_with')
    sangiin_url_ends_with = sgqlc.types.Field(String, graphql_name='sangiinUrl_ends_with')
    sangiin_url_not_ends_with = sgqlc.types.Field(String, graphql_name='sangiinUrl_not_ends_with')
    overview_url = sgqlc.types.Field(String, graphql_name='overviewUrl')
    overview_url_not = sgqlc.types.Field(String, graphql_name='overviewUrl_not')
    overview_url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='overviewUrl_in')
    overview_url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='overviewUrl_not_in')
    overview_url_contains = sgqlc.types.Field(String, graphql_name='overviewUrl_contains')
    overview_url_not_contains = sgqlc.types.Field(String, graphql_name='overviewUrl_not_contains')
    overview_url_starts_with = sgqlc.types.Field(String, graphql_name='overviewUrl_starts_with')
    overview_url_not_starts_with = sgqlc.types.Field(String, graphql_name='overviewUrl_not_starts_with')
    overview_url_ends_with = sgqlc.types.Field(String, graphql_name='overviewUrl_ends_with')
    overview_url_not_ends_with = sgqlc.types.Field(String, graphql_name='overviewUrl_not_ends_with')
    essential_url = sgqlc.types.Field(String, graphql_name='essentialUrl')
    essential_url_not = sgqlc.types.Field(String, graphql_name='essentialUrl_not')
    essential_url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='essentialUrl_in')
    essential_url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='essentialUrl_not_in')
    essential_url_contains = sgqlc.types.Field(String, graphql_name='essentialUrl_contains')
    essential_url_not_contains = sgqlc.types.Field(String, graphql_name='essentialUrl_not_contains')
    essential_url_starts_with = sgqlc.types.Field(String, graphql_name='essentialUrl_starts_with')
    essential_url_not_starts_with = sgqlc.types.Field(String, graphql_name='essentialUrl_not_starts_with')
    essential_url_ends_with = sgqlc.types.Field(String, graphql_name='essentialUrl_ends_with')
    essential_url_not_ends_with = sgqlc.types.Field(String, graphql_name='essentialUrl_not_ends_with')
    comparison_url = sgqlc.types.Field(String, graphql_name='comparisonUrl')
    comparison_url_not = sgqlc.types.Field(String, graphql_name='comparisonUrl_not')
    comparison_url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='comparisonUrl_in')
    comparison_url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='comparisonUrl_not_in')
    comparison_url_contains = sgqlc.types.Field(String, graphql_name='comparisonUrl_contains')
    comparison_url_not_contains = sgqlc.types.Field(String, graphql_name='comparisonUrl_not_contains')
    comparison_url_starts_with = sgqlc.types.Field(String, graphql_name='comparisonUrl_starts_with')
    comparison_url_not_starts_with = sgqlc.types.Field(String, graphql_name='comparisonUrl_not_starts_with')
    comparison_url_ends_with = sgqlc.types.Field(String, graphql_name='comparisonUrl_ends_with')
    comparison_url_not_ends_with = sgqlc.types.Field(String, graphql_name='comparisonUrl_not_ends_with')
    pull_request_url = sgqlc.types.Field(String, graphql_name='pullRequestUrl')
    pull_request_url_not = sgqlc.types.Field(String, graphql_name='pullRequestUrl_not')
    pull_request_url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pullRequestUrl_in')
    pull_request_url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pullRequestUrl_not_in')
    pull_request_url_contains = sgqlc.types.Field(String, graphql_name='pullRequestUrl_contains')
    pull_request_url_not_contains = sgqlc.types.Field(String, graphql_name='pullRequestUrl_not_contains')
    pull_request_url_starts_with = sgqlc.types.Field(String, graphql_name='pullRequestUrl_starts_with')
    pull_request_url_not_starts_with = sgqlc.types.Field(String, graphql_name='pullRequestUrl_not_starts_with')
    pull_request_url_ends_with = sgqlc.types.Field(String, graphql_name='pullRequestUrl_ends_with')
    pull_request_url_not_ends_with = sgqlc.types.Field(String, graphql_name='pullRequestUrl_not_ends_with')
    refer_url = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl')
    refer_url_not = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_not')
    refer_url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='referUrl_in')
    refer_url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='referUrl_not_in')
    refer_url_some = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_some')
    refer_url_none = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_none')
    refer_url_single = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_single')
    refer_url_every = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_every')
    related_time_line = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine')
    related_time_line_not = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_not')
    related_time_line_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimelineFilter')), graphql_name='relatedTimeLine_in')
    related_time_line_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimelineFilter')), graphql_name='relatedTimeLine_not_in')
    related_time_line_some = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_some')
    related_time_line_none = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_none')
    related_time_line_single = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_single')
    related_time_line_every = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_every')


class _BillInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _DietFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'number', 'number_not', 'number_in', 'number_not_in', 'number_lt', 'number_lte', 'number_gt', 'number_gte', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'start_date', 'start_date_not', 'start_date_in', 'start_date_not_in', 'start_date_lt', 'start_date_lte', 'start_date_gt', 'start_date_gte', 'end_date', 'end_date_not', 'end_date_in', 'end_date_not_in', 'end_date_lt', 'end_date_lte', 'end_date_gt', 'end_date_gte', 'bills', 'bills_not', 'bills_in', 'bills_not_in', 'bills_some', 'bills_none', 'bills_single', 'bills_every', 'minutes', 'minutes_not', 'minutes_in', 'minutes_not_in', 'minutes_some', 'minutes_none', 'minutes_single', 'minutes_every')
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
    bills = sgqlc.types.Field(_BillFilter, graphql_name='bills')
    bills_not = sgqlc.types.Field(_BillFilter, graphql_name='bills_not')
    bills_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='bills_in')
    bills_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='bills_not_in')
    bills_some = sgqlc.types.Field(_BillFilter, graphql_name='bills_some')
    bills_none = sgqlc.types.Field(_BillFilter, graphql_name='bills_none')
    bills_single = sgqlc.types.Field(_BillFilter, graphql_name='bills_single')
    bills_every = sgqlc.types.Field(_BillFilter, graphql_name='bills_every')
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
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'ndl_id', 'ndl_id_not', 'ndl_id_in', 'ndl_id_not_in', 'ndl_id_contains', 'ndl_id_not_contains', 'ndl_id_starts_with', 'ndl_id_not_starts_with', 'ndl_id_ends_with', 'ndl_id_not_ends_with', 'e_gov_id', 'e_gov_id_not', 'e_gov_id_in', 'e_gov_id_not_in', 'e_gov_id_contains', 'e_gov_id_not_contains', 'e_gov_id_starts_with', 'e_gov_id_not_starts_with', 'e_gov_id_ends_with', 'e_gov_id_not_ends_with', 'e_gov_url', 'e_gov_url_not', 'e_gov_url_in', 'e_gov_url_not_in', 'e_gov_url_contains', 'e_gov_url_not_contains', 'e_gov_url_starts_with', 'e_gov_url_not_starts_with', 'e_gov_url_ends_with', 'e_gov_url_not_ends_with', 'law_title', 'law_title_not', 'law_title_in', 'law_title_not_in', 'law_title_contains', 'law_title_not_contains', 'law_title_starts_with', 'law_title_not_starts_with', 'law_title_ends_with', 'law_title_not_ends_with', 'law_number', 'law_number_not', 'law_number_in', 'law_number_not_in', 'law_number_contains', 'law_number_not_contains', 'law_number_starts_with', 'law_number_not_starts_with', 'law_number_ends_with', 'law_number_not_ends_with', 'discussed_at', 'discussed_at_not', 'discussed_at_in', 'discussed_at_not_in', 'discussed_at_some', 'discussed_at_none', 'discussed_at_single', 'discussed_at_every', 'referenced_by', 'referenced_by_not', 'referenced_by_in', 'referenced_by_not_in', 'referenced_by_some', 'referenced_by_none', 'referenced_by_single', 'referenced_by_every', 'references', 'references_not', 'references_in', 'references_not_in', 'references_some', 'references_none', 'references_single', 'references_every', 'amended_by', 'amended_by_not', 'amended_by_in', 'amended_by_not_in', 'amended_by_some', 'amended_by_none', 'amended_by_single', 'amended_by_every', 'refer_url', 'refer_url_not', 'refer_url_in', 'refer_url_not_in', 'refer_url_some', 'refer_url_none', 'refer_url_single', 'refer_url_every', 'related_time_line', 'related_time_line_not', 'related_time_line_in', 'related_time_line_not_in', 'related_time_line_some', 'related_time_line_none', 'related_time_line_single', 'related_time_line_every')
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
    ndl_id = sgqlc.types.Field(String, graphql_name='ndlId')
    ndl_id_not = sgqlc.types.Field(String, graphql_name='ndlId_not')
    ndl_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ndlId_in')
    ndl_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ndlId_not_in')
    ndl_id_contains = sgqlc.types.Field(String, graphql_name='ndlId_contains')
    ndl_id_not_contains = sgqlc.types.Field(String, graphql_name='ndlId_not_contains')
    ndl_id_starts_with = sgqlc.types.Field(String, graphql_name='ndlId_starts_with')
    ndl_id_not_starts_with = sgqlc.types.Field(String, graphql_name='ndlId_not_starts_with')
    ndl_id_ends_with = sgqlc.types.Field(String, graphql_name='ndlId_ends_with')
    ndl_id_not_ends_with = sgqlc.types.Field(String, graphql_name='ndlId_not_ends_with')
    e_gov_id = sgqlc.types.Field(String, graphql_name='eGovId')
    e_gov_id_not = sgqlc.types.Field(String, graphql_name='eGovId_not')
    e_gov_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='eGovId_in')
    e_gov_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='eGovId_not_in')
    e_gov_id_contains = sgqlc.types.Field(String, graphql_name='eGovId_contains')
    e_gov_id_not_contains = sgqlc.types.Field(String, graphql_name='eGovId_not_contains')
    e_gov_id_starts_with = sgqlc.types.Field(String, graphql_name='eGovId_starts_with')
    e_gov_id_not_starts_with = sgqlc.types.Field(String, graphql_name='eGovId_not_starts_with')
    e_gov_id_ends_with = sgqlc.types.Field(String, graphql_name='eGovId_ends_with')
    e_gov_id_not_ends_with = sgqlc.types.Field(String, graphql_name='eGovId_not_ends_with')
    e_gov_url = sgqlc.types.Field(String, graphql_name='eGovUrl')
    e_gov_url_not = sgqlc.types.Field(String, graphql_name='eGovUrl_not')
    e_gov_url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='eGovUrl_in')
    e_gov_url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='eGovUrl_not_in')
    e_gov_url_contains = sgqlc.types.Field(String, graphql_name='eGovUrl_contains')
    e_gov_url_not_contains = sgqlc.types.Field(String, graphql_name='eGovUrl_not_contains')
    e_gov_url_starts_with = sgqlc.types.Field(String, graphql_name='eGovUrl_starts_with')
    e_gov_url_not_starts_with = sgqlc.types.Field(String, graphql_name='eGovUrl_not_starts_with')
    e_gov_url_ends_with = sgqlc.types.Field(String, graphql_name='eGovUrl_ends_with')
    e_gov_url_not_ends_with = sgqlc.types.Field(String, graphql_name='eGovUrl_not_ends_with')
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
    discussed_at = sgqlc.types.Field('_MinutesFilter', graphql_name='discussedAt')
    discussed_at_not = sgqlc.types.Field('_MinutesFilter', graphql_name='discussedAt_not')
    discussed_at_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='discussedAt_in')
    discussed_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MinutesFilter')), graphql_name='discussedAt_not_in')
    discussed_at_some = sgqlc.types.Field('_MinutesFilter', graphql_name='discussedAt_some')
    discussed_at_none = sgqlc.types.Field('_MinutesFilter', graphql_name='discussedAt_none')
    discussed_at_single = sgqlc.types.Field('_MinutesFilter', graphql_name='discussedAt_single')
    discussed_at_every = sgqlc.types.Field('_MinutesFilter', graphql_name='discussedAt_every')
    referenced_by = sgqlc.types.Field('_LawFilter', graphql_name='referencedBy')
    referenced_by_not = sgqlc.types.Field('_LawFilter', graphql_name='referencedBy_not')
    referenced_by_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_LawFilter')), graphql_name='referencedBy_in')
    referenced_by_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_LawFilter')), graphql_name='referencedBy_not_in')
    referenced_by_some = sgqlc.types.Field('_LawFilter', graphql_name='referencedBy_some')
    referenced_by_none = sgqlc.types.Field('_LawFilter', graphql_name='referencedBy_none')
    referenced_by_single = sgqlc.types.Field('_LawFilter', graphql_name='referencedBy_single')
    referenced_by_every = sgqlc.types.Field('_LawFilter', graphql_name='referencedBy_every')
    references = sgqlc.types.Field('_LawFilter', graphql_name='references')
    references_not = sgqlc.types.Field('_LawFilter', graphql_name='references_not')
    references_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_LawFilter')), graphql_name='references_in')
    references_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_LawFilter')), graphql_name='references_not_in')
    references_some = sgqlc.types.Field('_LawFilter', graphql_name='references_some')
    references_none = sgqlc.types.Field('_LawFilter', graphql_name='references_none')
    references_single = sgqlc.types.Field('_LawFilter', graphql_name='references_single')
    references_every = sgqlc.types.Field('_LawFilter', graphql_name='references_every')
    amended_by = sgqlc.types.Field(_BillFilter, graphql_name='amendedBy')
    amended_by_not = sgqlc.types.Field(_BillFilter, graphql_name='amendedBy_not')
    amended_by_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='amendedBy_in')
    amended_by_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='amendedBy_not_in')
    amended_by_some = sgqlc.types.Field(_BillFilter, graphql_name='amendedBy_some')
    amended_by_none = sgqlc.types.Field(_BillFilter, graphql_name='amendedBy_none')
    amended_by_single = sgqlc.types.Field(_BillFilter, graphql_name='amendedBy_single')
    amended_by_every = sgqlc.types.Field(_BillFilter, graphql_name='amendedBy_every')
    refer_url = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl')
    refer_url_not = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_not')
    refer_url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='referUrl_in')
    refer_url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='referUrl_not_in')
    refer_url_some = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_some')
    refer_url_none = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_none')
    refer_url_single = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_single')
    refer_url_every = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_every')
    related_time_line = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine')
    related_time_line_not = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_not')
    related_time_line_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimelineFilter')), graphql_name='relatedTimeLine_in')
    related_time_line_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimelineFilter')), graphql_name='relatedTimeLine_not_in')
    related_time_line_some = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_some')
    related_time_line_none = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_none')
    related_time_line_single = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_single')
    related_time_line_every = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_every')


class _LawInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _MeetingFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'members', 'members_not', 'members_in', 'members_not_in', 'members_some', 'members_none', 'members_single', 'members_every', 'minutes', 'minutes_not', 'minutes_in', 'minutes_not_in', 'minutes_some', 'minutes_none', 'minutes_single', 'minutes_every')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MeetingFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_MeetingFilter')), graphql_name='OR')
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


class _MeetingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _MemberFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'name', 'name_not', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'first_name', 'first_name_not', 'first_name_in', 'first_name_not_in', 'first_name_contains', 'first_name_not_contains', 'first_name_starts_with', 'first_name_not_starts_with', 'first_name_ends_with', 'first_name_not_ends_with', 'last_name', 'last_name_not', 'last_name_in', 'last_name_not_in', 'last_name_contains', 'last_name_not_contains', 'last_name_starts_with', 'last_name_not_starts_with', 'last_name_ends_with', 'last_name_not_ends_with', 'name_hira', 'name_hira_not', 'name_hira_in', 'name_hira_not_in', 'name_hira_contains', 'name_hira_not_contains', 'name_hira_starts_with', 'name_hira_not_starts_with', 'name_hira_ends_with', 'name_hira_not_ends_with', 'first_name_hira', 'first_name_hira_not', 'first_name_hira_in', 'first_name_hira_not_in', 'first_name_hira_contains', 'first_name_hira_not_contains', 'first_name_hira_starts_with', 'first_name_hira_not_starts_with', 'first_name_hira_ends_with', 'first_name_hira_not_ends_with', 'last_name_hira', 'last_name_hira_not', 'last_name_hira_in', 'last_name_hira_not_in', 'last_name_hira_contains', 'last_name_hira_not_contains', 'last_name_hira_starts_with', 'last_name_hira_not_starts_with', 'last_name_hira_ends_with', 'last_name_hira_not_ends_with', 'current', 'current_not', 'house', 'house_not', 'house_in', 'house_not_in', 'elected_by', 'elected_by_not', 'elected_by_in', 'elected_by_not_in', 'elected_by_some', 'elected_by_none', 'elected_by_single', 'elected_by_every', 'submitted_bills', 'submitted_bills_not', 'submitted_bills_in', 'submitted_bills_not_in', 'submitted_bills_some', 'submitted_bills_none', 'submitted_bills_single', 'submitted_bills_every', 'attended_diets', 'attended_diets_not', 'attended_diets_in', 'attended_diets_not_in', 'attended_diets_some', 'attended_diets_none', 'attended_diets_single', 'attended_diets_every', 'attended_minutes', 'attended_minutes_not', 'attended_minutes_in', 'attended_minutes_not_in', 'attended_minutes_some', 'attended_minutes_none', 'attended_minutes_single', 'attended_minutes_every', 'refer_url', 'refer_url_not', 'refer_url_in', 'refer_url_not_in', 'refer_url_some', 'refer_url_none', 'refer_url_single', 'refer_url_every', 'related_time_line', 'related_time_line_not', 'related_time_line_in', 'related_time_line_not_in', 'related_time_line_some', 'related_time_line_none', 'related_time_line_single', 'related_time_line_every')
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
    current = sgqlc.types.Field(Boolean, graphql_name='current')
    current_not = sgqlc.types.Field(Boolean, graphql_name='current_not')
    house = sgqlc.types.Field(House, graphql_name='house')
    house_not = sgqlc.types.Field(House, graphql_name='house_not')
    house_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(House)), graphql_name='house_in')
    house_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(House)), graphql_name='house_not_in')
    elected_by = sgqlc.types.Field(_ElectionFilter, graphql_name='electedBy')
    elected_by_not = sgqlc.types.Field(_ElectionFilter, graphql_name='electedBy_not')
    elected_by_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_ElectionFilter)), graphql_name='electedBy_in')
    elected_by_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_ElectionFilter)), graphql_name='electedBy_not_in')
    elected_by_some = sgqlc.types.Field(_ElectionFilter, graphql_name='electedBy_some')
    elected_by_none = sgqlc.types.Field(_ElectionFilter, graphql_name='electedBy_none')
    elected_by_single = sgqlc.types.Field(_ElectionFilter, graphql_name='electedBy_single')
    elected_by_every = sgqlc.types.Field(_ElectionFilter, graphql_name='electedBy_every')
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
    refer_url = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl')
    refer_url_not = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_not')
    refer_url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='referUrl_in')
    refer_url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UrlFilter')), graphql_name='referUrl_not_in')
    refer_url_some = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_some')
    refer_url_none = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_none')
    refer_url_single = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_single')
    refer_url_every = sgqlc.types.Field('_UrlFilter', graphql_name='referUrl_every')
    related_time_line = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine')
    related_time_line_not = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_not')
    related_time_line_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimelineFilter')), graphql_name='relatedTimeLine_in')
    related_time_line_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimelineFilter')), graphql_name='relatedTimeLine_not_in')
    related_time_line_some = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_some')
    related_time_line_none = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_none')
    related_time_line_single = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_single')
    related_time_line_every = sgqlc.types.Field('_TimelineFilter', graphql_name='relatedTimeLine_every')


class _MemberInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _MinutesFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'ndl_id', 'ndl_id_not', 'ndl_id_in', 'ndl_id_not_in', 'ndl_id_contains', 'ndl_id_not_contains', 'ndl_id_starts_with', 'ndl_id_not_starts_with', 'ndl_id_ends_with', 'ndl_id_not_ends_with', 'ndl_url', 'ndl_url_not', 'ndl_url_in', 'ndl_url_not_in', 'ndl_url_contains', 'ndl_url_not_contains', 'ndl_url_starts_with', 'ndl_url_not_starts_with', 'ndl_url_ends_with', 'ndl_url_not_ends_with', 'minutes_number', 'minutes_number_not', 'minutes_number_in', 'minutes_number_not_in', 'minutes_number_contains', 'minutes_number_not_contains', 'minutes_number_starts_with', 'minutes_number_not_starts_with', 'minutes_number_ends_with', 'minutes_number_not_ends_with', 'start', 'start_not', 'start_in', 'start_not_in', 'start_lt', 'start_lte', 'start_gt', 'start_gte', 'end', 'end_not', 'end_in', 'end_not_in', 'end_lt', 'end_lte', 'end_gt', 'end_gte', 'meeting', 'meeting_not', 'meeting_in', 'meeting_not_in', 'participants', 'participants_not', 'participants_in', 'participants_not_in', 'participants_some', 'participants_none', 'participants_single', 'participants_every', 'held_at', 'held_at_not', 'held_at_in', 'held_at_not_in', 'discussed_bills', 'discussed_bills_not', 'discussed_bills_in', 'discussed_bills_not_in', 'discussed_bills_some', 'discussed_bills_none', 'discussed_bills_single', 'discussed_bills_every', 'discussed_laws', 'discussed_laws_not', 'discussed_laws_in', 'discussed_laws_not_in', 'discussed_laws_some', 'discussed_laws_none', 'discussed_laws_single', 'discussed_laws_every')
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
    ndl_id = sgqlc.types.Field(String, graphql_name='ndlId')
    ndl_id_not = sgqlc.types.Field(String, graphql_name='ndlId_not')
    ndl_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ndlId_in')
    ndl_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ndlId_not_in')
    ndl_id_contains = sgqlc.types.Field(String, graphql_name='ndlId_contains')
    ndl_id_not_contains = sgqlc.types.Field(String, graphql_name='ndlId_not_contains')
    ndl_id_starts_with = sgqlc.types.Field(String, graphql_name='ndlId_starts_with')
    ndl_id_not_starts_with = sgqlc.types.Field(String, graphql_name='ndlId_not_starts_with')
    ndl_id_ends_with = sgqlc.types.Field(String, graphql_name='ndlId_ends_with')
    ndl_id_not_ends_with = sgqlc.types.Field(String, graphql_name='ndlId_not_ends_with')
    ndl_url = sgqlc.types.Field(String, graphql_name='ndlUrl')
    ndl_url_not = sgqlc.types.Field(String, graphql_name='ndlUrl_not')
    ndl_url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ndlUrl_in')
    ndl_url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ndlUrl_not_in')
    ndl_url_contains = sgqlc.types.Field(String, graphql_name='ndlUrl_contains')
    ndl_url_not_contains = sgqlc.types.Field(String, graphql_name='ndlUrl_not_contains')
    ndl_url_starts_with = sgqlc.types.Field(String, graphql_name='ndlUrl_starts_with')
    ndl_url_not_starts_with = sgqlc.types.Field(String, graphql_name='ndlUrl_not_starts_with')
    ndl_url_ends_with = sgqlc.types.Field(String, graphql_name='ndlUrl_ends_with')
    ndl_url_not_ends_with = sgqlc.types.Field(String, graphql_name='ndlUrl_not_ends_with')
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
    start = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='start')
    start_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='start_not')
    start_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='start_in')
    start_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='start_not_in')
    start_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='start_lt')
    start_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='start_lte')
    start_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='start_gt')
    start_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='start_gte')
    end = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='end')
    end_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='end_not')
    end_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='end_in')
    end_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='end_not_in')
    end_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='end_lt')
    end_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='end_lte')
    end_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='end_gt')
    end_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='end_gte')
    meeting = sgqlc.types.Field(_MeetingFilter, graphql_name='meeting')
    meeting_not = sgqlc.types.Field(_MeetingFilter, graphql_name='meeting_not')
    meeting_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MeetingFilter)), graphql_name='meeting_in')
    meeting_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MeetingFilter)), graphql_name='meeting_not_in')
    participants = sgqlc.types.Field(_MemberFilter, graphql_name='participants')
    participants_not = sgqlc.types.Field(_MemberFilter, graphql_name='participants_not')
    participants_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MemberFilter)), graphql_name='participants_in')
    participants_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MemberFilter)), graphql_name='participants_not_in')
    participants_some = sgqlc.types.Field(_MemberFilter, graphql_name='participants_some')
    participants_none = sgqlc.types.Field(_MemberFilter, graphql_name='participants_none')
    participants_single = sgqlc.types.Field(_MemberFilter, graphql_name='participants_single')
    participants_every = sgqlc.types.Field(_MemberFilter, graphql_name='participants_every')
    held_at = sgqlc.types.Field(_DietFilter, graphql_name='heldAt')
    held_at_not = sgqlc.types.Field(_DietFilter, graphql_name='heldAt_not')
    held_at_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_DietFilter)), graphql_name='heldAt_in')
    held_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_DietFilter)), graphql_name='heldAt_not_in')
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
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'content', 'content_not', 'content_in', 'content_not_in', 'content_contains', 'content_not_contains', 'content_starts_with', 'content_not_starts_with', 'content_ends_with', 'content_not_ends_with', 'started_on', 'started_on_not', 'started_on_in', 'started_on_not_in', 'started_on_lt', 'started_on_lte', 'started_on_gt', 'started_on_gte', 'relating_bills', 'relating_bills_not', 'relating_bills_in', 'relating_bills_not_in', 'relating_bills_some', 'relating_bills_none', 'relating_bills_single', 'relating_bills_every', 'relating_laws', 'relating_laws_not', 'relating_laws_in', 'relating_laws_not_in', 'relating_laws_some', 'relating_laws_none', 'relating_laws_single', 'relating_laws_every', 'relating_members', 'relating_members_not', 'relating_members_in', 'relating_members_not_in', 'relating_members_some', 'relating_members_none', 'relating_members_single', 'relating_members_every')
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
    started_on = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='startedOn')
    started_on_not = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='startedOn_not')
    started_on_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='startedOn_in')
    started_on_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='startedOn_not_in')
    started_on_lt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='startedOn_lt')
    started_on_lte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='startedOn_lte')
    started_on_gt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='startedOn_gt')
    started_on_gte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='startedOn_gte')
    relating_bills = sgqlc.types.Field(_BillFilter, graphql_name='relatingBills')
    relating_bills_not = sgqlc.types.Field(_BillFilter, graphql_name='relatingBills_not')
    relating_bills_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='relatingBills_in')
    relating_bills_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='relatingBills_not_in')
    relating_bills_some = sgqlc.types.Field(_BillFilter, graphql_name='relatingBills_some')
    relating_bills_none = sgqlc.types.Field(_BillFilter, graphql_name='relatingBills_none')
    relating_bills_single = sgqlc.types.Field(_BillFilter, graphql_name='relatingBills_single')
    relating_bills_every = sgqlc.types.Field(_BillFilter, graphql_name='relatingBills_every')
    relating_laws = sgqlc.types.Field(_LawFilter, graphql_name='relatingLaws')
    relating_laws_not = sgqlc.types.Field(_LawFilter, graphql_name='relatingLaws_not')
    relating_laws_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_LawFilter)), graphql_name='relatingLaws_in')
    relating_laws_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_LawFilter)), graphql_name='relatingLaws_not_in')
    relating_laws_some = sgqlc.types.Field(_LawFilter, graphql_name='relatingLaws_some')
    relating_laws_none = sgqlc.types.Field(_LawFilter, graphql_name='relatingLaws_none')
    relating_laws_single = sgqlc.types.Field(_LawFilter, graphql_name='relatingLaws_single')
    relating_laws_every = sgqlc.types.Field(_LawFilter, graphql_name='relatingLaws_every')
    relating_members = sgqlc.types.Field(_MemberFilter, graphql_name='relatingMembers')
    relating_members_not = sgqlc.types.Field(_MemberFilter, graphql_name='relatingMembers_not')
    relating_members_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MemberFilter)), graphql_name='relatingMembers_in')
    relating_members_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_MemberFilter)), graphql_name='relatingMembers_not_in')
    relating_members_some = sgqlc.types.Field(_MemberFilter, graphql_name='relatingMembers_some')
    relating_members_none = sgqlc.types.Field(_MemberFilter, graphql_name='relatingMembers_none')
    relating_members_single = sgqlc.types.Field(_MemberFilter, graphql_name='relatingMembers_single')
    relating_members_every = sgqlc.types.Field(_MemberFilter, graphql_name='relatingMembers_every')


class _TimelineInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class _UrlFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'id_starts_with', 'id_not_starts_with', 'id_ends_with', 'id_not_ends_with', 'url', 'url_not', 'url_in', 'url_not_in', 'url_contains', 'url_not_contains', 'url_starts_with', 'url_not_starts_with', 'url_ends_with', 'url_not_ends_with', 'text', 'text_not', 'text_in', 'text_not_in', 'text_contains', 'text_not_contains', 'text_starts_with', 'text_not_starts_with', 'text_ends_with', 'text_not_ends_with', 'type', 'type_not', 'type_in', 'type_not_in', 'type_contains', 'type_not_contains', 'type_starts_with', 'type_not_starts_with', 'type_ends_with', 'type_not_ends_with', 'domain', 'domain_not', 'domain_in', 'domain_not_in', 'domain_contains', 'domain_not_contains', 'domain_starts_with', 'domain_not_starts_with', 'domain_ends_with', 'domain_not_ends_with', 'accessed_on', 'accessed_on_not', 'accessed_on_in', 'accessed_on_not_in', 'accessed_on_lt', 'accessed_on_lte', 'accessed_on_gt', 'accessed_on_gte', 'referred_bills', 'referred_bills_not', 'referred_bills_in', 'referred_bills_not_in', 'referred_bills_some', 'referred_bills_none', 'referred_bills_single', 'referred_bills_every', 'referred_laws', 'referred_laws_not', 'referred_laws_in', 'referred_laws_not_in', 'referred_laws_some', 'referred_laws_none', 'referred_laws_single', 'referred_laws_every', 'referred_members', 'referred_members_not', 'referred_members_in', 'referred_members_not_in', 'referred_members_some', 'referred_members_none', 'referred_members_single', 'referred_members_every')
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
    text = sgqlc.types.Field(String, graphql_name='text')
    text_not = sgqlc.types.Field(String, graphql_name='text_not')
    text_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='text_in')
    text_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='text_not_in')
    text_contains = sgqlc.types.Field(String, graphql_name='text_contains')
    text_not_contains = sgqlc.types.Field(String, graphql_name='text_not_contains')
    text_starts_with = sgqlc.types.Field(String, graphql_name='text_starts_with')
    text_not_starts_with = sgqlc.types.Field(String, graphql_name='text_not_starts_with')
    text_ends_with = sgqlc.types.Field(String, graphql_name='text_ends_with')
    text_not_ends_with = sgqlc.types.Field(String, graphql_name='text_not_ends_with')
    type = sgqlc.types.Field(String, graphql_name='type')
    type_not = sgqlc.types.Field(String, graphql_name='type_not')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='type_not_in')
    type_contains = sgqlc.types.Field(String, graphql_name='type_contains')
    type_not_contains = sgqlc.types.Field(String, graphql_name='type_not_contains')
    type_starts_with = sgqlc.types.Field(String, graphql_name='type_starts_with')
    type_not_starts_with = sgqlc.types.Field(String, graphql_name='type_not_starts_with')
    type_ends_with = sgqlc.types.Field(String, graphql_name='type_ends_with')
    type_not_ends_with = sgqlc.types.Field(String, graphql_name='type_not_ends_with')
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
    accessed_on = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='accessedOn')
    accessed_on_not = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='accessedOn_not')
    accessed_on_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='accessedOn_in')
    accessed_on_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='accessedOn_not_in')
    accessed_on_lt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='accessedOn_lt')
    accessed_on_lte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='accessedOn_lte')
    accessed_on_gt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='accessedOn_gt')
    accessed_on_gte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='accessedOn_gte')
    referred_bills = sgqlc.types.Field(_BillFilter, graphql_name='referredBills')
    referred_bills_not = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_not')
    referred_bills_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='referredBills_in')
    referred_bills_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='referredBills_not_in')
    referred_bills_some = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_some')
    referred_bills_none = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_none')
    referred_bills_single = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_single')
    referred_bills_every = sgqlc.types.Field(_BillFilter, graphql_name='referredBills_every')
    referred_laws = sgqlc.types.Field(_BillFilter, graphql_name='referredLaws')
    referred_laws_not = sgqlc.types.Field(_BillFilter, graphql_name='referredLaws_not')
    referred_laws_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='referredLaws_in')
    referred_laws_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='referredLaws_not_in')
    referred_laws_some = sgqlc.types.Field(_BillFilter, graphql_name='referredLaws_some')
    referred_laws_none = sgqlc.types.Field(_BillFilter, graphql_name='referredLaws_none')
    referred_laws_single = sgqlc.types.Field(_BillFilter, graphql_name='referredLaws_single')
    referred_laws_every = sgqlc.types.Field(_BillFilter, graphql_name='referredLaws_every')
    referred_members = sgqlc.types.Field(_BillFilter, graphql_name='referredMembers')
    referred_members_not = sgqlc.types.Field(_BillFilter, graphql_name='referredMembers_not')
    referred_members_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='referredMembers_in')
    referred_members_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BillFilter)), graphql_name='referredMembers_not_in')
    referred_members_some = sgqlc.types.Field(_BillFilter, graphql_name='referredMembers_some')
    referred_members_none = sgqlc.types.Field(_BillFilter, graphql_name='referredMembers_none')
    referred_members_single = sgqlc.types.Field(_BillFilter, graphql_name='referredMembers_single')
    referred_members_every = sgqlc.types.Field(_BillFilter, graphql_name='referredMembers_every')


class _UrlInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')



########################################################################
# Output Objects and Interfaces
########################################################################
class Bill(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'ndl_id', 'ndl_url', 'bill_title', 'bill_number', 'bill_category', 'bill_type', 'bill_status', 'submitted_by', 'submitted_to', 'discussed_at', 'ammends', 'syugiin_url', 'sangiin_url', 'overview_url', 'essential_url', 'comparison_url', 'pull_request_url', 'refer_url', 'related_time_line', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ndl_id = sgqlc.types.Field(String, graphql_name='ndlId')
    ndl_url = sgqlc.types.Field(String, graphql_name='ndlUrl')
    bill_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='billTitle')
    bill_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='billNumber')
    bill_category = sgqlc.types.Field(sgqlc.types.non_null(BillCategory), graphql_name='billCategory')
    bill_type = sgqlc.types.Field(sgqlc.types.non_null(BillType), graphql_name='billType')
    bill_status = sgqlc.types.Field(sgqlc.types.non_null(BillStatus), graphql_name='billStatus')
    submitted_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Member'))), graphql_name='submittedBy', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MemberOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MemberFilter, graphql_name='filter', default=None)),
))
    )
    submitted_to = sgqlc.types.Field(sgqlc.types.non_null('Diet'), graphql_name='submittedTo', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_DietFilter, graphql_name='filter', default=None)),
))
    )
    discussed_at = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Minutes'))), graphql_name='discussedAt', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MinutesOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MinutesFilter, graphql_name='filter', default=None)),
))
    )
    ammends = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Law'))), graphql_name='ammends', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_LawOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_LawFilter, graphql_name='filter', default=None)),
))
    )
    syugiin_url = sgqlc.types.Field(String, graphql_name='syugiinUrl')
    sangiin_url = sgqlc.types.Field(String, graphql_name='sangiinUrl')
    overview_url = sgqlc.types.Field(String, graphql_name='overviewUrl')
    essential_url = sgqlc.types.Field(String, graphql_name='essentialUrl')
    comparison_url = sgqlc.types.Field(String, graphql_name='comparisonUrl')
    pull_request_url = sgqlc.types.Field(String, graphql_name='pullRequestUrl')
    refer_url = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Url')), graphql_name='referUrl', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UrlOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UrlFilter, graphql_name='filter', default=None)),
))
    )
    related_time_line = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Timeline')), graphql_name='relatedTimeLine', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_TimelineOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_TimelineFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Diet(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'number', 'name', 'start_date', 'end_date', 'bills', 'minutes', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    start_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='startDate')
    end_date = sgqlc.types.Field('_Neo4jDateTime', graphql_name='endDate')
    bills = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bill))), graphql_name='bills', args=sgqlc.types.ArgDict((
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
    __field_names__ = ('id', 'ndl_id', 'e_gov_id', 'e_gov_url', 'law_title', 'law_number', 'discussed_at', 'referenced_by', 'references', 'amended_by', 'refer_url', 'related_time_line', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ndl_id = sgqlc.types.Field(String, graphql_name='ndlId')
    e_gov_id = sgqlc.types.Field(String, graphql_name='eGovId')
    e_gov_url = sgqlc.types.Field(String, graphql_name='eGovUrl')
    law_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lawTitle')
    law_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lawNumber')
    discussed_at = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Minutes'))), graphql_name='discussedAt', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MinutesOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MinutesFilter, graphql_name='filter', default=None)),
))
    )
    referenced_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Law'))), graphql_name='referencedBy', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_LawOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_LawFilter, graphql_name='filter', default=None)),
))
    )
    references = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Law'))), graphql_name='references', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_LawOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_LawFilter, graphql_name='filter', default=None)),
))
    )
    amended_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bill))), graphql_name='amendedBy', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    refer_url = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Url')), graphql_name='referUrl', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UrlOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UrlFilter, graphql_name='filter', default=None)),
))
    )
    related_time_line = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Timeline')), graphql_name='relatedTimeLine', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_TimelineOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_TimelineFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Meeting(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'members', 'minutes', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
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


class Member(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'first_name', 'last_name', 'name_hira', 'first_name_hira', 'last_name_hira', 'current', 'house', 'elected_by', 'submitted_bills', 'attended_diets', 'attended_minutes', 'refer_url', 'related_time_line', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    name_hira = sgqlc.types.Field(String, graphql_name='nameHira')
    first_name_hira = sgqlc.types.Field(String, graphql_name='firstNameHira')
    last_name_hira = sgqlc.types.Field(String, graphql_name='lastNameHira')
    current = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='current')
    house = sgqlc.types.Field(sgqlc.types.non_null(House), graphql_name='house')
    elected_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Election))), graphql_name='electedBy', args=sgqlc.types.ArgDict((
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
    refer_url = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Url')), graphql_name='referUrl', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UrlOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UrlFilter, graphql_name='filter', default=None)),
))
    )
    related_time_line = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Timeline')), graphql_name='relatedTimeLine', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_TimelineOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_TimelineFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Minutes(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'ndl_id', 'ndl_url', 'minutes_number', 'start', 'end', 'meeting', 'participants', 'held_at', 'topics', 'discussed_bills', 'discussed_laws', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ndl_id = sgqlc.types.Field(String, graphql_name='ndlId')
    ndl_url = sgqlc.types.Field(String, graphql_name='ndlUrl')
    minutes_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='minutesNumber')
    start = sgqlc.types.Field('_Neo4jDateTime', graphql_name='start')
    end = sgqlc.types.Field('_Neo4jDateTime', graphql_name='end')
    meeting = sgqlc.types.Field(Meeting, graphql_name='meeting', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_MeetingFilter, graphql_name='filter', default=None)),
))
    )
    participants = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Member))), graphql_name='participants', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MemberOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MemberFilter, graphql_name='filter', default=None)),
))
    )
    held_at = sgqlc.types.Field(Diet, graphql_name='heldAt', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_DietFilter, graphql_name='filter', default=None)),
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
    __field_names__ = ('add_member_elected_by', 'remove_member_elected_by', 'merge_member_elected_by', 'add_member_submitted_bills', 'remove_member_submitted_bills', 'merge_member_submitted_bills', 'add_member_attended_diets', 'remove_member_attended_diets', 'merge_member_attended_diets', 'add_member_attended_minutes', 'remove_member_attended_minutes', 'merge_member_attended_minutes', 'add_member_refer_url', 'remove_member_refer_url', 'merge_member_refer_url', 'add_member_related_time_line', 'remove_member_related_time_line', 'merge_member_related_time_line', 'create_member', 'update_member', 'delete_member', 'merge_member', 'add_election_elected_members', 'remove_election_elected_members', 'merge_election_elected_members', 'create_election', 'update_election', 'delete_election', 'merge_election', 'add_diet_bills', 'remove_diet_bills', 'merge_diet_bills', 'add_diet_minutes', 'remove_diet_minutes', 'merge_diet_minutes', 'create_diet', 'update_diet', 'delete_diet', 'merge_diet', 'add_law_discussed_at', 'remove_law_discussed_at', 'merge_law_discussed_at', 'add_law_referenced_by', 'remove_law_referenced_by', 'merge_law_referenced_by', 'add_law_references', 'remove_law_references', 'merge_law_references', 'add_law_amended_by', 'remove_law_amended_by', 'merge_law_amended_by', 'add_law_refer_url', 'remove_law_refer_url', 'merge_law_refer_url', 'add_law_related_time_line', 'remove_law_related_time_line', 'merge_law_related_time_line', 'create_law', 'update_law', 'delete_law', 'merge_law', 'add_bill_submitted_by', 'remove_bill_submitted_by', 'merge_bill_submitted_by', 'add_bill_submitted_to', 'remove_bill_submitted_to', 'merge_bill_submitted_to', 'add_bill_discussed_at', 'remove_bill_discussed_at', 'merge_bill_discussed_at', 'add_bill_ammends', 'remove_bill_ammends', 'merge_bill_ammends', 'add_bill_refer_url', 'remove_bill_refer_url', 'merge_bill_refer_url', 'add_bill_related_time_line', 'remove_bill_related_time_line', 'merge_bill_related_time_line', 'create_bill', 'update_bill', 'delete_bill', 'merge_bill', 'add_meeting_members', 'remove_meeting_members', 'merge_meeting_members', 'add_meeting_minutes', 'remove_meeting_minutes', 'merge_meeting_minutes', 'create_meeting', 'update_meeting', 'delete_meeting', 'merge_meeting', 'add_minutes_meeting', 'remove_minutes_meeting', 'merge_minutes_meeting', 'add_minutes_participants', 'remove_minutes_participants', 'merge_minutes_participants', 'add_minutes_held_at', 'remove_minutes_held_at', 'merge_minutes_held_at', 'add_minutes_discussed_bills', 'remove_minutes_discussed_bills', 'merge_minutes_discussed_bills', 'add_minutes_discussed_laws', 'remove_minutes_discussed_laws', 'merge_minutes_discussed_laws', 'create_minutes', 'update_minutes', 'delete_minutes', 'merge_minutes', 'add_url_referred_bills', 'remove_url_referred_bills', 'merge_url_referred_bills', 'add_url_referred_laws', 'remove_url_referred_laws', 'merge_url_referred_laws', 'add_url_referred_members', 'remove_url_referred_members', 'merge_url_referred_members', 'create_url', 'update_url', 'delete_url', 'merge_url', 'add_timeline_relating_bills', 'remove_timeline_relating_bills', 'merge_timeline_relating_bills', 'add_timeline_relating_laws', 'remove_timeline_relating_laws', 'merge_timeline_relating_laws', 'add_timeline_relating_members', 'remove_timeline_relating_members', 'merge_timeline_relating_members', 'create_timeline', 'update_timeline', 'delete_timeline', 'merge_timeline')
    add_member_elected_by = sgqlc.types.Field('_AddMemberElectedByPayload', graphql_name='AddMemberElectedBy', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    remove_member_elected_by = sgqlc.types.Field('_RemoveMemberElectedByPayload', graphql_name='RemoveMemberElectedBy', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_ElectionInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='to', default=None)),
))
    )
    merge_member_elected_by = sgqlc.types.Field('_MergeMemberElectedByPayload', graphql_name='MergeMemberElectedBy', args=sgqlc.types.ArgDict((
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
    add_member_refer_url = sgqlc.types.Field('_AddMemberReferUrlPayload', graphql_name='AddMemberReferUrl', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    remove_member_refer_url = sgqlc.types.Field('_RemoveMemberReferUrlPayload', graphql_name='RemoveMemberReferUrl', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    merge_member_refer_url = sgqlc.types.Field('_MergeMemberReferUrlPayload', graphql_name='MergeMemberReferUrl', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    add_member_related_time_line = sgqlc.types.Field('_AddMemberRelatedTimeLinePayload', graphql_name='AddMemberRelatedTimeLine', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    remove_member_related_time_line = sgqlc.types.Field('_RemoveMemberRelatedTimeLinePayload', graphql_name='RemoveMemberRelatedTimeLine', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    merge_member_related_time_line = sgqlc.types.Field('_MergeMemberRelatedTimeLinePayload', graphql_name='MergeMemberRelatedTimeLine', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    create_member = sgqlc.types.Field(Member, graphql_name='CreateMember', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
        ('name_hira', sgqlc.types.Arg(String, graphql_name='nameHira', default=None)),
        ('first_name_hira', sgqlc.types.Arg(String, graphql_name='firstNameHira', default=None)),
        ('last_name_hira', sgqlc.types.Arg(String, graphql_name='lastNameHira', default=None)),
        ('current', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='current', default=None)),
        ('house', sgqlc.types.Arg(sgqlc.types.non_null(House), graphql_name='house', default=None)),
))
    )
    update_member = sgqlc.types.Field(Member, graphql_name='UpdateMember', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
        ('name_hira', sgqlc.types.Arg(String, graphql_name='nameHira', default=None)),
        ('first_name_hira', sgqlc.types.Arg(String, graphql_name='firstNameHira', default=None)),
        ('last_name_hira', sgqlc.types.Arg(String, graphql_name='lastNameHira', default=None)),
        ('current', sgqlc.types.Arg(Boolean, graphql_name='current', default=None)),
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
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
        ('name_hira', sgqlc.types.Arg(String, graphql_name='nameHira', default=None)),
        ('first_name_hira', sgqlc.types.Arg(String, graphql_name='firstNameHira', default=None)),
        ('last_name_hira', sgqlc.types.Arg(String, graphql_name='lastNameHira', default=None)),
        ('current', sgqlc.types.Arg(Boolean, graphql_name='current', default=None)),
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
    add_diet_bills = sgqlc.types.Field('_AddDietBillsPayload', graphql_name='AddDietBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    remove_diet_bills = sgqlc.types.Field('_RemoveDietBillsPayload', graphql_name='RemoveDietBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    merge_diet_bills = sgqlc.types.Field('_MergeDietBillsPayload', graphql_name='MergeDietBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
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
    add_law_discussed_at = sgqlc.types.Field('_AddLawDiscussedAtPayload', graphql_name='AddLawDiscussedAt', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    remove_law_discussed_at = sgqlc.types.Field('_RemoveLawDiscussedAtPayload', graphql_name='RemoveLawDiscussedAt', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    merge_law_discussed_at = sgqlc.types.Field('_MergeLawDiscussedAtPayload', graphql_name='MergeLawDiscussedAt', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    add_law_referenced_by = sgqlc.types.Field('_AddLawReferencedByPayload', graphql_name='AddLawReferencedBy', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    remove_law_referenced_by = sgqlc.types.Field('_RemoveLawReferencedByPayload', graphql_name='RemoveLawReferencedBy', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    merge_law_referenced_by = sgqlc.types.Field('_MergeLawReferencedByPayload', graphql_name='MergeLawReferencedBy', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    add_law_references = sgqlc.types.Field('_AddLawReferencesPayload', graphql_name='AddLawReferences', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    remove_law_references = sgqlc.types.Field('_RemoveLawReferencesPayload', graphql_name='RemoveLawReferences', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    merge_law_references = sgqlc.types.Field('_MergeLawReferencesPayload', graphql_name='MergeLawReferences', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='to', default=None)),
))
    )
    add_law_amended_by = sgqlc.types.Field('_AddLawAmendedByPayload', graphql_name='AddLawAmendedBy', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_law_amended_by = sgqlc.types.Field('_RemoveLawAmendedByPayload', graphql_name='RemoveLawAmendedBy', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_law_amended_by = sgqlc.types.Field('_MergeLawAmendedByPayload', graphql_name='MergeLawAmendedBy', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    add_law_refer_url = sgqlc.types.Field('_AddLawReferUrlPayload', graphql_name='AddLawReferUrl', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    remove_law_refer_url = sgqlc.types.Field('_RemoveLawReferUrlPayload', graphql_name='RemoveLawReferUrl', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    merge_law_refer_url = sgqlc.types.Field('_MergeLawReferUrlPayload', graphql_name='MergeLawReferUrl', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    add_law_related_time_line = sgqlc.types.Field('_AddLawRelatedTimeLinePayload', graphql_name='AddLawRelatedTimeLine', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    remove_law_related_time_line = sgqlc.types.Field('_RemoveLawRelatedTimeLinePayload', graphql_name='RemoveLawRelatedTimeLine', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    merge_law_related_time_line = sgqlc.types.Field('_MergeLawRelatedTimeLinePayload', graphql_name='MergeLawRelatedTimeLine', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    create_law = sgqlc.types.Field(Law, graphql_name='CreateLaw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('ndl_id', sgqlc.types.Arg(String, graphql_name='ndlId', default=None)),
        ('e_gov_id', sgqlc.types.Arg(String, graphql_name='eGovId', default=None)),
        ('e_gov_url', sgqlc.types.Arg(String, graphql_name='eGovUrl', default=None)),
        ('law_title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='lawTitle', default=None)),
        ('law_number', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='lawNumber', default=None)),
))
    )
    update_law = sgqlc.types.Field(Law, graphql_name='UpdateLaw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('ndl_id', sgqlc.types.Arg(String, graphql_name='ndlId', default=None)),
        ('e_gov_id', sgqlc.types.Arg(String, graphql_name='eGovId', default=None)),
        ('e_gov_url', sgqlc.types.Arg(String, graphql_name='eGovUrl', default=None)),
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
        ('ndl_id', sgqlc.types.Arg(String, graphql_name='ndlId', default=None)),
        ('e_gov_id', sgqlc.types.Arg(String, graphql_name='eGovId', default=None)),
        ('e_gov_url', sgqlc.types.Arg(String, graphql_name='eGovUrl', default=None)),
        ('law_title', sgqlc.types.Arg(String, graphql_name='lawTitle', default=None)),
        ('law_number', sgqlc.types.Arg(String, graphql_name='lawNumber', default=None)),
))
    )
    add_bill_submitted_by = sgqlc.types.Field('_AddBillSubmittedByPayload', graphql_name='AddBillSubmittedBy', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_bill_submitted_by = sgqlc.types.Field('_RemoveBillSubmittedByPayload', graphql_name='RemoveBillSubmittedBy', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_bill_submitted_by = sgqlc.types.Field('_MergeBillSubmittedByPayload', graphql_name='MergeBillSubmittedBy', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    add_bill_submitted_to = sgqlc.types.Field('_AddBillSubmittedToPayload', graphql_name='AddBillSubmittedTo', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    remove_bill_submitted_to = sgqlc.types.Field('_RemoveBillSubmittedToPayload', graphql_name='RemoveBillSubmittedTo', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    merge_bill_submitted_to = sgqlc.types.Field('_MergeBillSubmittedToPayload', graphql_name='MergeBillSubmittedTo', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    add_bill_discussed_at = sgqlc.types.Field('_AddBillDiscussedAtPayload', graphql_name='AddBillDiscussedAt', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_bill_discussed_at = sgqlc.types.Field('_RemoveBillDiscussedAtPayload', graphql_name='RemoveBillDiscussedAt', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_bill_discussed_at = sgqlc.types.Field('_MergeBillDiscussedAtPayload', graphql_name='MergeBillDiscussedAt', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    add_bill_ammends = sgqlc.types.Field('_AddBillAmmendsPayload', graphql_name='AddBillAmmends', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    remove_bill_ammends = sgqlc.types.Field('_RemoveBillAmmendsPayload', graphql_name='RemoveBillAmmends', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    merge_bill_ammends = sgqlc.types.Field('_MergeBillAmmendsPayload', graphql_name='MergeBillAmmends', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='to', default=None)),
))
    )
    add_bill_refer_url = sgqlc.types.Field('_AddBillReferUrlPayload', graphql_name='AddBillReferUrl', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    remove_bill_refer_url = sgqlc.types.Field('_RemoveBillReferUrlPayload', graphql_name='RemoveBillReferUrl', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    merge_bill_refer_url = sgqlc.types.Field('_MergeBillReferUrlPayload', graphql_name='MergeBillReferUrl', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    add_bill_related_time_line = sgqlc.types.Field('_AddBillRelatedTimeLinePayload', graphql_name='AddBillRelatedTimeLine', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    remove_bill_related_time_line = sgqlc.types.Field('_RemoveBillRelatedTimeLinePayload', graphql_name='RemoveBillRelatedTimeLine', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    merge_bill_related_time_line = sgqlc.types.Field('_MergeBillRelatedTimeLinePayload', graphql_name='MergeBillRelatedTimeLine', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    create_bill = sgqlc.types.Field(Bill, graphql_name='CreateBill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('ndl_id', sgqlc.types.Arg(String, graphql_name='ndlId', default=None)),
        ('ndl_url', sgqlc.types.Arg(String, graphql_name='ndlUrl', default=None)),
        ('bill_title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='billTitle', default=None)),
        ('bill_number', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='billNumber', default=None)),
        ('bill_category', sgqlc.types.Arg(sgqlc.types.non_null(BillCategory), graphql_name='billCategory', default=None)),
        ('bill_type', sgqlc.types.Arg(sgqlc.types.non_null(BillType), graphql_name='billType', default=None)),
        ('bill_status', sgqlc.types.Arg(sgqlc.types.non_null(BillStatus), graphql_name='billStatus', default=None)),
        ('syugiin_url', sgqlc.types.Arg(String, graphql_name='syugiinUrl', default=None)),
        ('sangiin_url', sgqlc.types.Arg(String, graphql_name='sangiinUrl', default=None)),
        ('overview_url', sgqlc.types.Arg(String, graphql_name='overviewUrl', default=None)),
        ('essential_url', sgqlc.types.Arg(String, graphql_name='essentialUrl', default=None)),
        ('comparison_url', sgqlc.types.Arg(String, graphql_name='comparisonUrl', default=None)),
        ('pull_request_url', sgqlc.types.Arg(String, graphql_name='pullRequestUrl', default=None)),
))
    )
    update_bill = sgqlc.types.Field(Bill, graphql_name='UpdateBill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('ndl_id', sgqlc.types.Arg(String, graphql_name='ndlId', default=None)),
        ('ndl_url', sgqlc.types.Arg(String, graphql_name='ndlUrl', default=None)),
        ('bill_title', sgqlc.types.Arg(String, graphql_name='billTitle', default=None)),
        ('bill_number', sgqlc.types.Arg(String, graphql_name='billNumber', default=None)),
        ('bill_category', sgqlc.types.Arg(BillCategory, graphql_name='billCategory', default=None)),
        ('bill_type', sgqlc.types.Arg(BillType, graphql_name='billType', default=None)),
        ('bill_status', sgqlc.types.Arg(BillStatus, graphql_name='billStatus', default=None)),
        ('syugiin_url', sgqlc.types.Arg(String, graphql_name='syugiinUrl', default=None)),
        ('sangiin_url', sgqlc.types.Arg(String, graphql_name='sangiinUrl', default=None)),
        ('overview_url', sgqlc.types.Arg(String, graphql_name='overviewUrl', default=None)),
        ('essential_url', sgqlc.types.Arg(String, graphql_name='essentialUrl', default=None)),
        ('comparison_url', sgqlc.types.Arg(String, graphql_name='comparisonUrl', default=None)),
        ('pull_request_url', sgqlc.types.Arg(String, graphql_name='pullRequestUrl', default=None)),
))
    )
    delete_bill = sgqlc.types.Field(Bill, graphql_name='DeleteBill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_bill = sgqlc.types.Field(Bill, graphql_name='MergeBill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('ndl_id', sgqlc.types.Arg(String, graphql_name='ndlId', default=None)),
        ('ndl_url', sgqlc.types.Arg(String, graphql_name='ndlUrl', default=None)),
        ('bill_title', sgqlc.types.Arg(String, graphql_name='billTitle', default=None)),
        ('bill_number', sgqlc.types.Arg(String, graphql_name='billNumber', default=None)),
        ('bill_category', sgqlc.types.Arg(BillCategory, graphql_name='billCategory', default=None)),
        ('bill_type', sgqlc.types.Arg(BillType, graphql_name='billType', default=None)),
        ('bill_status', sgqlc.types.Arg(BillStatus, graphql_name='billStatus', default=None)),
        ('syugiin_url', sgqlc.types.Arg(String, graphql_name='syugiinUrl', default=None)),
        ('sangiin_url', sgqlc.types.Arg(String, graphql_name='sangiinUrl', default=None)),
        ('overview_url', sgqlc.types.Arg(String, graphql_name='overviewUrl', default=None)),
        ('essential_url', sgqlc.types.Arg(String, graphql_name='essentialUrl', default=None)),
        ('comparison_url', sgqlc.types.Arg(String, graphql_name='comparisonUrl', default=None)),
        ('pull_request_url', sgqlc.types.Arg(String, graphql_name='pullRequestUrl', default=None)),
))
    )
    add_meeting_members = sgqlc.types.Field('_AddMeetingMembersPayload', graphql_name='AddMeetingMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MeetingInput), graphql_name='to', default=None)),
))
    )
    remove_meeting_members = sgqlc.types.Field('_RemoveMeetingMembersPayload', graphql_name='RemoveMeetingMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MeetingInput), graphql_name='to', default=None)),
))
    )
    merge_meeting_members = sgqlc.types.Field('_MergeMeetingMembersPayload', graphql_name='MergeMeetingMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MeetingInput), graphql_name='to', default=None)),
))
    )
    add_meeting_minutes = sgqlc.types.Field('_AddMeetingMinutesPayload', graphql_name='AddMeetingMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MeetingInput), graphql_name='to', default=None)),
))
    )
    remove_meeting_minutes = sgqlc.types.Field('_RemoveMeetingMinutesPayload', graphql_name='RemoveMeetingMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MeetingInput), graphql_name='to', default=None)),
))
    )
    merge_meeting_minutes = sgqlc.types.Field('_MergeMeetingMinutesPayload', graphql_name='MergeMeetingMinutes', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MeetingInput), graphql_name='to', default=None)),
))
    )
    create_meeting = sgqlc.types.Field(Meeting, graphql_name='CreateMeeting', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    update_meeting = sgqlc.types.Field(Meeting, graphql_name='UpdateMeeting', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    delete_meeting = sgqlc.types.Field(Meeting, graphql_name='DeleteMeeting', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_meeting = sgqlc.types.Field(Meeting, graphql_name='MergeMeeting', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    add_minutes_meeting = sgqlc.types.Field('_AddMinutesMeetingPayload', graphql_name='AddMinutesMeeting', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MeetingInput), graphql_name='to', default=None)),
))
    )
    remove_minutes_meeting = sgqlc.types.Field('_RemoveMinutesMeetingPayload', graphql_name='RemoveMinutesMeeting', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MeetingInput), graphql_name='to', default=None)),
))
    )
    merge_minutes_meeting = sgqlc.types.Field('_MergeMinutesMeetingPayload', graphql_name='MergeMinutesMeeting', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MeetingInput), graphql_name='to', default=None)),
))
    )
    add_minutes_participants = sgqlc.types.Field('_AddMinutesParticipantsPayload', graphql_name='AddMinutesParticipants', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    remove_minutes_participants = sgqlc.types.Field('_RemoveMinutesParticipantsPayload', graphql_name='RemoveMinutesParticipants', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    merge_minutes_participants = sgqlc.types.Field('_MergeMinutesParticipantsPayload', graphql_name='MergeMinutesParticipants', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='to', default=None)),
))
    )
    add_minutes_held_at = sgqlc.types.Field('_AddMinutesHeldAtPayload', graphql_name='AddMinutesHeldAt', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    remove_minutes_held_at = sgqlc.types.Field('_RemoveMinutesHeldAtPayload', graphql_name='RemoveMinutesHeldAt', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
))
    )
    merge_minutes_held_at = sgqlc.types.Field('_MergeMinutesHeldAtPayload', graphql_name='MergeMinutesHeldAt', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MinutesInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_DietInput), graphql_name='to', default=None)),
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
        ('ndl_id', sgqlc.types.Arg(String, graphql_name='ndlId', default=None)),
        ('ndl_url', sgqlc.types.Arg(String, graphql_name='ndlUrl', default=None)),
        ('minutes_number', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='minutesNumber', default=None)),
        ('start', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='end', default=None)),
        ('topics', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='topics', default=None)),
))
    )
    update_minutes = sgqlc.types.Field(Minutes, graphql_name='UpdateMinutes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('ndl_id', sgqlc.types.Arg(String, graphql_name='ndlId', default=None)),
        ('ndl_url', sgqlc.types.Arg(String, graphql_name='ndlUrl', default=None)),
        ('minutes_number', sgqlc.types.Arg(String, graphql_name='minutesNumber', default=None)),
        ('start', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='end', default=None)),
        ('topics', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='topics', default=None)),
))
    )
    delete_minutes = sgqlc.types.Field(Minutes, graphql_name='DeleteMinutes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_minutes = sgqlc.types.Field(Minutes, graphql_name='MergeMinutes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('ndl_id', sgqlc.types.Arg(String, graphql_name='ndlId', default=None)),
        ('ndl_url', sgqlc.types.Arg(String, graphql_name='ndlUrl', default=None)),
        ('minutes_number', sgqlc.types.Arg(String, graphql_name='minutesNumber', default=None)),
        ('start', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='end', default=None)),
        ('topics', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='topics', default=None)),
))
    )
    add_url_referred_bills = sgqlc.types.Field('_AddUrlReferredBillsPayload', graphql_name='AddUrlReferredBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    remove_url_referred_bills = sgqlc.types.Field('_RemoveUrlReferredBillsPayload', graphql_name='RemoveUrlReferredBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    merge_url_referred_bills = sgqlc.types.Field('_MergeUrlReferredBillsPayload', graphql_name='MergeUrlReferredBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    add_url_referred_laws = sgqlc.types.Field('_AddUrlReferredLawsPayload', graphql_name='AddUrlReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    remove_url_referred_laws = sgqlc.types.Field('_RemoveUrlReferredLawsPayload', graphql_name='RemoveUrlReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    merge_url_referred_laws = sgqlc.types.Field('_MergeUrlReferredLawsPayload', graphql_name='MergeUrlReferredLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    add_url_referred_members = sgqlc.types.Field('_AddUrlReferredMembersPayload', graphql_name='AddUrlReferredMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    remove_url_referred_members = sgqlc.types.Field('_RemoveUrlReferredMembersPayload', graphql_name='RemoveUrlReferredMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    merge_url_referred_members = sgqlc.types.Field('_MergeUrlReferredMembersPayload', graphql_name='MergeUrlReferredMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_UrlInput), graphql_name='to', default=None)),
))
    )
    create_url = sgqlc.types.Field('Url', graphql_name='CreateUrl', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
        ('text', sgqlc.types.Arg(String, graphql_name='text', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('domain', sgqlc.types.Arg(String, graphql_name='domain', default=None)),
        ('accessed_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='accessedOn', default=None)),
))
    )
    update_url = sgqlc.types.Field('Url', graphql_name='UpdateUrl', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('text', sgqlc.types.Arg(String, graphql_name='text', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('domain', sgqlc.types.Arg(String, graphql_name='domain', default=None)),
        ('accessed_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='accessedOn', default=None)),
))
    )
    delete_url = sgqlc.types.Field('Url', graphql_name='DeleteUrl', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_url = sgqlc.types.Field('Url', graphql_name='MergeUrl', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('text', sgqlc.types.Arg(String, graphql_name='text', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('domain', sgqlc.types.Arg(String, graphql_name='domain', default=None)),
        ('accessed_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='accessedOn', default=None)),
))
    )
    add_timeline_relating_bills = sgqlc.types.Field('_AddTimelineRelatingBillsPayload', graphql_name='AddTimelineRelatingBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    remove_timeline_relating_bills = sgqlc.types.Field('_RemoveTimelineRelatingBillsPayload', graphql_name='RemoveTimelineRelatingBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    merge_timeline_relating_bills = sgqlc.types.Field('_MergeTimelineRelatingBillsPayload', graphql_name='MergeTimelineRelatingBills', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_BillInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    add_timeline_relating_laws = sgqlc.types.Field('_AddTimelineRelatingLawsPayload', graphql_name='AddTimelineRelatingLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    remove_timeline_relating_laws = sgqlc.types.Field('_RemoveTimelineRelatingLawsPayload', graphql_name='RemoveTimelineRelatingLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    merge_timeline_relating_laws = sgqlc.types.Field('_MergeTimelineRelatingLawsPayload', graphql_name='MergeTimelineRelatingLaws', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_LawInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    add_timeline_relating_members = sgqlc.types.Field('_AddTimelineRelatingMembersPayload', graphql_name='AddTimelineRelatingMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    remove_timeline_relating_members = sgqlc.types.Field('_RemoveTimelineRelatingMembersPayload', graphql_name='RemoveTimelineRelatingMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    merge_timeline_relating_members = sgqlc.types.Field('_MergeTimelineRelatingMembersPayload', graphql_name='MergeTimelineRelatingMembers', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_MemberInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_TimelineInput), graphql_name='to', default=None)),
))
    )
    create_timeline = sgqlc.types.Field('Timeline', graphql_name='CreateTimeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('content', sgqlc.types.Arg(String, graphql_name='content', default=None)),
        ('started_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startedOn', default=None)),
))
    )
    update_timeline = sgqlc.types.Field('Timeline', graphql_name='UpdateTimeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('content', sgqlc.types.Arg(String, graphql_name='content', default=None)),
        ('started_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startedOn', default=None)),
))
    )
    delete_timeline = sgqlc.types.Field('Timeline', graphql_name='DeleteTimeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_timeline = sgqlc.types.Field('Timeline', graphql_name='MergeTimeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('content', sgqlc.types.Arg(String, graphql_name='content', default=None)),
        ('started_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startedOn', default=None)),
))
    )


class Query(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('total_members', 'all_members', 'total_elections', 'all_elections', 'total_diets', 'all_diets', 'total_laws', 'all_laws', 'total_bills', 'all_bills', 'total_meetings', 'all_meetings', 'total_minutes', 'all_minutes', 'member', 'election', 'diet', 'law', 'bill', 'meeting', 'minutes', 'url', 'timeline')
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
    total_meetings = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalMeetings')
    all_meetings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Meeting'))), graphql_name='allMeetings', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MeetingOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MeetingFilter, graphql_name='filter', default=None)),
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
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
        ('name_hira', sgqlc.types.Arg(String, graphql_name='nameHira', default=None)),
        ('first_name_hira', sgqlc.types.Arg(String, graphql_name='firstNameHira', default=None)),
        ('last_name_hira', sgqlc.types.Arg(String, graphql_name='lastNameHira', default=None)),
        ('current', sgqlc.types.Arg(Boolean, graphql_name='current', default=None)),
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
        ('ndl_id', sgqlc.types.Arg(String, graphql_name='ndlId', default=None)),
        ('e_gov_id', sgqlc.types.Arg(String, graphql_name='eGovId', default=None)),
        ('e_gov_url', sgqlc.types.Arg(String, graphql_name='eGovUrl', default=None)),
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
        ('ndl_id', sgqlc.types.Arg(String, graphql_name='ndlId', default=None)),
        ('ndl_url', sgqlc.types.Arg(String, graphql_name='ndlUrl', default=None)),
        ('bill_title', sgqlc.types.Arg(String, graphql_name='billTitle', default=None)),
        ('bill_number', sgqlc.types.Arg(String, graphql_name='billNumber', default=None)),
        ('bill_category', sgqlc.types.Arg(BillCategory, graphql_name='billCategory', default=None)),
        ('bill_type', sgqlc.types.Arg(BillType, graphql_name='billType', default=None)),
        ('bill_status', sgqlc.types.Arg(BillStatus, graphql_name='billStatus', default=None)),
        ('syugiin_url', sgqlc.types.Arg(String, graphql_name='syugiinUrl', default=None)),
        ('sangiin_url', sgqlc.types.Arg(String, graphql_name='sangiinUrl', default=None)),
        ('overview_url', sgqlc.types.Arg(String, graphql_name='overviewUrl', default=None)),
        ('essential_url', sgqlc.types.Arg(String, graphql_name='essentialUrl', default=None)),
        ('comparison_url', sgqlc.types.Arg(String, graphql_name='comparisonUrl', default=None)),
        ('pull_request_url', sgqlc.types.Arg(String, graphql_name='pullRequestUrl', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    meeting = sgqlc.types.Field(sgqlc.types.list_of('Meeting'), graphql_name='Meeting', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MeetingOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MeetingFilter, graphql_name='filter', default=None)),
))
    )
    minutes = sgqlc.types.Field(sgqlc.types.list_of('Minutes'), graphql_name='Minutes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('ndl_id', sgqlc.types.Arg(String, graphql_name='ndlId', default=None)),
        ('ndl_url', sgqlc.types.Arg(String, graphql_name='ndlUrl', default=None)),
        ('minutes_number', sgqlc.types.Arg(String, graphql_name='minutesNumber', default=None)),
        ('start', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='end', default=None)),
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
        ('text', sgqlc.types.Arg(String, graphql_name='text', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('domain', sgqlc.types.Arg(String, graphql_name='domain', default=None)),
        ('accessed_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='accessedOn', default=None)),
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
        ('started_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startedOn', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_TimelineOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_TimelineFilter, graphql_name='filter', default=None)),
))
    )


class Timeline(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'content', 'started_on', 'relating_bills', 'relating_laws', 'relating_members', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    content = sgqlc.types.Field(String, graphql_name='content')
    started_on = sgqlc.types.Field('_Neo4jDateTime', graphql_name='startedOn')
    relating_bills = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bill)), graphql_name='relatingBills', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    relating_laws = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Law)), graphql_name='relatingLaws', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_LawOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_LawFilter, graphql_name='filter', default=None)),
))
    )
    relating_members = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Member)), graphql_name='relatingMembers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_MemberOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_MemberFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Url(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'url', 'text', 'type', 'domain', 'accessed_on', 'referred_bills', 'referred_laws', 'referred_members', '_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    text = sgqlc.types.Field(String, graphql_name='text')
    type = sgqlc.types.Field(String, graphql_name='type')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    accessed_on = sgqlc.types.Field('_Neo4jDateTime', graphql_name='accessedOn')
    referred_bills = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bill)), graphql_name='referredBills', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    referred_laws = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bill)), graphql_name='referredLaws', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    referred_members = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bill)), graphql_name='referredMembers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BillOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BillFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class _AddBillAmmendsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddBillDiscussedAtPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddBillReferUrlPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _AddBillRelatedTimeLinePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _AddBillSubmittedByPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddBillSubmittedToPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _AddDietBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _AddDietMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _AddElectionElectedMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Election, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _AddLawAmendedByPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _AddLawDiscussedAtPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _AddLawReferUrlPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _AddLawReferencedByPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _AddLawReferencesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _AddLawRelatedTimeLinePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _AddMeetingMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Meeting, graphql_name='to')


class _AddMeetingMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Meeting, graphql_name='to')


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


class _AddMemberElectedByPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Election, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _AddMemberReferUrlPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _AddMemberRelatedTimeLinePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _AddMemberSubmittedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


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


class _AddMinutesHeldAtPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _AddMinutesMeetingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Meeting, graphql_name='to')


class _AddMinutesParticipantsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _AddTimelineRelatingBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _AddTimelineRelatingLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _AddTimelineRelatingMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _AddUrlReferredBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _AddUrlReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _AddUrlReferredMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _MergeBillAmmendsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeBillDiscussedAtPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeBillReferUrlPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _MergeBillRelatedTimeLinePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _MergeBillSubmittedByPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeBillSubmittedToPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _MergeDietBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _MergeDietMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _MergeElectionElectedMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Election, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _MergeLawAmendedByPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _MergeLawDiscussedAtPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _MergeLawReferUrlPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _MergeLawReferencedByPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _MergeLawReferencesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _MergeLawRelatedTimeLinePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _MergeMeetingMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Meeting, graphql_name='to')


class _MergeMeetingMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Meeting, graphql_name='to')


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


class _MergeMemberElectedByPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Election, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _MergeMemberReferUrlPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _MergeMemberRelatedTimeLinePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _MergeMemberSubmittedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


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


class _MergeMinutesHeldAtPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _MergeMinutesMeetingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Meeting, graphql_name='to')


class _MergeMinutesParticipantsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _MergeTimelineRelatingBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _MergeTimelineRelatingLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _MergeTimelineRelatingMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _MergeUrlReferredBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _MergeUrlReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _MergeUrlReferredMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


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


class _RemoveBillAmmendsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveBillDiscussedAtPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveBillReferUrlPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _RemoveBillRelatedTimeLinePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _RemoveBillSubmittedByPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveBillSubmittedToPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _RemoveDietBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _RemoveDietMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _RemoveElectionElectedMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Election, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _RemoveLawAmendedByPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


class _RemoveLawDiscussedAtPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _RemoveLawReferUrlPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _RemoveLawReferencedByPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _RemoveLawReferencesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Law, graphql_name='to')


class _RemoveLawRelatedTimeLinePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _RemoveMeetingMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Meeting, graphql_name='to')


class _RemoveMeetingMinutesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Meeting, graphql_name='to')


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


class _RemoveMemberElectedByPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Election, graphql_name='from')
    to = sgqlc.types.Field(Member, graphql_name='to')


class _RemoveMemberReferUrlPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _RemoveMemberRelatedTimeLinePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _RemoveMemberSubmittedBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Bill, graphql_name='to')


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


class _RemoveMinutesHeldAtPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Diet, graphql_name='to')


class _RemoveMinutesMeetingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Minutes, graphql_name='from')
    to = sgqlc.types.Field(Meeting, graphql_name='to')


class _RemoveMinutesParticipantsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Minutes, graphql_name='to')


class _RemoveTimelineRelatingBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _RemoveTimelineRelatingLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Law, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _RemoveTimelineRelatingMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Member, graphql_name='from')
    to = sgqlc.types.Field(Timeline, graphql_name='to')


class _RemoveUrlReferredBillsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _RemoveUrlReferredLawsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')


class _RemoveUrlReferredMembersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(Bill, graphql_name='from')
    to = sgqlc.types.Field(Url, graphql_name='to')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None

