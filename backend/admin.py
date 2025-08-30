from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Department, Manager, Staff, Customer

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'phone')}),
    )

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'team', 'status')
    list_filter = ('department', 'status')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'manager', 'skill', 'status')
    list_filter = ('manager', 'status')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'skill')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'gender', 'status', 'added_on')
    list_filter = ('gender', 'status', 'added_on')
    search_fields = ('name', 'email', 'phone')