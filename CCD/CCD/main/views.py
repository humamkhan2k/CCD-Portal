from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.http import HttpResponse
=======
from django.http import HttpResponse,HttpResponseRedirect
>>>>>>> a3fb6cac250c608c0cc5d151587994f248177391
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, ProfileForm, StudentsAnnouncementForm, PrivateAnnouncementForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import StudentsAnnouncement,UserProfile, User
<<<<<<< HEAD
from django.urls import reverse_lazy
=======
from django.urls import reverse_lazy,reverse
>>>>>>> a3fb6cac250c608c0cc5d151587994f248177391
from django.views.generic import CreateView
# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def home(request):
    all_Announcement1 = StudentsAnnouncement.objects.all()
    all_Announcement = all_Announcement1[::-1]
    return render(request, 'homepage.html',{'all_Announcement' : all_Announcement})

@login_required
def portal(request):
    return render(request, 'home.html')

@login_required
def logout_view(request):
    print ("hii")
    logout(request)
<<<<<<< HEAD
    return render(request,'homepage.html')
=======
    return HttpResponseRedirect(reverse('home'))
>>>>>>> a3fb6cac250c608c0cc5d151587994f248177391

class StudentsAnnouncementview(CreateView):
     form_class = StudentsAnnouncementForm
     template_name = 'Student_Announcement_create.html'
     success_url = reverse_lazy('portal')
     
class PrivateAnnouncementview(CreateView):
     form_class = PrivateAnnouncementForm
     template_name = 'Private_Announcement_create.html'
     success_url = reverse_lazy('portal')

def profile(request):
    #s = User.username
    user = request.user
    obj = UserProfile.objects.get(user=user)
    args = {'obj' : obj}
    return render(request,'profile.html',args)

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('portal')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html', {'user_form': user_form, 'profile_form' : profile_form})
