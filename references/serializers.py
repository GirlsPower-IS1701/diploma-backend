from rest_framework import serializers
from .models import Reference, Reference_Type
from accounts.serializers import UserSerializer

from students.serializers import StudentsSerializer

class Reference_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reference_Type
        fields = ('id', 'name')

class ReferenceSerialaizer(serializers.ModelSerializer):
    reference_type_id = Reference_Type_Serializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Reference
        fields = ('id', 'reference_type_id', 'user', 'reference_file')