from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from students.models import Students
from .models import Grades, StudentGpa, Group_Enrollment
from .serializers import GradesSerializer
import pdfkit
from django.core.mail import EmailMessage
from rest_framework.response import Response

@api_view(('GET',))
@permission_classes([IsAuthenticated, ])
def get_study_plan(request):
    grades1 = []
    grades2 = []
    user = request.user
    student = Students.objects.get(user=user)
    for g in Grades.objects.filter(student=student):
        enrollment = g.enrollment
        subject = enrollment.subject.title
        semester = enrollment.semester
        if semester == 1:
            study_plan1 = {'subject': subject, 'pk1': g.pk1, 'pk2': g.pk2, 'final': g.final_grade, 'grade_letter': g.grade_letter, 'gpa': g.gpa}
            grades1.append(study_plan1)
        elif semester == 2:
            study_plan2 = {'subject': subject, 'pk1': g.pk1, 'pk2': g.pk2, 'final': g.final_grade, 'grade_letter': g.grade_letter, 'gpa': g.gpa}
            grades2.append(study_plan2)

    return Response({"1-semester": grades1, "2-semester": grades2})

@api_view(('GET',))
@permission_classes([IsAuthenticated, ])
def calculate_gpa(request):
    credits_count = 0
    total = 0
    user = request.user
    student = Students.objects.get(user=user)
    list = []
    data = []
    for g in Grades.objects.filter(student=student):
        data.append(GradesSerializer(g).data)
        enrollment = g.enrollment
        subject = enrollment.subject
        credits_count += int(subject.credits_count)
        total = subject.credits_count * int(g.gpa)
        list.append(total)
    total_sum = 0
    for i in list:
        total_sum+=i

    res = int(total_sum/credits_count)
    return Response({"grades": data, "gpa": res})





@api_view(('GET',))
@permission_classes([IsAuthenticated, ])
def calculate_gpa_example(request):
    credits_count = 0
    total = 0
    user = request.user
    student = Students.objects.get(user=user)
    list = []
    data = []
    group_enrollment = Group_Enrollment.objects.get(student_id = student)
    
    for g in Grades.objects.filter(student=student):
        
        enrollment = g.enrollment
        subject = enrollment.subject
        data.append({"subject": subject.title, "pk1": g.pk1, "pk2": g.pk2, "exam": g.exam_grade, "final": g.final_grade, "gpa": g.gpa})
        credits_count += int(subject.credits_count)
        total = int(subject.credits_count * float(g.gpa))
        list.append(total)
    total_sum = 0
    for i in list:
        total_sum+=i

    res = int(total_sum/credits_count)

    options = {
            'encoding': "UTF-8"
        }

    


    body2 = "<!DOCTYPE html><html><head><style>body {font-family:Verdana, Geneva, Tahoma, sans-serif;justify-content: center;align-items: center;height: 100vh;}#table {border: 1px solid black;text-align: center;}#table thead>tr>th:first-child {text-align: left;}#table tbody>tr>td:first-child {text-align: left;}#table thead {color: black;background-color: white;}#table td, th {padding: 15px;border: none;}#table th {color: l;font-size: 14px;}#table tbody>tr:hover {box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;background: linear-gradient(90deg, rgba(214,211,211,0.6617997540813201) 49%, rgba(206,206,206,0.5245448521205357) 100%);}#table tbody>tr {color: black;}</style></head><body id='body'><h3>Transcript</h3><h4>Name: " +request.user.first_name+ " </h4><h4>Surname: " +request.user.last_name+ "</h4><h4>Group: " +group_enrollment.group_id.name+ "</h4><table id='table' cellspacing='0' cellpadding='0'><thead><tr><td>1-semester</td><td></td><td></td><td></td><td></td><td></td></tr><tr><th>Subject</th><th>RK1</th><th>RK2</th><th>exam</th><th>final</th><th>GPA</th></tr></thead><tbody><tr><td>" +str(data[0]['subject'])+ "</td><td>" +str(data[0]['pk1'])+ "</td><td>" +str(data[0]['pk2'])+ "</td><td>" +str(data[0]['exam'])+ "</td><td>" +str(data[0]['final'])+ "</td><td>" +str(data[0]['gpa'])+ "</td><tr><td>" +str(data[1]['subject'])+ "</td><td>" +str(data[1]['pk1'])+ "</td><td>" +str(data[1]['pk2'])+ "</td><td>" +str(data[1]['exam'])+ "</td><td>" +str(data[1]['final'])+ "</td><td>" +str(data[1]['gpa'])+ "</tr></td><tr><td>" +str(data[2]['subject'])+ "</td><td>" +str(data[2]['pk1'])+ "</td><td>" +str(data[2]['pk2'])+ "</td><td>" +str(data[2]['exam'])+ "</td><td>" +str(data[2]['final'])+ "</td><td>" +str(data[2]['gpa'])+ "</tr></td></tr><tr><td>" +str(data[3]['subject'])+ "</td><td>" +str(data[3]['pk1'])+ "</td><td>" +str(data[3]['pk2'])+ "</td><td>" +str(data[3]['exam'])+ "</td><td>" +str(data[3]['final'])+ "</td><td>" +str(data[3]['gpa'])+ "</td></tr><tr><td>" +str(data[4]['subject'])+ "</td><td>" +str(data[4]['pk1'])+ "</td><td>" +str(data[4]['pk2'])+ "</td><td>" +str(data[4]['exam'])+ "</td><td>" +str(data[4]['final'])+ "</td><td>" +str(data[4]['gpa'])+ "</tr></td></tr><tr><td>" +str(data[5]['subject'])+ "</td><td>" +str(data[5]['pk1'])+ "</td><td>" +str(data[5]['pk2'])+ "</td><td>" +str(data[5]['exam'])+ "</td><td>" +str(data[5]['final'])+ "</td><td>" +str(data[5]['gpa'])+ "</td></tr><tr><td>" +str(data[6]['subject'])+ "</td><td>" +str(data[6]['pk1'])+ "</td><td>" +str(data[6]['pk2'])+ "</td><td>" +str(data[6]['exam'])+ "</td><td>" +str(data[6]['final'])+ "</td><td>" +str(data[6]['gpa'])+ "</tr></td></tr><tr><td>" +str(data[7]['subject'])+ "</td><td>" +str(data[7]['pk1'])+ "</td><td>" +str(data[7]['pk2'])+ "</td><td>" +str(data[7]['exam'])+ "</td><td>" +str(data[7]['final'])+ "</td><td>" +str(data[7]['gpa'])+ "</td></tr><tr><td>Total gpa: </td><td></td><td></td><td></td><td></td><td>" + str(res) +"</td></tr></tbody></table><br><br><br><br><table id='table' cellspacing='0' cellpadding='0'><thead><tr><td>2-semester</td><td></td><td></td><td></td><td></td><td></td></tr><tr><th>Subject</th><th>RK1</th><th>RK2</th><th>exam</th><th>final</th><th>GPA</th></tr></thead><tbody><tr><td>" +str(data[8]['subject'])+ "</td><td>" +str(data[8]['pk1'])+ "</td><td>" +str(data[8]['pk2'])+ "</td><td>" +str(data[8]['exam'])+ "</td><td>" +str(data[8]['final'])+ "</td><td>" +str(data[8]['gpa'])+ "</td><tr><td>" +str(data[9]['subject'])+ "</td><td>" +str(data[9]['pk1'])+ "</td><td>" +str(data[9]['pk2'])+ "</td><td>" +str(data[9]['exam'])+ "</td><td>" +str(data[9]['final'])+ "</td><td>" +str(data[9]['gpa'])+ "</tr></td><tr><td>" +str(data[10]['subject'])+ "</td><td>" +str(data[10]['pk1'])+ "</td><td>" +str(data[10]['pk2'])+ "</td><td>" +str(data[10]['exam'])+ "</td><td>" +str(data[10]['final'])+ "</td><td>" +str(data[10]['gpa'])+ "</tr></td></tr><tr><td>" +str(data[11]['subject'])+ "</td><td>" +str(data[11]['pk1'])+ "</td><td>" +str(data[11]['pk2'])+ "</td><td>" +str(data[11]['exam'])+ "</td><td>" +str(data[11]['final'])+ "</td><td>" +str(data[11]['gpa'])+ "</td></tr><tr><td>" +str(data[12]['subject'])+ "</td><td>" +str(data[12]['pk1'])+ "</td><td>" +str(data[12]['pk2'])+ "</td><td>" +str(data[12]['exam'])+ "</td><td>" +str(data[12]['final'])+ "</td><td>" +str(data[12]['gpa'])+ "</tr></td></tr><tr><td>" +str(data[13]['subject'])+ "</td><td>" +str(data[13]['pk1'])+ "</td><td>" +str(data[13]['pk2'])+ "</td><td>" +str(data[13]['exam'])+ "</td><td>" +str(data[13]['final'])+ "</td><td>" +str(data[13]['gpa'])+ "</td></tr><tr><td>" +str(data[14]['subject'])+ "</td><td>" +str(data[14]['pk1'])+ "</td><td>" +str(data[14]['pk2'])+ "</td><td>" +str(data[14]['exam'])+ "</td><td>" +str(data[14]['final'])+ "</td><td>" +str(data[14]['gpa'])+ "</tr></td></tr><tr><td>" +str(data[15]['subject'])+ "</td><td>" +str(data[15]['pk1'])+ "</td><td>" +str(data[15]['pk2'])+ "</td><td>" +str(data[15]['exam'])+ "</td><td>" +str(data[15]['final'])+ "</td><td>" +str(data[15]['gpa'])+ "</td></tr><tr><td>Total gpa: </td><td></td><td></td><td></td><td></td><td>" + str(res) +"</td></tr></tbody></table></body></html>" 
    myPdf2 = pdfkit.from_string(body2, 'gpa.pdf', options=options)
    msg2 = EmailMessage('Справка', request.user.first_name + ', ', 'aru.elemes23@gmail.com', [request.user.email])
    msg2.content_subtype = "html"  
    msg2.attach_file("gpa.pdf")
    student_gpa = StudentGpa(user = user, gpa_file = "gpa.pdf")
    student_gpa.save()
    msg2.send()
    return Response({"grades": data, "gpa": res})







