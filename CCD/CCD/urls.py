"""CCD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView
from CCD.main import views as core_views
from django.urls import path

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', core_views.search, name='search'),
    path('portal/search/', core_views.search1, name='search1'),
    path('portal/<int:pk>/delete/', core_views.AnnouncementDeleteView.as_view(), name='announcement-delete'),
    path('<int:pk>/delete/', core_views.StudentAnnouncementDeleteView.as_view(), name='student-announcement-delete'),
    path('portal/<int:pk>/profile/', core_views.profile, name='profile'),
    path('portal/<int:pk>/studentprofile/', core_views.studentprofile, name='student-profile'),
    path('portal/<int:pk>/selectedstudents/', core_views.selectedstudents, name='selected-students'),
    path('portal/<int:pk>/<int:pk2>/updateprofile', core_views.UpdateProfile, name='Update-Profile'),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^portal/$', core_views.portal, name='portal'),
    url(r'^logout/$', core_views.logout_view, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^portal/profile/$', core_views.profile, name='profile'),
    url(r'^portal/add_students_announcement/$',core_views.StudentsAnnouncementview.as_view(),name='studentannouncement'),
    url(r'^portal/add_private_announcement/$',core_views.PrivateAnnouncementview.as_view(),name='privateannouncement'),
    ]