from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.http import HttpResponse , JsonResponse
from .models import Company
from django.contrib import messages
 
 
def signin(request):
    password =  request.POST.get('password')
    username =  request.POST.get('username')

    user = auth.authenticate(username=username,password=password)

    
    if user is not None :
        try:
            if (user.company.isCompany == True ) :
                auth.login(request,user)
                print(user.company.name, 'logged in')
                return True
            else:
                return False

        except :
            return False

    else:
        return False


def auth_company(request):

    if request.method == 'POST':
        if (request.POST.get('formtype') =='signupform'):
            username = request.POST.get('email')
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password1 = request.POST.get('confpassword')

            if password == password1:
                    if User.objects.filter(username=username).exists():
                        messages.info(request, 'User name already exists')
                        return redirect(auth_company)
                        # return HttpResponse('id exists')

                    else:
                        user = User.objects.create_user(username=username,first_name=name, password=password, email=email)
                        user.save()

                        newCompany = Company(user=user, name=name, email=email)
                        newCompany.save()
                        # messages.info(request, 'User Created Successfully')
                        signin(request)
                        messages.info(request, 'Sucessfully Registered and signed in.')
                        return redirect('home')

            # return redirect('login')

        elif (request.POST.get('formtype')=='signinform'):
            if signin(request):
                messages.info(request, "Signed in successfully")
                return redirect('home')
            else:
                messages.info(request, "invlid credentials")
                return redirect(auth_company)


    else:
        return render(request,'Company.html')
    


