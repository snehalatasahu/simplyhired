from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.http import HttpResponse , JsonResponse
from .models import Company, Internship
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
                    return render(request,'CompanyHomePage2.html')

            # return redirect('login')

        elif (request.POST.get('formtype')=='signinform'):
            if signin(request):
                messages.info(request, "Signed in successfully")
                return render(request,'CompanyHomePage2.html')
            else:
                messages.info(request, "invlid credentials....")
                return redirect(auth_company)
        else:
            messages.info(request, "invlid credentials here....")
            return redirect(auth_company)

            
    else:
        return render(request,'Company.html')


def home(request):
    return render(request,'CompanyHomePage2.html')

def post_detail(request):
    return render(request,'CompanyInternshipDetails.html')

def new_post(request):
    if request.method == 'POST':
        # print(request.user)
        # if request.user.is_authenticated:
        #     try:
        #         if (request.user.company.isCompany == True):
        #             title = request.POST.get('title')
        #             place = 'bbsr'
        #             duration = '2 Months'
        #             stipend = request.POST.get('stipend')
        #             apply_by = request.POST.get('apply_by') 
        #             no_of_openings =  request.POST.get('no_of_openings')
        #             perks = request.POST.get('perks')
        #             skills = request.POST.get('skills')
        #             about_internship = request.POST.get('about_internship')
        #             who_can_apply = request.POST.get('who_can_apply')

        #             newPost = Internship(company=request.user, title='title', place='place', duration='duration', stipend='stipend', apply_by='apply_by', no_of_openings='no_of_openings', perks='perks', skills='skills', about_internship='about_internship', who_can_apply='who_can_apply')
        #             newPost.save()
        #     except:
        #         return redirect(auth_company)
        #     # company = models.ForeignKey( 'Company' , on_delete=models.CASCADE)
            

        # else:
        #     return redirect(auth_company)
        title = request.POST.get('title')
        place = 'bbsr'
        duration = '2 Months'
        stipend = request.POST.get('stipend')
        apply_by = request.POST.get('apply_by') 
        no_of_openings =  request.POST.get('no_of_openings')
        perks = request.POST.get('perks')
        skills = request.POST.get('skills')
        about_internship = request.POST.get('about_internship')
        who_can_apply = request.POST.get('who_can_apply')

        newPost = Internship(title='title', place='place', duration='duration', stipend='stipend', apply_by='apply_by', no_of_openings='no_of_openings', perks='perks', skills='skills', about_internship='about_internship', who_can_apply='who_can_apply')
        newPost.save()

    return render(request,'CompanyInternshipForm.html')
    


