from django.db import models

# Create your models here.
from accounts.models import User


class Study_Form(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True)
    course_count = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Study_Form'
        verbose_name_plural = 'Study_Forms'

class Payment_Form(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Payment_Form'
        verbose_name_plural = 'Payment_Forms'


class Study_Statuses(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Study_Status'
        verbose_name_plural = 'Study_Statuses'

class Degree_Types(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Degree_Type'
        verbose_name_plural = 'Degree_Types'


class Students(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user")
    study_status = models.ForeignKey(Study_Statuses, on_delete=models.CASCADE, verbose_name="study_statuses")
    study_form = models.ForeignKey(Study_Form, on_delete=models.CASCADE, verbose_name="study_form")
    payment_form = models.ForeignKey(Payment_Form, on_delete=models.CASCADE, verbose_name="payment_form")
    course = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'










