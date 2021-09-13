from django.urls import path
from django.views.generic import TemplateView

from admin_app import views

urlpatterns = [
    path('adminloginpage/',TemplateView.as_view(template_name="badmin/homepage.html"),name="adminloginpage" ),
    path('adminlogin/',views.showadminwelcome,name='adminlogin'),
]
