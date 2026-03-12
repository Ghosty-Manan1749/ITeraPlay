from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from movies.models import Movie
from accounts.models import Profile

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            profile = getattr(user, 'profile', None)
            if profile and profile.is_admin:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                return render(request, 'adminpanel/login.html', {'error': 'Unauthorized access'})
        return render(request, 'adminpanel/login.html', {'error': 'Invalid credentials'})
    return render(request, 'adminpanel/login.html')

@login_required(login_url='admin_login')
def admin_dashboard(request):
    # Verify the user is an admin
    if not getattr(request.user, 'profile', None) or not request.user.profile.is_admin:
        return redirect('home')
        
    movies = Movie.objects.all().order_by('-created_at')
    return render(request, 'adminpanel/dashboard.html', {'movies': movies})

@login_required(login_url='admin_login')
def upload_movie(request):
    # Verify the user is an admin
    if not getattr(request.user, 'profile', None) or not request.user.profile.is_admin:
        return redirect('home')
        
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        poster = request.FILES.get('poster')
        banner = request.FILES.get('banner')
        stream_link = request.POST.get('stream_link')
        download_link = request.POST.get('download_link')
        release_date = request.POST.get('release_date')
        is_trending = request.POST.get('is_trending') == 'on'
        is_new = request.POST.get('is_new') == 'on'
        
        Movie.objects.create(
            title=title,
            description=description,
            poster=poster,
            banner=banner,
            stream_link=stream_link,
            download_link=download_link,
            release_date=release_date,
            is_trending=is_trending,
            is_new=is_new
        )
        return redirect('admin_dashboard')
        
    return render(request, 'adminpanel/upload_movie.html')
