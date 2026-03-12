from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user, is_admin=False)
        login(request, user)
        return redirect('home')
        
    return render(request, 'accounts/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            profile = getattr(user, 'profile', None)
            if profile and profile.is_admin:
                return redirect('admin_dashboard')
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
            
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})
