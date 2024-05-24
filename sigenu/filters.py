import django_filters
from .models import Student


class StudentFilter(django_filters.FilterSet):
    national_career_code = django_filters.CharFilter(
        field_name='career_fk__national_career_fk__code', 
        label='National Career Code'
    )
    country_code = django_filters.CharFilter(
        field_name='country_fk__code', 
        label='Country Code'
    )

    class Meta:
        model = Student
        fields = {
            'name': ['exact', 'icontains'],
            'identification': ['exact', 'icontains'],

            'country_fk__code': ['exact', 'icontains'],
            'career_fk__national_career_fk__code': ['exact', 'icontains'],
        }
        labels = {
            'name': 'Nombre',
        }
