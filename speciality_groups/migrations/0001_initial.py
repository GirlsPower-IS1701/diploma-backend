# Generated by Django 3.1.6 on 2021-05-07 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0003_subjects_department_id'),
        ('staff', '__first__'),
        ('students', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adviser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff', verbose_name='staff')),
            ],
            options={
                'verbose_name': 'Adviser',
                'verbose_name_plural': 'Advisers',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Enrollment',
                'verbose_name_plural': 'Enrollments',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start_year', models.DateField(blank=True, null=True)),
                ('finish_year', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('adviser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speciality_groups.adviser', verbose_name='adviser')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department', verbose_name='department')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pk1', models.FloatField(blank=True, null=True)),
                ('pk2', models.FloatField(blank=True, null=True)),
                ('exam_grade', models.FloatField(blank=True, null=True)),
                ('final_grade', models.FloatField(blank=True, null=True)),
                ('grade_letter', models.CharField(blank=True, max_length=255, null=True)),
                ('gpa', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speciality_groups.enrollment', verbose_name='enrollment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.students', verbose_name='student')),
            ],
            options={
                'verbose_name': 'Grade',
                'verbose_name_plural': 'Grades',
            },
        ),
        migrations.AddField(
            model_name='enrollment',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speciality_groups.group', verbose_name='group'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='lecturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollmentlecturer', to='staff.staff', verbose_name='lecturer'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.subjects', verbose_name='subject'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollmenttutor', to='staff.staff', verbose_name='tutor'),
        ),
    ]