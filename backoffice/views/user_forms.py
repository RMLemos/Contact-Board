from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

from backoffice.forms import RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('backoffice:login')


    return render(
        request,
        'backoffice/register.html',
        {
            'form': form
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('backoffice:index')

    return render(
        request,
        'backoffice/login.html',
        {
            'form': form
        }
    )

def logout_view(request):
    auth.logout(request)
    return redirect('backoffice:login')