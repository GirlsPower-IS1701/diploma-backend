from django.db import models

# Create your models here.
from accounts.models import User
from speciality_groups.models import Enrollment


class Room_Type(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Room_Type'
        verbose_name_plural = 'Room_Types'

class Room(models.Model):
    number = models.CharField(max_length=255, null=True, blank=True)
    room_type = models.ForeignKey(Room_Type, on_delete=models.CASCADE, verbose_name="room_type")
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

class Lession_Time(models.Model):
    number = models.CharField(max_length=255, null=True, blank=True)
    time_begin = models.TimeField(null=True, blank=True)
    time_end = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Lession_Time'
        verbose_name_plural = 'Lession_Times'


class TimeTable(models.Model):
    MONDAY = '1'
    TUESDAY = '2'
    WEDNESDAY = '3'
    THURSDAY = '4'
    FRIDAY = '5'
    SATURDAY = '6'
    SUNDAY = '7'

    DAY_OF_WEEK = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday')
    )
    day = models.CharField(max_length=200, choices=DAY_OF_WEEK)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, verbose_name="enrollment")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="room")
    lession_time = models.ForeignKey(Lession_Time, on_delete=models.CASCADE, verbose_name="lession_time")
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Timetable'
        verbose_name_plural = 'Timetables'

