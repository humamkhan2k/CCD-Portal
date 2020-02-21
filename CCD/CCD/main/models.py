from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse

programme = (
        ('btech' , 'btech') ,
        ('mtech' , 'mtech') ,
        ('msc' , 'msc') ,
        ('mdes' , 'mdes') ,
        ('bdes' , 'bdes') ,
        ('phd' , 'phd') ,
        ('msr' , 'msr') ,
        ('ma' , 'ma') ,
)    
    
class candidate(models.Model):
    candidate_name = models.CharField(max_length = 200 , blank = False)
    roll_number = models.CharField(max_length=50)
    Phone_number = models.IntegerField(default=0)
    is_selected = models.BooleanField(default = False)
    is_interview = models.BooleanField(default = False)
    start_time = models.CharField(max_length = 200 , blank = True)
    expected_time = models.CharField(max_length = 200 , blank = True)
    company_name = models.CharField(max_length = 200 , blank = True)

    
    def get_absolute_url(self):
        return reverse('home')
    
    def __str__(self):
        return self.candidate_name
    
class eligible(models.Model):
    cpi = models.CharField(max_length=100 , blank = True)
    major = models.CharField(max_length=100 , blank = True)
    minor = models.BooleanField(default=False , blank = True)
    programme = models.CharField(max_length = 100 , choices = programme)
    specialization = models.CharField(max_length=100 , blank = True)
    def __str__(self):
        return self.cpi
    
class company(models.Model):
    company_name = models.CharField(max_length = 200 , blank = False)
    cpoc = models.CharField(max_length = 200 , blank = False)
    cpoc_contact = models.CharField(max_length = 200 , blank = False)
    eligibility_criteria = models.ManyToManyField(eligible , related_name = 'eligible_companies',blank=True )
    waiting_candidate = models.ManyToManyField(candidate, related_name = 'waiting_person' , blank = True)
    shortlist_candidate = models.ManyToManyField(candidate, related_name = 'shortlist_person' , blank=True)
    all_candidate = models.ManyToManyField(candidate, related_name = 'all_person', blank = True)

    def __str__(self):
        return self.company_name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company = models.OneToOneField(company , on_delete=models.CASCADE)
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
    
