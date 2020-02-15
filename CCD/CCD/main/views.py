from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, ProfileForm, StudentsAnnouncementForm, PrivateAnnouncementForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
<<<<<<< HEAD
from .models import StudentsAnnouncement,UserProfile, User, PrivateAnnouncement
=======
from .models import StudentsAnnouncement,UserProfile, User
from django.urls import reverse_lazy
>>>>>>> b31e434fa56bfe234d04a09936fad47ebe383e38
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView
# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def home(request):
    all_Announcement1 = StudentsAnnouncement.objects.all()
    all_Announcement = all_Announcement1[::-1]
    return render(request, 'homepage.html',{'all_Announcement' : all_Announcement})

@login_required
def portal(request):
    all_Announcement1 = PrivateAnnouncement.objects.all()
    all_Announcement = all_Announcement1[::-1]
    return render(request, 'home.html',{'all_Announcement' : all_Announcement})

@login_required
def logout_view(request):
    print ("hii")
    logout(request)
    return render(request,'homepage.html')
    return HttpResponseRedirect(reverse('home'))

class StudentsAnnouncementview(CreateView):
     form_class = StudentsAnnouncementForm
     template_name = 'Student_Announcement_create.html'
     success_url = reverse_lazy('portal')
     
class PrivateAnnouncementview(CreateView):
     form_class = PrivateAnnouncementForm
     template_name = 'Private_Announcement_create.html'
     #success_url = reverse_lazy('portal')
     
     def form_valid(self, form):
          self.object = form.save(commit=False)
          obj = UserProfile.objects.get(user=self.request.user)
          self.object.user = obj
          self.object.poc_company = obj.company
          self.object.save()
          return HttpResponseRedirect(reverse('portal'))

def profile(request):
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
