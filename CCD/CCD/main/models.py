from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company = models.CharField(max_length=40,default='')
    email = models.EmailField(default='',unique = True)
    
    def __str__(self):
        return self.user.username
    
class StudentsAnnouncement(models.Model):
    student = models.CharField(max_length=40,default='')
    rollnumber = models.CharField(max_length=20,default='')
    Announcement = models.TextField()
    AnnouncementTime = models.DateTimeField(default=timezone.now)