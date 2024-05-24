# urls.py en tu aplicación
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (StudentViewSet, CareerViewSet, NationalCareerViewSet,
                     CountryViewSet, EntrySourceViewSet, AcademicSituationViewSet, UniversityViewSet, 
                     StudentStatusViewSet, StudentTypeViewSet, FacultyViewSet, StudyRegimenViewSet,TownViewSet, SciencEspecialtyViewSet, ProvinceViewSet,
                     OrphanViewSet, CourseTypeViewSet, ScholasticOriginViewSet,PoliticOrgViewSet, SexViewSet, TownUniversityViewSet, MaritalStatusViewSet, SkinColorViewSet
                     )

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'careers', CareerViewSet)
router.register(r'national_careers', NationalCareerViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'entry_sources', EntrySourceViewSet)
router.register(r'academic_situations', AcademicSituationViewSet)
router.register(r'student_statuses', StudentStatusViewSet)
router.register(r'student_types', StudentTypeViewSet)
router.register(r'faculties', FacultyViewSet)
router.register(r'orphans', OrphanViewSet)
router.register(r'course_types', CourseTypeViewSet)
router.register(r'scholastic_origins', ScholasticOriginViewSet)
router.register(r'politic_orgs', PoliticOrgViewSet)
router.register(r'sexes', SexViewSet)
router.register(r'town_universities', TownUniversityViewSet)
router.register(r'marital_statuses', MaritalStatusViewSet)
router.register(r'study_regimens', StudyRegimenViewSet)
router.register(r'towns', TownViewSet)
router.register(r'skin_colors', SkinColorViewSet)
router.register(r'scienc_especialties', SciencEspecialtyViewSet)
router.register(r'provinces', ProvinceViewSet)
router.register(r'universities', UniversityViewSet)



urlpatterns = [
    path('', include(router.urls)),
]

