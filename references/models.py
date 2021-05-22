from django.db import models
from django.utils import timezone

from students.models import Students
from staff.models import Staff
from accounts.models import User

class Reference_Type(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Reference_Type'
        verbose_name_plural = 'Reference_Types'


class Reference(models.Model):
    reference_type_id = models.ForeignKey(Reference_Type, on_delete=models.CASCADE, verbose_name="reference_type")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user", null=True)
    reference_file = models.FileField(upload_to='references/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Reference'
        verbose_name_plural = 'References'
    
        