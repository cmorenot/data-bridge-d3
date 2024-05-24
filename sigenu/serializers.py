# serializers.py
from rest_framework import serializers
from .models import (Student, Career, NationalCareer, Country, EntrySource, StudyRegimen, Province, University,
                      AcademicSituation, StudentStatus, StudentType, Faculty, Town, SkinColor, SciencEspecialty,
                        Orphan, CourseType, ScholasticOrigin, PoliticOrg, Sex, TownUniversity, MaritalStatus
                        )


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'


class SciencEspecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = SciencEspecialty
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class NationalCareerSerializer(serializers.ModelSerializer):
    scienc_especialty_fk = SciencEspecialtySerializer(read_only=True)

    class Meta:
        model = NationalCareer
        fields = '__all__'



class TownSerializer(serializers.ModelSerializer):
    province_fk = ProvinceSerializer(read_only=True)

    class Meta:
        model = Town
        fields = '__all__'



class FacultySerializer(serializers.ModelSerializer):
    town_fk = TownSerializer(read_only=True)
    university_fk = UniversitySerializer(read_only=True)
    
    class Meta:
        model = Faculty
        fields = '__all__'


class TownUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TownUniversity
        fields = '__all__'


class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = '__all__'


class CareerSerializer(serializers.ModelSerializer):
    national_career_fk = NationalCareerSerializer(read_only=True)
    faculty_fk = FacultySerializer(read_only=True)
    town_university_fk = TownUniversitySerializer(read_only=True)
    course_type_fk = CourseTypeSerializer(read_only=True)

    class Meta:
        model = Career
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class EntrySourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntrySource
        fields = '__all__'


class StudentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentStatus
        fields = '__all__'

    
class AcademicSituationSerializer(serializers.ModelSerializer):
    student_status_fk = StudentStatusSerializer(read_only=True)

    class Meta:
        model = AcademicSituation
        fields = '__all__'


class StudentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentType
        fields = '__all__'


class OrphanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orphan
        fields = '__all__'


class ScholasticOriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholasticOrigin
        fields = '__all__'


class PoliticOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticOrg
        fields = '__all__'


class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = '__all__'


class MaritalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = '__all__'

class StudyRegimenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudyRegimen
        fields = '__all__'



class SkinColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinColor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    career_fk = CareerSerializer(read_only=True)
    country_fk = CountrySerializer(read_only=True)
    entry_source_fk = EntrySourceSerializer(read_only=True)
    academic_situation_fk = AcademicSituationSerializer(read_only=True)
    student_status_fk = StudentStatusSerializer(read_only=True)
    student_type_fk = StudentTypeSerializer(read_only=True)
    faculty_fk = FacultySerializer(read_only=True)
    orphan_fk = OrphanSerializer(read_only=True)
    course_type_fk = CourseTypeSerializer(read_only=True)
    scholastic_origin_fk = ScholasticOriginSerializer(read_only=True)
    politic_org_fk = PoliticOrgSerializer(read_only=True)
    sex_fk = SexSerializer(read_only=True)
    town_university_fk = TownUniversitySerializer(read_only=True)
    marital_status_fk = MaritalStatusSerializer(read_only=True)
    study_regimen_fk = StudyRegimenSerializer(read_only=True)
    town_fk = TownSerializer(read_only=True)
    skin_color_fk = SkinColorSerializer(read_only=True)

    birth_date = serializers.DateField(source='fixed_birth_date', required=False)
    higher_education_in_date = serializers.DateField(source='fixed_higher_education_date', required=False)
    university_in_date = serializers.DateField(source='fixed_university_in_date', required=False)
    register_date = serializers.DateTimeField(source='fixed_register_date', required=False)


    class Meta:
        model = Student
        fields = '__all__'
    


