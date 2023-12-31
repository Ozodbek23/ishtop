from rest_framework import serializers
from resumes.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"
