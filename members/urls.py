
from django.urls import path
from .views import UserRegisterViews
#rom.import views
app_name='members'
urlpatterns = [
    path('register/',UserRegisterViews.as_view(),name='register'),

]