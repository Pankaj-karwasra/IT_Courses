from django.http import HttpResponse
from django.shortcuts import render,redirect
from get_in_touch.models  import get_in_touch
from top_touch.models import top_touch
from aboutus.models import aboutus
from contactus.models import contactus
from OurCourses.models import OurCourses
from Choose_TD.models import Choose_TD
from Choose_image.models import Choose_image
from Choose_US.models import Choose_US
from Choose_US1.models import Choose_US1
from Choose_US2.models import Choose_US2
from Team.models import Team
from Testimonial.models import Testimonial
from students.models import students
from categories.models import categories
from Recent.models import Recent
from course_details.models import course_details
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def homepage(request):
    touch=get_in_touch.objects.all()
    top=top_touch.objects.all()
    context={'touch':touch,'top':top}
    return render(request,'index.html',context)


def home(request):
    touch=get_in_touch.objects.all()
    top=top_touch.objects.all()
    context={'touch':touch,'top':top}
    return render(request,'index.html',context)


def about(request):
    touch=get_in_touch.objects.all()
    top=top_touch.objects.all() 
    about=aboutus.objects.all()
    context={'touch':touch,'top':top,'about':about}
    return render(request,'about.html',context)


def contact(request):
    touch=get_in_touch.objects.all()
    top=top_touch.objects.all() 
    contact_info=contactus.objects.all()
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact_save=contactus(name=name,email=email,subject=subject,message=message)
        contact_save.save()
        return redirect('contact')
    context={'touch':touch,'top':top,'contact_info':contact_info}
    return render(request,'contact.html',context)

def course(request):
    touch=get_in_touch.objects.all()
    top=top_touch.objects.all() 
    course_next=OurCourses.objects.all()
    context={'touch':touch,'top':top,'course_next':course_next}
    return render(request,'course.html',context)


def detail(request):
    touch=get_in_touch.objects.all()
    top=top_touch.objects.all() 
    cat=categories.objects.all()
    recent=Recent.objects.all()
    info_detail=course_details.objects.all()
    context={'touch':touch,'top':top,'cat':cat,'recent':recent,'info_detail':info_detail}
    return render(request,'detail.html',context)


def feature(request):
    touch=get_in_touch.objects.all()
    top=top_touch.objects.all() 
    choose=Choose_TD.objects.all()
    choose_img=Choose_image.objects.all()
    choose_us=Choose_US.objects.all()
    choose_us1=Choose_US1.objects.all()
    choose_us2=Choose_US2.objects.all()
    context={'touch':touch,'top':top,'choose':choose,'choose_img':choose_img,'choose_us':choose_us,'choose_us1':choose_us1,'choose_us2':choose_us2}
    return render(request,'feature.html',context)

def team(request):
    touch=get_in_touch.objects.all()
    top=top_touch.objects.all() 
    team_dic=Team.objects.all()
    context={'touch':touch,'top':top,'team_dic':team_dic}
    return render(request,'team.html',context)

def testimonial(request):
    touch=get_in_touch.objects.all()
    top=top_touch.objects.all() 
    testimonial_dic=Testimonial.objects.all()
    st_dic=students.objects.all()
    context={'touch':touch,'top':top,'testimonial_dic':testimonial_dic,'st_dic':st_dic}
    return render(request,'testimonial.html',context)

def pages(request):
    return render(request,'pages.html')

def privacy(request):
    touch=get_in_touch.objects.all()
    top=top_touch.objects.all()
    context={'touch':touch,'top':top}
    return render(request,'privacy.html',context)


@login_required(login_url='/login/')
def register(request):
   if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=User.objects.filter(username=username)

        if user.exists():
            messages.error(request,'Username already taken')
            return redirect('register')
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        user.set_password(password)
        user.save()

        messages.info(request,'Account created Successfully')
        return redirect('register')
    
   return render(request,'register.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return redirect("/login/")
        user = authenticate(request,username=username, password=password)
        if user is None:
            messages.error(request, "password and username note match")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/")
    return render(request, "login.html")

 
def logout_page(request):
    logout(request)
    return render(request,'logout.html')