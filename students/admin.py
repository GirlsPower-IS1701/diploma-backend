from django.contrib import admin
from .models import Payment_Form, Degree_Types, Study_Form, Study_Statuses, Students, StudentProfile


class PaymentFormAdmin(admin.ModelAdmin):
    pass
admin.site.register(Payment_Form, PaymentFormAdmin)

class DegreeTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Degree_Types, DegreeTypeAdmin)

class StudyFormAdmin(admin.ModelAdmin):
    pass
admin.site.register(Study_Form, StudyFormAdmin)

class StudyStatusAdmin(admin.ModelAdmin):
    pass
admin.site.register(Study_Statuses, StudyStatusAdmin)

class StudentsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Students, StudentsAdmin)

class StudentProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentProfile, StudentProfileAdmin)