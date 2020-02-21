from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, ProfileForm, StudentsAnnouncementForm, PrivateAnnouncementForm,UpdateCandidateDetail
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import *
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def home(request):
    # all_Announcement1 = StudentsAnnouncement.objects.all()
    # all_Announcement = all_Announcement1[::-1]
    return render(request, 'homepage.html')

@login_required
def portal(request):
    # all_Announcement1 = PrivateAnnouncement.objects.all()
    # all_Announcement = all_Announcement1[::-1]
    try:
       user = request.user
       obj = UserProfile.objects.get(user=user)
    except:
      obj = request.user
    args = {'obj' : obj}
    return render(request, 'home.html',args)

def search(request):
  if request.method == 'POST':
    search_text = request.POST['search_text']
    all_Announcement1 = StudentsAnnouncement.objects.filter(student__contains=search_text)
    all_Announcement1 |= StudentsAnnouncement.objects.filter(rollnumber__contains=search_text)
  else:
    search_text = ''
    all_Announcement1 = StudentsAnnouncement.objects.all() 
  all_Announcement = all_Announcement1.order_by('-AnnouncementTime')
  return render(request, 'ajax-search.html', { 'all_Announcement': all_Announcement } )


def search1(request):
  if request.method == 'POST':
    search_text = request.POST['search_text']
    all_Announcement1 = PrivateAnnouncement.objects.filter(user__in=UserProfile.objects.filter(user__in=User.objects.filter(username__contains=search_text)))
    all_Announcement1 |= PrivateAnnouncement.objects.filter(poc_company__contains=search_text)
  else:
    search_text = ''
    all_Announcement1 = PrivateAnnouncement.objects.all() 
  all_Announcement = all_Announcement1.order_by('-AnnouncementTime')
  return render(request, 'ajax-search1.html', { 'all_Announcement': all_Announcement } )

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
  
class StudentsAnnouncementview(LoginRequiredMixin,CreateView):
     form_class = StudentsAnnouncementForm
     template_name = 'Student_Announcement_create.html'
     #success_url = reverse_lazy('portal')
     
     def form_valid(self, form):
          self.object = form.save(commit=False)
          obj = UserProfile.objects.get(user=self.request.user)
          self.object.user = obj
          obj1 = candidate.objects.get(roll_number=self.object.rollnumber)
          self.object.student = obj1.candidate_name
          self.object.save()
          return HttpResponseRedirect(reverse('portal'))
     
class PrivateAnnouncementview(LoginRequiredMixin,CreateView):
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
  
@login_required
def profile(request,pk=None):
      if pk:
           user = User.objects.get(pk=pk)
           obj = UserProfile.objects.get(user=user)
      else:
           user = request.user
           obj = UserProfile.objects.get(user=user)
      args = {'obj' : obj}
      return render(request,'profile.html',args)
    
@login_required
def studentprofile(request,pk):
      obj = candidate.objects.get(pk=pk)
      user = request.user
      obj1 = UserProfile.objects.get(user=user)
      args = {'obj' : obj, 'obj1' : obj1}
      return render(request,'studentprofile.html',args)

@login_required
def selectedstudents(request , **kwargs):
    context = {}
    pk = kwargs['pk']
    print("hi",pk)
    try:
        poc = get_object_or_404(UserProfile , pk = pk )
        company = poc.company
        context['shortlist'] = company.shortlist_candidate.all().filter( is_confirm = False)
        print(context['shortlist'])
        context['waitlist'] = company.waiting_candidate.all().filter( is_confirm = False)
        context['poc'] = poc
        context['id'] = pk
    except:
        pass  
    return render(request, 'selectedstudents.html' , context)
 
@login_required    
def UpdateProfile(request , pk , pk2):  
    candidate1 = get_object_or_404(candidate, pk=pk)
    form = UpdateCandidateDetail(instance=candidate1)
    user = request.user
    user_obj = UserProfile.objects.get(user=user)
    comp = user_obj.company.company_name
    if request.method == 'POST':
        form = UpdateCandidateDetail(instance=candidate1, data=request.POST)
        if form.is_valid():
            candidate1.start_time=timezone.now()
            print(candidate1.start_time)
            candidate1.expected_time = form.cleaned_data.get('expected_time')
            candidate1.company_name = comp
            candidate1.is_selected = form.cleaned_data.get('is_selected')
            candidate1.is_interview = True
            candidate1.save()
            if(candidate1.is_selected):
              x = Confirm(cand = candidate1,confirm1='0')
              x.save()
        return selectedstudents(request,pk=pk2)
    return render(request, 'UpdateCandidateDetail.html', {'form':form, 'patient':candidate})
    
@login_required
def ResetProfile(request, pk, pk2):
  candidate1 = get_object_or_404(candidate, pk=pk)
  candidate1.is_interview = False
  candidate1.start_time = None
  candidate1.expected_time = ""
  candidate1.company_name = ""
  candidate1.save()
  return selectedstudents(request,pk=pk2)

class AnnouncementDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = PrivateAnnouncement
    template_name = 'privateannouncement_confirm_delete.html'
    success_url = reverse_lazy('portal')

    def test_func(self):
        announcement = self.get_object()
        if self.request.user == announcement.user.user or self.request.user.is_superuser:
            return True
        return False
      
class StudentAnnouncementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = StudentsAnnouncement
    template_name = 'studentsannouncement_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        announcement = self.get_object()
        if self.request.user == announcement.user.user  or self.request.user.is_superuser: 
            return True
        return False

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
