from django.db import models

from departments.models import Department, Subjects
from staff.models import Staff
from students.models import Students



class Adviser(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="staff")
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Adviser'
        verbose_name_plural = 'Advisers'


class Group(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="department")
    name = models.CharField(max_length=255, null=True, blank=True)
    adviser = models.ForeignKey(Adviser, on_delete=models.CASCADE, verbose_name="adviser")
    start_year = models.DateField(null=True, blank=True)
    finish_year = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class Enrollment(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name="subject")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="group")
    lecturer = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="lecturer", related_name="enrollmentlecturer")
    tutor = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="tutor", related_name="enrollmenttutor")
    semester = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'


class Grades(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, verbose_name="enrollment")
    student = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name="student")
    pk1 = models.FloatField(null=True, blank=True)
    pk2 = models.FloatField(null=True, blank=True)
    exam_grade = models.FloatField(null=True, blank=True)
    final_grade = models.FloatField(null=True, blank=True)
    grade_letter = models.CharField(max_length=255, null=True, blank=True)
    gpa = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'







