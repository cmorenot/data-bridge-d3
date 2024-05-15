import django_filters
from .models import Student

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'name': ['exact', 'icontains'],
            'identification': ['exact', 'icontains'],
            # Agrega más campos aquí si es necesario
        }