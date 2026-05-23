from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from faculty.models import FacultyProfile
from parent.models import ParentProfile
from student.models import StudentProfile


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'landing.html')


def home_redirect(request):
    return redirect('landing')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard_redirect(request):
    user = request.user
    if user.is_superuser or hasattr(user, 'adminprofile'):
        return redirect('admin_dashboard')
    if hasattr(user, 'studentprofile'):
        return redirect('student_dashboard')
    if hasattr(user, 'facultyprofile'):
        return redirect('faculty_dashboard')
    if hasattr(user, 'parentprofile'):
        return redirect('parent_dashboard')

    messages.warning(request, 'Your account has no role profile yet. Ask admin to assign one.')
    return redirect('landing')


@login_required
def dashboard(request):
    context = {
        'student_count': StudentProfile.objects.count(),
        'faculty_count': FacultyProfile.objects.count(),
        'parent_count': ParentProfile.objects.count(),
    }
    return render(request, 'admin/dashboard.html', context)
