from django.contrib.auth.models import User
from django.shortcuts import render

from .models import UserEmail
from .forms import RegisterForm

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if UserEmail.objects.get(email=form.cleaned_data.get('email')) and \
                    not User.objects.filter(email=form.cleaned_data.get('email')):
                User.objects.create(
                    email=form.cleaned_data.get('email'),
                    username=form.cleaned_data.get('email'),
                    password=form.cleaned_data.get('password'),
                    first_name=form.cleaned_data.get('first_name'),
                    last_name=form.cleaned_data.get('last_name'),
                    )

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})