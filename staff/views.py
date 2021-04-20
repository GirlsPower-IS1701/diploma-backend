from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from staff.models import Staff, Academic_Degree, Academic_Rank, Positions, StaffProfile
from staff.serializers import StaffSerializer, StaffProfileSerializer


class StaffApi(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StaffSerializer

    def get(self, request, *args, **kwargs):
        staff = Staff.objects.all()
        serializer = self.serializer_class(staff, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            staff = Staff(
                user = User.objects.get(pk=request.POST["user_id"]),
                academic_degree=Academic_Degree.objects.get(pk=request.POST["academic_degree_id"]),
                academic_rank=Academic_Rank.objects.get(pk=request.POST["academic_rank_id"]),
                position = Positions.objects.get(pk=request.POST["position_id"])
            )
            staff.save()
            response_serializer = self.serializer_class(staff)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class StaffProfileApi(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StaffProfileSerializer

    def get(self, request, *args, **kwargs):
        staff = Staff.objects.get(user=request.user)
        staff_profile = StaffProfile.objects.get(staff=staff)
        serializer = self.serializer_class(staff_profile)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            staff_profile = StaffProfile(
                staff = Staff.objects.get(user=request.user),
                avatar=serializer.validated_data.get("avatar")
            )
            staff_profile.save()
            response_serializer = self.serializer_class(staff_profile)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




@api_view(('GET',))
@permission_classes([IsAuthenticated, ])
# @csrf_exempt
def get_staff_profile(request):
    user = request.user
    staff = Staff.objects.get(user=user)
    staff_profile = StaffProfile.objects.get(staff=staff)
    staff_serializer = StaffSerializer(staff)
    profile_serializer = StaffProfileSerializer(staff_profile)
    if profile_serializer.data['avatar']:
        return Response({"staff": staff_serializer.data, "avatar": profile_serializer.data['avatar']})
    else:
        return Response({"staff": staff_serializer.data, "avatar": None})


