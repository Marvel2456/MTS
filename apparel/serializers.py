from pyexpat import model
from rest_framework import serializers
from . models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        
    def validate(self, attrs):
        customer_name = attrs.get('customer_name', '')
        
        return attrs
    
    def create(self, validated_data):
        return Customer.objects.create(**validated_data)         
    
        
class MaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Male
        fields = "__all__"

class FemaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Female
        fields = "__all__"
        
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"
        
    def validate(self, attrs):
        staff_name = attrs.get('staff_name', '')
        
        return attrs
    
    def create(self, validated_data):
        return Staff.objects.create(**validated_data)
        
class TailorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tailor
        fields = "__all__"
        
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = "__all__"
        
class ClotheSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Clothes
        fields = "__all__"
        
class RegisterInSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Clothes
        fields = "__all__"
        
class RegisterOutSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Clothes
        fields = "__all__"
        
class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Clothes
        fields = "__all__"
        
class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = "__all__"