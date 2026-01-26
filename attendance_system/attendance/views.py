from django.shortcuts import render, redirect
from .models import Student

def home(request):
    return render(request, 'attendance/home.html')

def register_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll = request.POST.get('roll')

        Student.objects.create(
            name=name,
            roll_number=roll
        )
        return redirect('home')

    return render(request, 'attendance/register.html')

def start_attendance(request):
    return render(request, 'attendance/start.html')

def view_attendance(request):
    return render(request, 'attendance/attendance_view.html')
