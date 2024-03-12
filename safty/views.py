from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import FormView,CreateView,TemplateView,View,UpdateView,DetailView,ListView
from django.urls import reverse
from django.utils import timezone
from django.utils.decorators import method_decorator 
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate,login,logout

from safty.models import *
from safty.forms import *

# from saftyapp.decorators import login_required

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib import messages
from django import forms
from django.urls import reverse_lazy


decs=[login_required,never_cache]

class RegisterUserView(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('signup') 

class UserIndexView(TemplateView):
    template_name="user_index.html"
 
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('user-index')  

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Invalid username or password.')
            return redirect('login')

# @method_decorator(decs,name="dispatch")
# class signoutView(View):
#     def get(self,request,*args,**kwargs):
#          logout(request)
#          return redirect("signi")
    
class CreateUserProfileView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'userprofile.html'
    success_url = reverse_lazy('user-index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreatepoliceProfileView(CreateView):
    model= PoliceProfile
    form_class = PoliceProfileForm
    template_name = 'add_policestation.html'
    success_url = reverse_lazy('user-index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
