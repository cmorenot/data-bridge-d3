from django.db import models
from django.db.models import Case, F, Value, When

class DefaultManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using("students_db")

class StudentManager(DefaultManager):
    """Manager class for Student"""

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                fixed_birth_date=Case(
                    When(birth_date__year__gt=9999, then=Value(None)),
                    default=F("birth_date"),
                ),
                fixed_higher_education_date=Case(
                    When(higher_education_in_date__year__gt=9999, then=Value(None)),
                    default=F("higher_education_in_date"),
                ),
                fixed_university_in_date=Case(
                    When(university_in_date__year__gt=9999, then=Value(None)),
                    default=F("university_in_date"),
                ),
                fixed_register_date=Case(
                    When(register_date__year__gt=9999, then=Value(None)),
                    default=F("register_date"),
                ),
            )
            .defer("birth_date", "higher_education_in_date", "university_in_date", "register_date")
        )
