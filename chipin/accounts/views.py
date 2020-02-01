from django.shortcuts import render
from django.contrib.auth import login, authenticate
from accounts.forms import SignUpForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView

def profile_view(request):
    return render(request, 'profile.html')

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('login.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def get(self, request):
    """ returns landing page. """
    return render(request, 'profile.html')

