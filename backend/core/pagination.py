from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 20
    max_page_size = 30
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        return Response({
            "total":self.page.paginator.count,
            "total_pages":self.page.paginator.num_pages,
            "prev":bool(self.get_previous_link()),
            "next":bool(self.get_next_link()),
            "data":data
        })

