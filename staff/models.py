from django.db import models

# Create your models here.
from accounts.models import User


class Academic_Degree(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Academic_Degree'
        verbose_name_plural = 'Academic_Degrees'

class Academic_Rank(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Academic_Rank'
        verbose_name_plural = 'Academic_Ranks'


class Position_Types(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Position_Type'
        verbose_name_plural = 'Position_Types'


class Positions(models.Model):
    position_type = models.ForeignKey(Position_Types, on_delete=models.CASCADE, verbose_name="position_types")
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user")
    academic_degree = models.ForeignKey(Academic_Degree, on_delete=models.CASCADE, verbose_name="academic_degree")
    academic_rank = models.ForeignKey(Academic_Rank, on_delete=models.CASCADE, verbose_name="academic_rank")
    position = models.ForeignKey(Positions, on_delete=models.CASCADE, verbose_name="position")
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

class StaffProfile(models.Model):
    staff = models.OneToOneField(Staff, blank=False, on_delete=models.CASCADE, related_name="staff_avatar", null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, default='avatars/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Staff_Profile'
        verbose_name_plural = 'Staff_Profile'



