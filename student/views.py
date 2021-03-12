from django.shortcuts import render

# Create your views here.
def auth_student(request):
    return render(request, 'student/Student.html')
