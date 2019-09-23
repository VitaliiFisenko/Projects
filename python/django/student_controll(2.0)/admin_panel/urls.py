
from django.urls import path

from admin_panel import views

urlpatterns = [

    path('admin_panel/', views.AdminPanel.as_view(), name='admin_panel'),
    path('admin_panel/connection/', views.Connection.as_view(), name='connect_group-teacher'),
    path('admin_panel/connection/<str:choiced_departament>', views.Connection.as_view(), name='connect_group-teacher')

]
