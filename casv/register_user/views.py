# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _

from .models import UserEmail
from .forms import RegisterForm


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                UserEmail.objects.get(email=email)
                if User.objects.filter(email=email).count() == 0:
                    user = User.objects.create(
                        email=email,
                        username=email,
                        first_name=form.cleaned_data.get('first_name'),
                        last_name=form.cleaned_data.get('last_name'),
                        )
                    user.set_password(form.cleaned_data.get('password'))
                    user.save()
                    msg = _('Your account was created successfully! Please login below.')
                    return redirect('core:login')
                else:
                    msg = 'The email you submitted is already registered in the system.'
                    return render(request, 'register.html', {'form': form, 'msg': msg})
            except UserEmail.DoesNotExist:
                msg = _('The email you submitted is not allowed to register.')
                return render(request, 'register.html', {'form': form, 'msg': msg})

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form, 'msg': ''})