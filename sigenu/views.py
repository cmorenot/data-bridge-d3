from django.shortcuts import render

# Create your views here.

# views.py
from rest_framework import viewsets, pagination
from .models import Student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from.filters import StudentFilter

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10  # Define el número de resultados por página
    page_size_query_param = 'page_size'
    max_page_size = 1000


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.using('students_db').all()
    serializer_class = StudentSerializer
    pagination_class = StandardResultsSetPagination  # Agrega paginación a la vista
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudentFilter

