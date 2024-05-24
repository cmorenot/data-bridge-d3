from django.shortcuts import render

# Create your views here.

# views.py
from rest_framework import viewsets, pagination
from .models import (Student, Career, NationalCareer, Country, EntrySource, AcademicSituation, StudentStatus, StudentType, Faculty, Orphan, CourseType,
ScholasticOrigin, PoliticOrg, Sex, TownUniversity, MaritalStatus, StudyRegimen, Town, SkinColor, SciencEspecialty, Province, University)
from .serializers import (StudentSerializer, CareerSerializer, NationalCareerSerializer, CountrySerializer, EntrySourceSerializer, AcademicSituationSerializer, StudentStatusSerializer, StudentTypeSerializer,
                            FacultySerializer, OrphanSerializer, CourseTypeSerializer, ProvinceSerializer, UniversitySerializer,
                              ScholasticOriginSerializer, PoliticOrgSerializer, SexSerializer, SciencEspecialtySerializer,
                              TownUniversitySerializer, MaritalStatusSerializer, StudyRegimenSerializer, TownSerializer, SkinColorSerializer
                            )
from django_filters.rest_framework import DjangoFilterBackend
from.filters import StudentFilter

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100  # Define el número de resultados por página
    page_size_query_param = 'page_size'
    max_page_size = 1000


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.using('students_db').all()
    serializer_class = StudentSerializer
    pagination_class = StandardResultsSetPagination  # Agrega paginación a la vista
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudentFilter


class SciencEspecialtyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SciencEspecialty.objects.using('students_db').all()
    serializer_class = SciencEspecialtySerializer


class CareerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Career.objects.using('students_db').all()
    serializer_class = CareerSerializer


class NationalCareerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NationalCareer.objects.using('students_db').all()
    serializer_class = NationalCareerSerializer


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.using('students_db').all()
    serializer_class = CountrySerializer


class EntrySourceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EntrySource.objects.using('students_db').all()
    serializer_class = EntrySourceSerializer


class AcademicSituationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AcademicSituation.objects.using('students_db').all()
    serializer_class = AcademicSituationSerializer


class StudentStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StudentStatus.objects.using('students_db').all()
    serializer_class = StudentStatusSerializer


class StudentTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StudentType.objects.using('students_db').all()
    serializer_class = StudentTypeSerializer


class FacultyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Faculty.objects.using('students_db').all()
    serializer_class = FacultySerializer


class OrphanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Orphan.objects.using('students_db').all()
    serializer_class = OrphanSerializer


class CourseTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CourseType.objects.using('students_db').all()
    serializer_class = CourseTypeSerializer


class ScholasticOriginViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScholasticOrigin.objects.using('students_db').all()
    serializer_class = ScholasticOriginSerializer


class PoliticOrgViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PoliticOrg.objects.using('students_db').all()
    serializer_class = PoliticOrgSerializer


class SexViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sex.objects.using('students_db').all()
    serializer_class = SexSerializer

class TownUniversityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TownUniversity.objects.using('students_db').all()
    serializer_class = TownUniversitySerializer


class MaritalStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MaritalStatus.objects.using('students_db').all()
    serializer_class = MaritalStatusSerializer


class StudyRegimenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StudyRegimen.objects.using('students_db').all()
    serializer_class = StudyRegimenSerializer


class TownViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Town.objects.using('students_db').all()
    serializer_class = TownSerializer


class SkinColorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SkinColor.objects.using('students_db').all()
    serializer_class = SkinColorSerializer


class ProvinceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Province.objects.using('students_db').all()
    serializer_class = ProvinceSerializer


class UniversityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = University.objects.using('students_db').all()
    serializer_class = UniversitySerializer