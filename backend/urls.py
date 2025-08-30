from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, DepartmentViewSet, ManagerViewSet, StaffViewSet, CustomerViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'managers', ManagerViewSet)
router.register(r'staff', StaffViewSet)  # This matches your frontend API.get("staff/")
router.register(r'customers', CustomerViewSet)  # This matches your frontend API.get("customers/")

urlpatterns = [
    path('', include(router.urls)),
]