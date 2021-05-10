from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    short_name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Subject_Cycles(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    short_title = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Subject_Cycle'
        verbose_name_plural = 'Subject_Cycles'


class Subjects(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="department", null=True)
    subject_cycle = models.ForeignKey(Subject_Cycles, on_delete=models.CASCADE, verbose_name="subject_cycles")
    lection_count = models.IntegerField(null=True, blank=True)
    lab_count = models.IntegerField(null=True, blank=True)
    practice_count = models.IntegerField(null=True, blank=True)
    is_additional = models.BooleanField(default=False, null=True)
    is_language = models.BooleanField(default=False, null=True)
    is_research = models.BooleanField(default=False, null=True)
    is_practice = models.BooleanField(default=False, null=True)
    credits_count = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

class Cafedra_Subjects(models.Model):
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name="subject")
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="department")
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Cafedra_Subject'
        verbose_name_plural = 'Cafedra_Subjects'


