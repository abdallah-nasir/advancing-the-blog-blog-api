from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination




class CustomPagination(LimitOffsetPagination):
        default_limit  = 5
    


'''
class Pagination(PageNumberPagination):
        page_size   = 5
'''