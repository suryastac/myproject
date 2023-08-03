import csv
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['userID']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    else:
        return render(request, 'login_user.html')
    
def logout_user(request):
    auth.logout(request)
    return redirect('home')


def home(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8')
        data = csv.reader(decoded_file.splitlines(), delimiter=',')
        headers = next(data)
        rows = list(data)
        return render(request, 'home.html', {'headers': headers, 'rows': rows})
    return render(request, 'home.html')