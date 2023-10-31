
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name="index"),
    path('new_course',views.new_course,name='new_course'),
    path('course',views.course,name='course'),
]
