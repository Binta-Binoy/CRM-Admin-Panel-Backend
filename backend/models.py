from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=50, choices=[
        ("Admin", "Admin"),
        ("Manager", "Manager"),
        ("Staff", "Staff"),
    ], default="Staff")
    phone = models.CharField(max_length=15, blank=True, null=True)
    joined_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(null=True, blank=True)

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="manager_profile")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ], default="Active")

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff_profile")
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, blank=True, related_name="staffs")
    skill = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ], default="Active")

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ])
    date_of_birth = models.DateField(null=True, blank=True)
    added_on = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ("New", "New"),
        ("Complete", "Complete"),
        ("Pending", "Pending"),
    ], default="New")
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.name