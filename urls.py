
//Global URLs 

from django.contrib import admin
from django.urls import path, include
from content.views import RegisterView
from content import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('content.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.RegisterView.as_view(), name='register'),
]
