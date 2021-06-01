from django.contrib import admin
from .models import Adviser, Group, Enrollment, Grades, Group_Enrollment, StudentGpa
# Register your models here.

class AdviserAdmin(admin.ModelAdmin):
    pass
admin.site.register(Adviser, AdviserAdmin)

class GroupAdmin(admin.ModelAdmin):
    pass
    list_display = ('department', 'name', 'adviser', 'start_year', 'finish_year')
    search_fields = ['name']
admin.site.register(Group, GroupAdmin)

class EnrollmentAdmin(admin.ModelAdmin):
    pass
    list_display = ('subject', 'group', 'tutor', 'semester')
admin.site.register(Enrollment, EnrollmentAdmin)

class GradesAdmin(admin.ModelAdmin):
    pass
    list_display = ('enrollment', 'student', 'pk1', 'pk2', 'exam_grade', 'final_grade', 'grade_letter', 'gpa')
admin.site.register(Grades, GradesAdmin)

class EnrollmentGroupAdmin(admin.ModelAdmin):
    pass
admin.site.register(Group_Enrollment, EnrollmentGroupAdmin)

class StudentGpaAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentGpa, StudentGpaAdmin)