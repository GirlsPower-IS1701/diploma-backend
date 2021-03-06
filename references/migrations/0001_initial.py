# Generated by Django 3.1.6 on 2021-05-08 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Reference_Type',
                'verbose_name_plural': 'Reference_Types',
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='references.reference_type', verbose_name='reference_type')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.students', verbose_name='student')),
            ],
            options={
                'verbose_name': 'Reference',
                'verbose_name_plural': 'References',
            },
        ),
    ]
