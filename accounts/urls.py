from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from . import views


app_name = 'accounts'

urlpatterns = [
  path('login/',LoginView.as_view(), name='login'),
  path('logout/',LogoutView.as_view(), name='logout'),
  path('signup/', views.SignUpView.as_view(), name='signup'),
  path('edit/', views.CustomUserEdit, name='edit'),
  path('detail/<int:id>', views.CustomUserDetail, name='detail'),
]

