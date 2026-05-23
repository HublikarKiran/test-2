from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Attendance, Mark, StudentProfile


def home(request):
    return render(request, 'student/home.html')


# @login_required
# def dashboard(request):
#     try:
#         profile = StudentProfile.objects.get(user=request.user)
#     except StudentProfile.DoesNotExist:
#         messages.warning(request, 'This account is not a student account.')
#         return redirect('dashboard')

#     marks = Mark.objects.filter(student=profile).order_by('subject')
#     attendance = Attendance.objects.filter(
#         student=profile).order_by('-date')[:10]

#     return render(request, 'student/dashboard.html', {
#         'profile': profile,
#         'marks': marks,
#         'attendance': attendance,
#     })
