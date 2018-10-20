from django.shortcuts import render, redirect
from .form import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Employee, Booking, Location, Rate
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'coolie/signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'coolie/home.html')


def reserve(request):
    return render(request, 'coolie/list.html')


def destination(request):
    railway = request.POST.get('boarding_station')
    coolie = Employee.objects.all()
    avail = Available.objects.filter(id=coolie.id).value_list('avail', flat=True)
    return render(request, 'coolie/destination.html')