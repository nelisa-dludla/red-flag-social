from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'title': 'Register',
        'form': form
    }

    return render(request, 'users/register.html', context=context)


@login_required
def profile(request):
    context = {
        'title': 'Profile'
    }
    return render(request, 'users/profile.html', context=context)
