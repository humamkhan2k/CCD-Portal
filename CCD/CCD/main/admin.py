from django.contrib import admin
from .models import UserProfile,StudentsAnnouncement,PrivateAnnouncement
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(StudentsAnnouncement)
admin.site.register(PrivateAnnouncement)
