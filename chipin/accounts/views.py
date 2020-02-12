from django.shortcuts import render
from django.contrib.auth import login, authenticate
from accounts.forms import SignUpForm, CreateValueForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def signup(request):
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
            return redirect('home')
        else:
            form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})