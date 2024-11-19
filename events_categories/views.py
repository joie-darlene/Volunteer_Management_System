from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Application
from .forms import EventForm  # Assuming you have a form created for the Event model
from volunteers.models import Volunteer  # Adjust this path if necessary
from django.contrib.auth.decorators import login_required

@login_required
def apply_to_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    volunteer = request.user
    
    # Check if the user is a volunteer and hasn't already applied
    if volunteer.role == 'volunteer' and not Application.objects.filter(event=event, volunteer=volunteer).exists():
        Application.objects.create(event=event, volunteer=volunteer)
        # Redirect to the event list or detail page
        return redirect('event_list')
    else:
        # Optionally handle cases where the user is not a volunteer or has already applied
        return redirect('event_list')  # Adjust as necessary


# List all events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'Event/event_list.html', {'events': events})

# Event detail view
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event/event_detail.html', {'event': event})

# Create a new event
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Adjust to your URL name for event list
    else:
        form = EventForm()
    return render(request, 'event/event_form.html', {'form': form})

# Update an event
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=pk)  # Adjust to your URL name for event detail
    else:
        form = EventForm(instance=event)
    return render(request, 'event/event_form.html', {'form': form})

# Delete an event
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')  # Adjust to your URL name for event list
    return render(request, 'event/event_confirm_delete.html', {'event': event})
