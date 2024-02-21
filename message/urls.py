from django.urls import path
from . import views

app_name = "message"

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:room_id>', views.room, name='room'),
  path('direct/<int:user_id>', views.direct, name='direct'),
]
