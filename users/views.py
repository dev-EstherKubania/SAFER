from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegisterUserForm


# Create your views here.
def register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid:
            user = form.save()
            messages.success(request, 'Acount has been created succesfully')
            return redirect('login_user')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error, extra_tags='warning')
            return redirect('register')
    else:
        form = RegisterUserForm()
        context = {
            'form': form
        }
        return render(request, 'users/register_user.html', context)


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('login_user')

    return render(request, 'users/login_user.html')
