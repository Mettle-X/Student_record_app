from django.contrib.auth.models import Student, academics
from rest_framework import serializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ["url", "surname", "middle_name", "age", "email", "state_of_origin", "department"]


class academicsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = academics
        fields = ["url", "faculty", "department", "current_level"]