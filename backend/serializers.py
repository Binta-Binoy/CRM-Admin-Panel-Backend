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
    user = UserSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Manager
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    manager = ManagerSerializer(read_only=True)

    class Meta:
        model = Staff
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
