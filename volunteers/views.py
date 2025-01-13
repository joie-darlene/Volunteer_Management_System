from django.shortcuts import render, redirect, get_object_or_404 
from .models import Volunteer
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from .forms import VolunteerForm, VolunteerAuthForm

# View to display the list of volunteers

def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteers/volunteer_list.html', {'volunteers': volunteers, 'user': request.user})

def home(request):
    return render(request, 'layout.html')

def volunteer_register(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            
            # Redirect based on role
            if user.role == 'volunteer':
                return redirect('/login/')  # Adjust to the volunteer dashboard page
            elif user.role == 'recruiter':
                return redirect('/login/')  # Adjust to the recruiter dashboard page
    else:
        form = VolunteerForm()
    return render(request, 'volunteers/volunteer_form.html', {'form': form})

def volunteer_login(request):
    if request.method == 'POST':
        form = VolunteerAuthForm(request, data=request.POST)
        role = request.POST.get('role')  # Capture the selected role
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.role == role:  # Check role
                login(request, user)
                if user.role == 'volunteer':
                    return redirect('/event/')  
                elif user.role == 'recruiter':
                    return redirect('volunteers:volunteer_list')  # Corrected redirection
            else:
                # if user is not None and user.role == role:  # Check role
                #     login(request, user)
                #     # Redirect to appropriate dashboard based on role
                #     if user.role == 'volunteer':
                #         return redirect('/event/')
                #     elif user.role == 'recruiter':
                #         return redirect('/volunteers/')
                # else:
                messages.error(request, 'Invalid credentials or role.')
    else:
        form = VolunteerAuthForm()
    return render(request, 'volunteers/login.html', {'form': form})


def volunteer_logout(request):
    logout(request)  
    return redirect('volunteers:home') 

# View to edit an existing volunteer
def volunteer_edit(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    if request.method == 'POST':
        form = VolunteerForm(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
            return redirect('/volunteers')  # Redirects to /vols after editing
    else:
        form = VolunteerForm(instance=volunteer)
    return render(request, 'volunteers/volunteer_form.html', {'form': form, 'volunteer': volunteer})


# View to delete a volunteer
def volunteer_delete(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    if request.method == 'POST':
        volunteer.delete()
        return redirect('volunteer_list')  # Redirect to the list after deletion
    return render(request, 'volunteers/volunteer_confirm_delete.html', {'volunteer': volunteer})

   