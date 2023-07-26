from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    template_name = 'users/register.html'
    form = UserCreationForm()
    return render(request, template_name, {'form': form})

