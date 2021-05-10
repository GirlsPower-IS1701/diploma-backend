from django.db import models

from students.models import Students
from staff.models import Staff


class Reference_Type(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Reference_Type'
        verbose_name_plural = 'Reference_Types'


class Reference(models.Model):
    reference_type_id = models.ForeignKey(Reference_Type, on_delete=models.CASCADE, verbose_name="reference_type")
    student = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name="student")

    class Meta:
        verbose_name = 'Reference'
        verbose_name_plural = 'References'
    
        