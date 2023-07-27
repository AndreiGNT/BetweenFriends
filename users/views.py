from django.shortcuts import render, redirect
<<<<<<< HEAD
from .forms import UserRegisterForm
=======
>>>>>>> 98546a065815404add54fa2d03a5922726efda34
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    template_name = 'users/register.html'

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, template_name, {'form': form})

