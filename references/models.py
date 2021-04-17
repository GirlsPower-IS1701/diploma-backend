from django.db import models

# Create your models here.
from students.models import Students


class Reference_Type(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    template = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Reference_Type'
        verbose_name_plural = 'Reference_Types'


class Reference(models.Model):
    reference_type = models.ForeignKey(Reference_Type, on_delete=models.CASCADE, verbose_name="reference")
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Reference'
        verbose_name_plural = 'References'


class Student_Reference(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name="student")
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE, verbose_name="reference")
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Student_Reference'
        verbose_name_plural = 'Student_References'
