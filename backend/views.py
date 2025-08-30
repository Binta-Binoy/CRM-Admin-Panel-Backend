from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from .models import User, Department, Manager, Staff, Customer
from .serializers import (
    UserSerializer, DepartmentSerializer, ManagerSerializer, 
    StaffSerializer, CustomerSerializer, StaffFrontendSerializer, 
    CustomerFrontendSerializer
)

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.select_related('user', 'department').all()
    serializer_class = ManagerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.select_related('user', 'manager__user').all()
    serializer_class = StaffSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return StaffFrontendSerializer
        return StaffSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        # Create a User
        user = User.objects.create_user(
            username=data['mail'], 
            email=data['mail'], 
            first_name=data['fullName'].split()[0],
            last_name=' '.join(data['fullName'].split()[1:]),
            phone=data['phone'],
            role='Staff'
        )
        manager = Manager.objects.get(id=data['manager']) if data.get('manager') else None
        staff = Staff.objects.create(
            user=user,
            manager=manager,
            skill=data.get('skills', ''),
            status='Active'
        )
        serializer = StaffFrontendSerializer(staff)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        # Use frontend-compatible serializer for list/retrieve actions
        if self.action in ['list', 'retrieve']:
            return CustomerFrontendSerializer
        return CustomerSerializer