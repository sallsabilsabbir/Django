from rest_framework import serializers
from .models import Aiquest

class AiquestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aiquest
        fields = ['id','teacher_name', 'course_name', 'course_duration', 'seat']




"""
# manual process: 

class AiquestSerializer(serializers.Serializer):
    teacher_name = serializers.CharField(max_length=25)
    course_name = serializers.CharField(max_length=20)
    course_duration = serializers.IntegerField()
    seat = serializers.IntegerField()

    def create(self, validated_data):
        # Create a new Aiquest instance
        aiquest_instance = Aiquest(
            teacher_name=validated_data['teacher_name'],
            course_name=validated_data['course_name'],
            course_duration=validated_data['course_duration'],
            seat=validated_data['seat']
        )
        # Save the instance to the database
        aiquest_instance.save()
        return aiquest_instance

"""