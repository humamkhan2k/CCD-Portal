from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company = models.CharField(max_length=40,default='')
    email = models.EmailField(default='',unique = True)
    Phone_number = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username
    
class StudentsAnnouncement(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default='')
    student = models.CharField(max_length=40,default='')
    rollnumber = models.CharField(max_length=20,default='')
    Announcement = models.TextField()
    AnnouncementTime = models.DateTimeField(default=timezone.now)
    
class PrivateAnnouncement(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    poc_company = models.CharField(max_length=40,default='')
    Announcement = models.TextField()
    AnnouncementTime = models.DateTimeField(default=timezone.now)
    
#class Students(models.Models):
 #   name = models.CharField(max_length=40,default='')
  #  Phone_number = models.IntegerField(default=0)
   # email = models.EmailField(default='',unique = True)