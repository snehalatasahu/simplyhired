from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.http import HttpResponse , JsonResponse
from .models import Student, Resume
from company.models import Company, Internship
from django.contrib import messages
 
 

def home(request):
    return render(request, 'index.html')

def internships(request):
    if request.user.is_authenticated:
        try:
            if (request.user.student.isStudent == True):
                posts = Internship.objects.order_by('-id')
                std = Student.objects.get(email=request.user.student.email)
                return render(request, 'StudentHomePage.html', {'posts':posts, 'student':std})
            else:
                messages.info(request, 'Please sign in as a student')
                return redirect(auth_student)
        except:
            messages.info(request, 'Some error occured. Please signin again')
            return redirect(auth_student)
    else:
        messages.info(request, 'Please signin to proceed')
        return redirect(auth_student)

def detail(request, post_id):
    std = Student.objects.get(email=request.user.student.email)
    post = Internship.objects.get(id=post_id)
    return render(request, 'StudentCompanyViewDetails.html', {'post':post, 'student':std})

def signin(request):
    password =  request.POST.get('password')
    username =  request.POST.get('username')
    if (request.POST.get('formtype') =='signupform'):
        username =  request.POST.get('email')

    user = auth.authenticate(username=username,password=password)

    
    if user is not None :
        try:
            if (user.student.isStudent == True ) :
                auth.login(request,user)
                print(user.student.name, 'logged in')
                return True
            else:
                return False

        except :
            return False

    else:
        return False


def auth_student(request):

    if request.method == 'POST':
        if (request.POST.get('formtype') =='signupform'):
            username = request.POST.get('email')
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password1 = request.POST.get('confpassword')
            fullname = name.split()
            firstname = fullname[0]
            lastname = fullname[-1]


            if password == password1:
                    if User.objects.filter(username=username).exists():
                        messages.info(request, 'User name already exists')
                        return redirect(auth_student)
                        # return HttpResponse('id exists')

                    else:
                        user = User.objects.create_user(username=username,first_name=firstname, last_name=lastname, password=password, email=email)
                        user.save()

                        newStudent = Student(user=user, name=name, email=email)
                        newStudent.save()
                        stdResume = Resume(student=newStudent)
                        stdResume.save()
                        # messages.info(request, 'User Created Successfully')
                        signin(request)
                        messages.info(request, 'Sucessfully Registered and signed in.')
                        return redirect('internships')

            # return redirect('login')

        elif (request.POST.get('formtype')=='signinform'):
            if signin(request):
                messages.info(request, "Signed in successfully")
                return redirect('internships')
            else:
                messages.info(request, "invlid credentials")
                return redirect(auth_student)


    else:
        return render(request,'Student.html')

@login_required
def profile(request):
    std = request.user.student
    resume = std.resume
    return render(request, 'StudentProfile.html', {'resume':resume, 'student':std})

@login_required
def profileEdit(request):

    std = request.user.student
    resume = std.resume
    if request.method == 'POST':
        email = request.POST.get('email')
        if email != std.email:
            if User.objects.filter(username=email).exists():
                messages.info(request, "This email is already in use")
            else:
                std.email = email
                request.user.email = email
                request.user.username = email         
            

        std.name = request.POST.get('name')
        fullname = std.name.split()
        request.user.first_name = fullname[0]
        request.user.last_name = fullname[-1]

        std.save()
        request.user.save()

        if 'image' in request.FILES:
            std.resume.pic = request.FILES['image']  

        std.resume.mob = request.POST.get('mob')
        std.resume.address = request.POST.get('address')
        std.resume.skills = request.POST.get('skills')
        std.resume.college = request.POST.get('college')
        std.resume.degree= request.POST.get('degree')
        std.resume.grad_year = request.POST.get('grad_year')
        std.resume.cgpa = request.POST.get('cgpa')
        std.resume.save()
        return redirect('profile')

    print(std.name)    
    return render(request, 'StudentProfileEdit.html', {'resume':resume, 'student':std})
    
@login_required
def dashboard(request):
    return render(request, 'StudentDashboard.html')
