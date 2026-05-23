from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import FacultyProfile


@login_required
def dashboard(request):
    try:
        profile = FacultyProfile.objects.get(user=request.user)
    except FacultyProfile.DoesNotExist:
        messages.warning(request, 'This account is not a faculty account.')
        return redirect('dashboard')

    subjects = profile.subjects.all()

    return render(request, 'faculty/dashboard.html', {
        'profile': profile,
        'subjects': subjects,
    })
