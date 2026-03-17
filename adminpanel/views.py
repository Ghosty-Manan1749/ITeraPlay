from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from movies.models import Movie, Category
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
        if 'add_category' in request.POST:
            category_name = request.POST.get('name')
            if category_name:
                Category.objects.create(name=category_name)
            return redirect('upload_movie')

        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        poster = request.FILES.get('poster')
        banner = request.FILES.get('banner')
        stream_link = request.POST.get('stream_link')
        download_link = request.POST.get('download_link')
        release_date = request.POST.get('release_date')
        is_trending = request.POST.get('is_trending') == 'on'
        is_new = request.POST.get('is_new') == 'on'
        
        category = get_object_or_404(Category, id=category_id)

        Movie.objects.create(
            title=title,
            description=description,
            category=category,
            poster=poster,
            banner=banner,
            stream_link=stream_link,
            download_link=download_link,
            release_date=release_date,
            is_trending=is_trending,
            is_new=is_new
        )
        return redirect('admin_dashboard')
        
    categories = Category.objects.all()
    return render(request, 'adminpanel/upload_movie.html', {'categories': categories})

@login_required(login_url='admin_login')
def edit_movie(request, movie_id):
    if not getattr(request.user, 'profile', None) or not request.user.profile.is_admin:
        return redirect('home')
        
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        if 'add_category' in request.POST:
            category_name = request.POST.get('name')
            if category_name:
                Category.objects.create(name=category_name)
            return redirect('edit_movie', movie_id=movie.id)

        movie.title = request.POST.get('title')
        movie.description = request.POST.get('description')
        category_id = request.POST.get('category')
        if category_id:
            movie.category = get_object_or_404(Category, id=category_id)
        if request.FILES.get('poster'):
            movie.poster = request.FILES.get('poster')
        if request.FILES.get('banner'):
            movie.banner = request.FILES.get('banner')
        movie.stream_link = request.POST.get('stream_link')
        movie.download_link = request.POST.get('download_link')
        movie.release_date = request.POST.get('release_date')
        movie.is_trending = request.POST.get('is_trending') == 'on'
        movie.is_new = request.POST.get('is_new') == 'on'
        movie.save()
        return redirect('admin_dashboard')
        
    categories = Category.objects.all()
    return render(request, 'adminpanel/edit_movie.html', {'movie': movie, 'categories': categories})

@login_required(login_url='admin_login')
def delete_movie(request, movie_id):
    if not getattr(request.user, 'profile', None) or not request.user.profile.is_admin:
        return redirect('home')
        
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
    return redirect('admin_dashboard')
