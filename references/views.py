from django.shortcuts import render
from students.models import Students
from .models import Reference, Reference_Type
from .serializers import ReferenceSerialaizer
from students.serializers import StudentsSerializer
from rest_framework.views import APIView
import pdfkit
from django.core.mail import EmailMessage
from rest_framework.response import Response
from accounts.serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ReferenceApiView(APIView):
    serializer_class = UserSerializer
    serializer_class2 = ReferenceSerialaizer

    def post(self, request, format=None):
        options = {
            'encoding': "UTF-8"
        }

        user=request.user

        reference_type = request.data.get('type')
        
        body = "<html lang='en' style=' box-sizing: border-box;'><head><meta charset='UTF-8'><title>Справка</title></head><body><img src='https://storage.yvision.kz/images/user/stazzz/5dmkGhukuFi7AOWkzK7szIO8X5M8Rn.jpg' width='400' height='90' style=' display: block; margin-left: auto; margin-right: auto; width: 50%;'><br><br><br><br><br><br><br><table height='100' cellpadding='10' style='width:100%; border-radius:5px;'><tr><th><h3>Справка</h3></th></tr></table><p style=' margin-top: 10px; margin-bottom: 10px; margin-right: 200px; margin-left: 200px;'>Дана "+request.user.first_name+" "+request.user.last_name+"</p><p style=' margin-top: 10px; margin-bottom: 10px; margin-right: 200px; margin-left: 200px;'>В том, что он(а) действительно является студентом очного отделения в АО Международный университет информационных технологий по специальности 5I070300 - Информационные системы</p><p style=' margin-top: 10px; margin-bottom: 10px; margin-right: 200px; margin-left: 200px;'>Гос.лицензия Серия АБ № 0064907 от 29.05.2009 год без ограничения срока</p><p style=' margin-top: 10px; margin-bottom: 10px; margin-right: 200px; margin-left: 200px;'>Справка действительна на 220-2021 учебный год</p><p style=' margin-top: 10px; margin-bottom: 10px; margin-right: 200px; margin-left: 200px;'>Справка выдана для предъявления по месту требования</p><p style=' margin-top: 10px; margin-bottom: 10px; margin-right: 200px; margin-left: 200px;'>Срок обучения в учебном заведении 4(четыре) года</p><p style=' margin-top: 10px; margin-bottom: 10px; margin-right: 200px; margin-left: 200px;'>Период обучения с 01.09.2017г. по 30.06.2021г.</p><br><br><br><br><br><p style=' margin-top: 10px; margin-bottom: 10px; margin-right: 200px; margin-left: 200px;'></p></body></html>"
        myPdf = pdfkit.from_string(body, 'cv.pdf', options=options)
        serializer = self.serializer_class(user)
        msg = EmailMessage('Справка', request.user.first_name + ', ', 'aru.elemes23@gmail.com', [request.user.email])
        msg.content_subtype = "html"  
        
        msg.attach_file("cv.pdf")
        reference = Reference(reference_type_id = Reference_Type.objects.get(pk=reference_type), user = request.user, reference_file = "cv.pdf")
        reference.save()
        msg.send()
        return Response(serializer.data)



@api_view(('GET',))
@permission_classes([IsAuthenticated, ])
def get_reference_history(request):
    user = request.user

    references = Reference.objects.filter(user=user).order_by('created_at')
    serializer = ReferenceSerialaizer(references, many=True)

    return Response(serializer.data)