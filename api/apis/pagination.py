from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination             

class LoSung(LimitOffsetPagination):
    default_size=5
    limit_query_param='size'
    offset_query_param='start'
    max_limit=10
    
    
class LoSuuung(PageNumberPagination):
    page_size=1
    page_query_param='P'
    page_size_query_param='choice'
    max_page_size=2
    last_page_strings='end'