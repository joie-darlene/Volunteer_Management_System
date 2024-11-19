from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('volunteers', views.volunteer_list, name='volunteer_list'),
    path('register/', views.volunteer_register, name='volunteer_register'),
    path('login/', views.volunteer_login, name='login'),  # Login URL
    path('<int:pk>/edit/', views.volunteer_edit, name='volunteer_edit'),
    path('<int:pk>/delete/', views.volunteer_delete, name='volunteer_delete'),
]
