# C:\Users\LENOVO\Desktop\rental_marketplace\users\views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        print("--- POST request received for signup ---")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("--- Form is VALID ---")
            user = form.save()
            login(request, user)
            print(f"--- User {user.username} successfully signed up and logged in ---")
            return redirect('core:index')
        else:
            print("--- Form is INVALID ---")
            print("Form errors:", form.errors) # Print specific field errors
            print("Non-field errors:", form.non_field_errors()) # Print general form errors
    else:
        print("--- GET request received for signup ---")
        form = CustomUserCreationForm()

    return render(request, 'users/signup.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('core:index') # Redirect to homepage after successful login
            else:
                # Add a non-field error if authentication fails
                form.add_error(None, "Invalid username or password.")
        # If form is not valid or authentication fails, re-render the form with errors
        return render(request, 'users/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('core:index') # Redirect to homepage after logout
