# Generated by Django 2.2.13 on 2021-05-28 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('speciality_groups', '0002_group_enrollment'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGpa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa_file', models.FileField(blank=True, null=True, upload_to='gpalist/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Student_Gpa',
                'verbose_name_plural': 'Students_Gpa',
            },
        ),
    ]
