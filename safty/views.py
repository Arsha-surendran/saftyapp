from django.shortcuts import render
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


from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

decs=[login_required,never_cache]

class RegisterUserView(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login') 

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


# class LoginView(FormView):
#     template_name = 'login.html'
#     form_class = LoginForm
#     success_url = reverse_lazy('police-index')  

#     def form_valid(self, form):
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']

#         user = authenticate(self.request, username=username, password=password)
#         if user is not None:
#             login(self.request, user)
#             return super().form_valid(form)
#         else:
#             messages.error(self.request, 'Invalid username or password.')
#             return redirect('login')

class signoutView(View):
    def get(self,request,*args,**kwargs):
         logout(request)
         return redirect("login")
    
class CreateUserProfileView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'userprofile.html'
    success_url = reverse_lazy('user-index')

    def get_object(self, queryset=None):
        # Get the profile object for the current user if it exists, otherwise return None
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateUserProfileView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'userprofile.html'
    success_url = reverse_lazy('user-index')

    def get_object(self, queryset=None):
        # Get the profile object for the current user if it exists, otherwise return None
        return UserProfile.objects.get_or_create(user=self.request.user)[0]


class CreatepoliceProfileView(CreateView):
    model= PoliceProfile
    form_class = PoliceProfileForm
    template_name = 'add_policestation.html'
    success_url = reverse_lazy('user-index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ComplaintView(CreateView):
    model= Complaint
    form_class = ComplaintForm
    template_name = 'complaint.html'
    success_url = reverse_lazy('user-index')

    def form_valid(self, form):
        form.instance.complainant = self.request.user
        return super().form_valid(form)

class PoliceIndexView(TemplateView):
    template_name="police_index.html"


class NearbyStationView(TemplateView):
    template_name = "nearby_station.html"


class SaftytipsView(CreateView):
    model= Saftytips
    form_class = SaftytipsForm
    template_name = 'safty_tips.html'
    success_url = reverse_lazy('user-index')

class PoliceDetailView(TemplateView):
    template_name = "policedetails.html"


class AdminIndexView(TemplateView):
    template_name="admin_index.html"


class EmailAlertView(View):
    def post(self, request):
        recipient_email = request.POST.get('recipient_email')  # Assuming the email is submitted via a form field
        alert_details = request.POST.get('alert_details')  # Assuming the alert details are submitted via a form field

        subject = 'Emergency Alert'
        html_message = render_to_string('email_alert.html', {'alert_details': alert_details})
        plain_message = strip_tags(html_message)
        from_email = 'your-from-email@example.com'  # Replace with your "from" email address
        send_mail(subject, plain_message, from_email, [recipient_email], html_message=html_message)

        # Optionally, you can return a JSON response indicating success or failure
        return JsonResponse({'message': 'Email sent successfully'}, status=200)



class ComplaintDetailView(DetailView):
    template_name="complaintview.html"
    model=Complaint
    context_object_name="data"
