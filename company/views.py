from django.shortcuts import render

# Create your views here.
def auth_company(request):
    return render(request, 'Company.html')
