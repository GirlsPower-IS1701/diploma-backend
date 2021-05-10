from django.shortcuts import render
from students.models import Students
from students.serializers import StudentsSerializer
from rest_framework.views import APIView
import pdfkit
from django.core.mail import EmailMessage
from rest_framework.response import Response
from accounts.serializers import UserSerializer
# Create your views here.
class ReferenceApiView(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        options = {
            'encoding': "UTF-8"
        }

        user=request.user
        reference_type = request.data.get('type')
        
        body = "<html lang='en' style=' box-sizing: border-box;'><head><meta charset='UTF-8'><title>CV</title></head><body style='font-family: Source Sans Pro, sans-serif; line-height: 1.5; background: #F2F2F2; color: #323232;'><div style='max-width: 960px; margin: 40px auto; padding: 32px; background: white; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);'><section style='display: grid; grid-template-columns: 1fr 4fr; grid-gap: 20px; padding: 24px 0; border-bottom: 1px solid lightgrey;'> <div> </div>  <div><div style='font-size: 48px; line-height: 1;'>"+request.user.first_name+" "+request.user.last_name+"</div><div style='display: flex; margin: 10px 0 20px 0;'><div style='display: flex; align-items: center; flex: 1;'><svg viewBox='0 0 1792 1792' style='margin-right: 6px;' xmlns='http://www.w3.org/2000/svg'><path d='M1664 1504v-768q-32 36-69 66-268 206-426 338-51 43-83 67t-86.5 48.5-102.5 24.5h-2q-48 0-102.5-24.5t-86.5-48.5-83-67q-158-132-426-338-37-30-69-66v768q0 13 9.5 22.5t22.5 9.5h1472q13 0 22.5-9.5t9.5-22.5zm0-1051v-24.5l-.5-13-3-12.5-5.5-9-9-7.5-14-2.5h-1472q-13 0-22.5 9.5t-9.5 22.5q0 168 147 284 193 152 401 317 6 5 35 29.5t46 37.5 44.5 31.5 50.5 27.5 43 9h2q20 0 43-9t50.5-27.5 44.5-31.5 46-37.5 35-29.5q208-165 401-317 54-43 100.5-115.5t46.5-131.5zm128-37v1088q0 66-47 113t-113 47h-1472q-66 0-113-47t-47-113v-1088q0-66 47-113t113-47h1472q66 0 113 47t47 113z'/></svg><a href='mailto:email@email.com'>"+request.user.email+"</a></div> <div style='display: flex; align-items: center; flex: 1;'><svg  viewBox='0 0 1792 1792' style='margin-right: 6px;' xmlns='http://www.w3.org/2000/svg'><path d='M1600 1240q0 27-10 70.5t-21 68.5q-21 50-122 106-94 51-186 51-27 0-53-3.5t-57.5-12.5-47-14.5-55.5-20.5-49-18q-98-35-175-83-127-79-264-216t-216-264q-48-77-83-175-3-9-18-49t-20.5-55.5-14.5-47-12.5-57.5-3.5-53q0-92 51-186 56-101 106-122 25-11 68.5-21t70.5-10q14 0 21 3 18 6 53 76 11 19 30 54t35 63.5 31 53.5q3 4 17.5 25t21.5 35.5 7 28.5q0 20-28.5 50t-62 55-62 53-28.5 46q0 9 5 22.5t8.5 20.5 14 24 11.5 19q76 137 174 235t235 174q2 1 19 11.5t24 14 20.5 8.5 22.5 5q18 0 46-28.5t53-62 55-62 50-28.5q14 0 28.5 7t35.5 21.5 25 17.5q25 15 53.5 31t63.5 35 54 30q70 35 76 53 3 7 3 21z'/></svg><a href='tel:123-456-7890'>"+request.user.phone_number+"</a> </div> </div> </div>  </section> <section style='display: grid; grid-template-columns: 1fr 4fr; grid-gap: 20px; padding: 24px 0; border-bottom: 1px solid lightgrey;'><div style='font-weight: bold; font-size: 18px;'>О себе</div> <div> <div style='padding-bottom: 24px; margin-bottom: 24px; border-bottom: 1px solid lightgray;'><div style='display: flex; justify-content: space-between; margin-bottom: 20px; font-size: 18px;'><div>  <div style='line-height: 1.2;'></div> </div>  </div> </div>  </div> <div style='font-weight: bold; font-size: 18px;'>Дата рождения</div><div> <div style='padding-bottom: 24px; margin-bottom: 24px; border-bottom: 1px solid lightgray;'><div style='display: flex; justify-content: space-between; margin-bottom: 20px; font-size: 18px;'> <div> <div style='line-height: 1.2;'></div> </div>   </div>   </div>   </div> <div style='font-weight: bold; font-size: 18px;'>Сфера деятельности</div> <div> <div style='padding-bottom: 24px; margin-bottom: 24px; border-bottom: 1px solid lightgray;'> <div style='display: flex; justify-content: space-between; margin-bottom: 20px; font-size: 18px;'> <div>  <div style='line-height: 1.2;'></div>  </div> </div> </div>   </div><div style='font-weight: bold; font-size: 18px;'>Образование</div> <div><div style='padding-bottom: 24px; margin-bottom: 24px; border-bottom: 1px solid lightgray;'><div style='display: flex; justify-content: space-between; margin-bottom: 20px; font-size: 18px;'><div><div style='line-height: 1.2;'></div><div style='display: flex; justify-content: space-between; margin-bottom: 20px; font-size: 18px;'> </div> </div> </div>  </div>  </div></section><section style='display: grid; grid-template-columns: 1fr 4fr; grid-gap: 20px; padding: 24px 0; border-bottom: 1px solid lightgrey;'><div style='font-weight: bold; font-size: 18px;'>Знания</div> <div><div style='display: grid; grid-template-columns: 1fr 1fr 1fr; grid-gap: 20px; margin-bottom: 24px;'> <ul style='margin-left: 20px; list-style-type: disc;'> <li>React js</li> <li>Django</li><li>Git</li> </ul> </div>  </div> </section> <section style='display: grid; grid-template-columns: 1fr 4fr; grid-gap: 20px; padding: 24px 0; border-bottom: 1px solid lightgrey;'><div style='font-weight: bold; font-size: 18px;'>Ссылки</div> <div class='interests-container'><div style='display: grid; grid-template-columns: 1fr 1fr 1fr; grid-gap: 20px; margin-bottom: 24px;'><ul style='margin-left: 20px; list-style-type: disc;'> <li></li>   <li></li>   <li></li>  </ul>   </div>   </div> </section> </div></body></html>"
        myPdf = pdfkit.from_string(body, 'cv.pdf', options=options)
        serializer = self.serializer_class(user)
        msg = EmailMessage('Справка', request.user.first_name + ', ', 'ainur.is1701@gmail.com', [request.user.email])
        msg.content_subtype = "html"  
        msg.attach_file("cv.pdf")
        msg.send()
        return Response(serializer.data)


