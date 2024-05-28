from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegisterUserForm


# Create your views here.
def register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid:
            user = form.save()
            messages.success(request, 'Acount has been created succesfully')
            return redirect('login')
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


