# Generated by Django 3.1.6 on 2021-05-07 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Subject_Cycles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('short_title', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Subject_Cycle',
                'verbose_name_plural': 'Subject_Cycles',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('lection_count', models.IntegerField(blank=True, null=True)),
                ('lab_count', models.IntegerField(blank=True, null=True)),
                ('practice_count', models.IntegerField(blank=True, null=True)),
                ('is_additional', models.BooleanField(default=False, null=True)),
                ('is_language', models.BooleanField(default=False, null=True)),
                ('is_research', models.BooleanField(default=False, null=True)),
                ('is_practice', models.BooleanField(default=False, null=True)),
                ('credits_count', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject_cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.subject_cycles', verbose_name='subject_cycles')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='Cafedra_Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department', verbose_name='department')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.subjects', verbose_name='subject')),
            ],
            options={
                'verbose_name': 'Cafedra_Subject',
                'verbose_name_plural': 'Cafedra_Subjects',
            },
        ),
    ]
