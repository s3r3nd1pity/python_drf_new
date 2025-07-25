from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PagePagination(PageNumberPagination):
    page_size = 2
    max_page_size = 10
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        return Response({
            'total_results': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'next': bool(self.get_next_link()),
            'previous': bool(self.get_previous_link()),
            'results': data,
        })