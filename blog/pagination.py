from rest_framework.pagination import PageNumberPagination


class PostPageNumberPagination(PageNumberPagination):
    # Nr. of posts per page
    page_size = 5
    # Control requested pages
    page_size_query_param = 'page_size'
    # With the max requested pages being
    max_page_size = 1
