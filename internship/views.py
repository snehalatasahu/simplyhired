from django.shortcuts import render, get_object_or_404

# Create your views here.

def home(request):
    return render(request, 'internship/index.html')

def internships(request):
    return render(request, 'internship/StudentHomePage.html')

def detail(request):
    return render(request, 'internship/StudentCompanyViewDetails.html')