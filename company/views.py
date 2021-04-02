from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.http import HttpResponse , JsonResponse
from .models import Company, Internship, Profile
from django.contrib import messages
 
 
def signin(request):
    password =  request.POST.get('password')    
    username =  request.POST.get('username')
    if (request.POST.get('formtype') =='signupform'):
        username =  request.POST.get('email')
    print(username, password)

    user = auth.authenticate(username=username,password=password)

    
    if user is not None :
        try:
            if (user.company.isCompany == True ) :
                auth.login(request,user)
                print(user.company.name, 'logged in')
                return True
            else:
                print("not company")
                return False

        except :
            print("company error")
            return False

    else:
        print("not user")
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

                    newProfile = Profile(company=newCompany)
                    newProfile.save()
                    # messages.info(request, 'User Created Successfully')
                    signin(request)
                    messages.info(request, 'Sucessfully Registered and signed in.')
                    return redirect(home)

            # return redirect('login')

        elif (request.POST.get('formtype')=='signinform'):
            if signin(request):
                messages.info(request, "Signed in successfully")
                return redirect(home)
            else:
                messages.info(request, "invlid credentials....")
                return redirect(auth_company)
        else:
            messages.info(request, "invlid credentials here....")
            return redirect(auth_company)

            
    else:
        return render(request,'Company.html')


def home(request):
    if request.user.is_authenticated:
        try:
            if (request.user.company.isCompany == True):
                comp = Company.objects.get(email=request.user.company.email)
                print(comp)
                posts = Internship.objects.filter(company=comp)
                print(posts)
                return render(request, 'CompanyHomePage2.html', {'posts':posts, 'company':comp})
            else:
                messages.info(request, 'Please sign in as a company')
                return redirect(auth_company)
        except:
            print(request.user.company.isCompany, request.user.company)
            messages.info(request, 'Some error occured. Please signin again')
            return redirect(auth_company)
    else:
        messages.info(request, 'Please signin to proceed')
        return redirect(auth_company)

def post_detail(request, post_id):
    comp = Company.objects.get(email=request.user.company.email)
    post = Internship.objects.get(id=post_id)
    print(post, comp)
    return render(request, 'CompanyInternshipDetails.html', {'post':post, 'company':comp})

def new_post(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                if (request.user.company.isCompany == True):
                    title = request.POST.get('title')
                    place = 'bbsr'
                    duration = '2 Months'
                    stipend = request.POST.get('stipend')
                    # apply_by = request.POST.get('apply_by') 
                    no_of_openings =  request.POST.get('no_of_openings')
                    perks = request.POST.get('perks')
                    skills = request.POST.get('skills')
                    about_internship = request.POST.get('about_internship')
                    who_can_apply = request.POST.get('who_can_apply')
                    comp = Company.objects.get(email=request.user.company.email)
                    newPost = Internship(company=comp, title=title, place=place, duration=duration, stipend=stipend, no_of_openings=no_of_openings, perks=perks, skills=skills, about_internship=about_internship, who_can_apply=who_can_apply)
                    # newPost = Internship(company=request.user, title='title', place='place', duration='duration', stipend='stipend', apply_by='apply_by', no_of_openings='no_of_openings', perks='perks', skills='skills', about_internship='about_internship', who_can_apply='who_can_apply')
                    newPost.save()
            except:
                print('4 ', request.user, request.user.company.isCompany, request.user.is_authenticated)
                return redirect(auth_company)
            # company = models.ForeignKey( 'Company' , on_delete=models.CASCADE)
            

        else:
            print('4 ', request.user, request.user.company.isCompany, request.user.is_authenticated)
            return redirect(auth_company)
        # title = request.POST.get('title')
        # place = 'bbsr'
        # duration = '2 Months'
        # stipend = request.POST.get('stipend')
        # # apply_by = request.POST.get('apply_by') 
        # no_of_openings =  request.POST.get('no_of_openings')
        # perks = request.POST.get('perks')
        # skills = request.POST.get('skills')
        # about_internship = request.POST.get('about_internship')
        # who_can_apply = request.POST.get('who_can_apply')

        # newPost = Internship(title=title, place=place, duration=duration, stipend=stipend, no_of_openings=no_of_openings, perks=perks, skills=skills, about_internship=about_internship, who_can_apply=who_can_apply)
        # newPost.save()

    return render(request,'CompanyInternshipForm.html')
    
@login_required
def company_profile(request):
    cmp = request.user.company
    profile = cmp.profile
    return render(request, 'CompanyProfile.html', {'profile':profile, 'company':cmp})

@login_required
def company_profile_edit(request):
    cmp = request.user.company
    profile = cmp.profile
    if request.method == 'POST':
        print(cmp)
        email = request.POST.get('email')
        if email != cmp.email:
            if User.objects.filter(username=email).exists():
                messages.info(request, "This email is already in use")
            else:
                cmp.email = email
                request.user.email = email
                request.user.username = email         
            

        cmp.name = request.POST.get('name')
        fullname = cmp.name.split()
        request.user.first_name = fullname[0]
        request.user.last_name = fullname[-1]

        cmp.save()
        request.user.save()

        if 'image' in request.FILES:
            cmp.profile.pic = request.FILES['image']  

        cmp.profile.mob = request.POST.get('mob')
        cmp.profile.address = request.POST.get('address')
        cmp.profile.website = request.POST.get('website')

        cmp.profile.no_of_employees = request.POST.get('no_of_employees')
        cmp.profile.internship_post= request.POST.get('internship_post')
        cmp.profile.interns_hired = request.POST.get('interns_hired')

        cmp.profile.facebook_link = request.POST.get('facebook_link')
        cmp.profile.twitter_link = request.POST.get('twitter_link')
        cmp.profile.linkedin_link = request.POST.get('linkedin_link')
        cmp.profile.youtube_link = request.POST.get('youtube_link')

        cmp.profile.about = request.POST.get('about')

        cmp.profile.save()
        return redirect('company-profile')
  
    return render(request, 'CompanyProfileEdit.html', {'profile':profile, 'company':cmp})


