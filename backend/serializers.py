from rest_framework import serializers
from .models import User, Department, Manager, Staff, Customer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "phone", "role", "joined_on"]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class ManagerSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    user_phone = serializers.CharField(source='user.phone', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    joined_on = serializers.DateField(source='user.joined_on', read_only=True)
    
    class Meta:
        model = Manager
        fields = ['id', 'user', 'user_name', 'user_email', 'user_phone', 'department', 
                 'department_name', 'team', 'status', 'joined_on']

class StaffSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    user_phone = serializers.CharField(source='user.phone', read_only=True)
    manager_name = serializers.CharField(source='manager.user.get_full_name', read_only=True)
    joined_on = serializers.DateField(source='user.joined_on', read_only=True)
    
    class Meta:
        model = Staff
        fields = ['id', 'user', 'user_name', 'user_email', 'user_phone', 'manager', 
                 'manager_name', 'skill', 'status', 'joined_on']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

# Frontend-compatible serializers (return data in the format your frontend expects)
class StaffFrontendSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='user.username', read_only=True)
    name = serializers.CharField(source='user.get_full_name', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    phone = serializers.CharField(source='user.phone', read_only=True)
    manager = serializers.CharField(source='manager.user.get_full_name', read_only=True)
    joinedOn = serializers.DateField(source='user.joined_on', read_only=True)
    
    class Meta:
        model = Staff
        fields = ['id', 'name', 'email', 'phone', 'manager', 'skill', 'status', 'joinedOn']

class CustomerFrontendSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    addedOn = serializers.DateField(source='added_on', read_only=True)
    
    def get_id(self, obj):
        return f"CUST{str(obj.id).zfill(3)}"
    
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'email', 'gender', 'addedOn', 'status']