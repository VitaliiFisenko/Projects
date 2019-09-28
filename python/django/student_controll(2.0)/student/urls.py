from django.urls import path

from student import views

urlpatterns = [

    path('profile/', views.StudentProfile.as_view(), name='student_profile')

]