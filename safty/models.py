from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    dob = models.DateField(null=True)
    location = models.CharField(max_length=200, null=True)
    profile_image = models.ImageField(upload_to='images/profile', blank=True, null=True)
    guardian_name = models.CharField(max_length=200, null=True)
    guardian_phone = models.CharField(max_length=20, null=True)
    guardian_email = models.EmailField(max_length=30,null=True)

    def __str__(self):
        return self.user.username

class PoliceProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="police_profile")
    station_name = models.CharField(max_length=200)
    officer_details=models.CharField(max_length=300)
    police_station_location=models.CharField(max_length=200)
    helpline_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username

class Complaint(models.Model):
    complainant = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint #{self.pk}"


class Saftytips(models.Model):
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.description