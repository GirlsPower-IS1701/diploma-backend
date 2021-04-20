from django.db import models

# Create your models here.
class Academic_Calendar(models.Model):

    name = models.CharField(max_length=200, blank=True, null=True)
    from_year = models.IntegerField(blank=True, null=True)
    to_year = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Academic_Calendar'
        verbose_name_plural = 'Academic_Calendars'


class Events(models.Model):
    AUTUMN = 'Autumn'
    SPRING = 'Spring'

    SEMESTER_CHOISES = [
        (AUTUMN, 'Autumn'),
        (SPRING, 'Spring')
    ]

    name = models.CharField(max_length=200, blank=True, null=True)
    academic_calendar = models.ForeignKey(Academic_Calendar, on_delete=models.CASCADE, verbose_name="academic_calendar")
    semester = models.CharField(max_length=6, choices=SEMESTER_CHOISES, null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

