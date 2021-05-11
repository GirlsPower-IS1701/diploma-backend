# Generated by Django 3.1.6 on 2021-05-11 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('references', '0002_reference_reference_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reference',
            name='student',
        ),
        migrations.AddField(
            model_name='reference',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]