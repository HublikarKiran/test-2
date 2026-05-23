from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from student.models import Attendance, Mark

from .models import ParentProfile


@login_required
def dashboard(request):
    try:
        profile = ParentProfile.objects.get(user=request.user)
    except ParentProfile.DoesNotExist:
        messages.warning(request, 'This account is not a parent account.')
        return redirect('dashboard')

    children = profile.children.all()
    marks = Mark.objects.filter(student__in=children).order_by('student__roll_number', 'subject')
    attendance = Attendance.objects.filter(student__in=children).order_by('-date')[:20]

    return render(request, 'parent/dashboard.html', {
        'profile': profile,
        'children': children,
        'marks': marks,
        'attendance': attendance,
    })
