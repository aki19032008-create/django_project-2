from django.shortcuts import render, redirect
from .models import Student

# Home page
def home(request):
    return render(request, 'attendance/home.html')


# Register student page
def register_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll = request.POST.get('roll')

        if name and roll:
            Student.objects.create(
                name=name,
                roll_number=roll
            )

        return redirect('home')

    return render(request, 'attendance/register.html')


# Start attendance (camera page)
def start_attendance(request):
    return render(request, 'attendance/start.html')


# View attendance records
def view_attendance(request):
    students = Student.objects.all()
    return render(
        request,
        'attendance/attendance_view.html',
        {'students': students}
    )