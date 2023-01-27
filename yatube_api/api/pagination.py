from rest_framework.pagination import PageNumberPagination


class PostPagination(PageNumberPagination):
    PAGE_SIZE = 10
