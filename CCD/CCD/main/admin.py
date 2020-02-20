from django.contrib import admin
from .models import UserProfile,StudentsAnnouncement,PrivateAnnouncement
from .models import candidate,eligible,company
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(StudentsAnnouncement)
admin.site.register(PrivateAnnouncement)
admin.site.register(company)
admin.site.register(eligible)
admin.site.register(candidate)
