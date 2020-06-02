"""
Serializer for patient.
"""
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from .models import Group, Contact
from rest_framework import serializers
        
class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['user', 'name']

class ContactSerializer(ModelSerializer):
    group = GroupSerializer
    group_name = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(required=None)
    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'birthdate', 'phone', 'email', 'url', 'group_name', 'group']
    
    def get_group_name(self, obj):
        return obj.group.name