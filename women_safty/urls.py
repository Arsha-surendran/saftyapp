"""
URL configuration for women_safty project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from safty.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/",RegisterUserView.as_view(),name="signup"),
    path("login/",LoginView.as_view(),name="login"),
    path("adminindex/",AdminIndexView.as_view(),name="admin-index"),
    path("userindex/",UserIndexView.as_view(),name="user-index"),
    path("policeindex/",PoliceIndexView.as_view(),name="police-index"),
    path("add/profile",CreateUserProfileView.as_view(),name="add-profile"),
    path("add/policeprofile",CreatepoliceProfileView.as_view(),name="add-policeprofile"),
    path("signout/",signoutView.as_view(),name="signout"),
    path("complaint/",ComplaintView.as_view(),name="add-complaint") ,
    path('complaint/<int:pk>/change',ComplaintUpdateView.as_view(),name="complaint_change"),
    path("complaintlist/",ComplaintListView.as_view(), name="complaint-detail"),
    path("nearbystation/",NearbyStationView.as_view(),name='nearby-station'),
    path("saftytips/",SaftytipsView.as_view(),name='safty_tips'),
    path("saftytipsview/",SafetyTipListView.as_view(),name="saftytipsview"),
    path("policedetail/",PoliceDetailView.as_view(),name='police_detail'),
    path("policeupdate/<int:pk>/change/",PoliceUpdateView.as_view(),name="police-update"),
    path("policedelete/<int:pk>/remove/",PoliceDeleteView.as_view(),name="police-delete"),
    path("emailalert/",EmailAlertView.as_view(),name='email_alert'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
