from django.contrib import admin
from django.urls import path
from events_categories import views as event_views  # Import views from the event app

urlpatterns = [
    
    # Event URLs
     path('', event_views.event_list, name='event_list'),
    path('apply/<int:pk>/', event_views.apply_to_event, name='apply_to_event'),
  path('event/create/', event_views.event_create, name='event_create'),
    path('event/<int:pk>/', event_views.event_detail, name='event_detail'),
    path('event/<int:pk>/edit/', event_views.event_update, name='event_update'),  
    path('event/<int:pk>/delete/', event_views.event_delete, name='event_delete'),  
]
