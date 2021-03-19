from django.shortcuts import render, get_object_or_404

# Create your views here.

def home(request):
    # if request.user.is_authenticated:
    #     return render(request, 'StudentCompanyViewDetails.html')
    return render(request, 'index.html')

def internships(request):
    return render(request, 'StudentHomePage.html')

def detail(request):
    return render(request, 'StudentCompanyViewDetails.html')