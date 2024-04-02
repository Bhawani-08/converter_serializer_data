from rest_framework import serializers
from .models import Table1,Table2

class Table1serializer(serializers.ModelSerializer):
    class Meta:
        model = Table1
        fields = '__all__'

class table2serializer(serializers.ModelSerializer):
    class Meta:
        model = Table2
        fields = '__all__'


