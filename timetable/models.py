from django.db import models
from speciality_groups.models import Enrollment, Group

# Create your models here.
class Timetable(models.Model):
    MONDAY = '1'
    TUESDAY = '2'
    WEDNESDAY = '3'
    THURSDAY = '4'
    FRIDAY = '5'
    SATURDAY = '6'

    DAY_OF_WEEK = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
    )

    LECTURE = 'a'
    PRACTICE = 'b'
    LAB = 'c'

    LESSON_TYPE = (
        (LECTURE, 'Lecture'),
        (PRACTICE, 'Practice'),
        (LAB, 'Lab'),
    )

    day_of_week = models.CharField(max_length=1, choices=DAY_OF_WEEK)
    lesson_type = models.CharField(max_length=1, choices=LESSON_TYPE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    start_time = models.TimeField(null=True, blank=True)
    finish_time = models.TimeField(null=True, blank=True)
    room_number = models.CharField(max_length=200, null=True, blank=True)
    

    class Meta:
        verbose_name = 'Timetable'
        verbose_name_plural = 'Timetables'