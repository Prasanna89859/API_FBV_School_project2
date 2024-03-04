from rest_framework import serializers
from app.models import *

class SchoolModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=School
        fields='__all__'
        