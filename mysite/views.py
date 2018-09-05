import datetime
from django.shortcuts import render_to_response, render
from django.template.loader import render_to_string

from .models import TechoryzeAnalytics, Courses, CoursesTopic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.views.generic.base import TemplateView



def coursesTopic_view(request):
    if request.user.is_authenticated():

        if request.user.is_active:
            msg = None
            template = 'index.html'
            coursesTopic = CoursesTopic.objects.all()
            context = {'coursesTopic': coursesTopic,
                       'msg': msg,
                       'username':request.user.first_name}
            return render(request, template, context)
        else:
            msg = 'Account is not active. Check your email and active your account'
            template = 'index.html'
            coursesTopic = CoursesTopic.objects.all()
            context = {'coursesTopic': coursesTopic,
                       'msg': msg,
                       'username': request.user.first_name}
            return render(request, template, context)


    template = 'index.html'
    coursesTopic = CoursesTopic.objects.all()
    context = {'coursesTopic': coursesTopic}
    return render(request, template, context)

def courses_view(request, course_name):
    if request.user.is_authenticated():

        template = 'courses.html'
        if course_name == u'Productivity':
            courses = Courses.objects.filter(course_category = 'MOS')
            coursesTopic = CoursesTopic.objects.get(course_title = 'Productivity')
            context = {'courses': courses, 'courseTopic': coursesTopic }
            return render(request, template, context)
        elif course_name == u'Graphic_Design':
            courses = Courses.objects.filter(course_category='GD')
            coursesTopic = CoursesTopic.objects.get(course_title='Creative Design')
            context = {'courses': courses, 'courseTopic': coursesTopic}
            return render(request, template, context)
        elif course_name == u'Sound_Music':
            courses = Courses.objects.filter(course_category='SM')
            coursesTopic = CoursesTopic.objects.get(course_title='Sound & Music')
            context = {'courses': courses, 'courseTopic': coursesTopic}
            return render(request, template, context)
        elif course_name == u'Web_Site_Development':
            courses = Courses.objects.filter(course_category='WD')
            coursesTopic = CoursesTopic.objects.get(course_title='3D Modeling')
            context = {'courses': courses, 'courseTopic': coursesTopic}
            return render(request, template, context)
        elif course_name == u'Animation_Production':
            courses = Courses.objects.filter(course_category='AP')
            coursesTopic = CoursesTopic.objects.get(course_title='Animation Production')
            context = {'courses': courses, 'courseTopic': coursesTopic}
            return render(request, template, context)
        elif course_name == u'Video_Editing':
            courses = Courses.objects.filter(course_category='VE')
            coursesTopic = CoursesTopic.objects.get(course_title='Video Editing')
            context = {'courses': courses, 'courseTopic': coursesTopic}
            return render(request, template, context)

        else:
                    return HttpResponseRedirect("/")
    else:
            return HttpResponseRedirect("/logins")

def login_view(request):
    template = 'login.html'
    now = datetime.datetime.now()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        analytics = TechoryzeAnalytics.objects.create(AppID='1001', Username=username, AssetID='500',
                                       PageID='1', Page_Title='Login Page', Asset_Title='Login - Submit', Asset_Type='Button',
                                       DateTime=now)
        analytics.save()
        user = authenticate(username=username, password=password)
        request.session["user_name"] = username

        if user is not None:
            user1 = User.objects.get(username=username)
            if user1.is_active:
                auth.login(request, user)
                request.session["email"] = username
                request.session["email_c"] = ''
            # A backend authenticated the credentials
                return HttpResponseRedirect("/")
            else:
                messages.error(request,"Please activate your account first.")
                return HttpResponseRedirect("/logins")
        else:
            messages.error(request, "Invalid username and password.")
            return render(request, template)
    else:
        if "user_name" not in request.session:
            return render(request, template)
        email = request.session['user_name']
        user = User.objects.get(username=email)
        if user is not None:
            analytics = TechoryzeAnalytics.objects.create(AppID='1001', Username=request.session["user_name"],
                                                          AssetID='501',
                                                          PageID='1', Page_Title='Categories', Asset_Title='Sign Out',
                                                          Asset_Type='Button',
                                                          DateTime=now)
            analytics.save()
            auth.logout(request)


        return render(request, template)

def logout_view(request):
    # A backend authenticated the credentials

    return HttpResponseRedirect("logins")

def video_view(request, course_name, course_id):
    if request.user.is_authenticated():
        template = 'video.html'
        courses = Courses.objects.filter(pk=course_id)
        context = {'courses': courses }
        return render(request, template, context)

    else:
        return HttpResponseRedirect("/logins")

def activateaccount_view(request):
    template = 'activation.html'
    return render(request,template)

def createAccount_view(request):
    template = 'createnewAccount.html'
    if request.method == 'POST':
        email = request.POST['email']
        try:
            User.objects.get(username=email)
            messages.error(request, "Email address already exist.")
            return HttpResponseRedirect("createnewAccount")
        except User.DoesNotExist:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = request.POST['password']
            cPassword = request.POST['c_password']
            if password == cPassword:

                user = User.objects.create_user(email, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.is_active = False
                user.save()

                subject, from_email, to = 'Account Activation', 'noreply@techoryze.com', email


                html_content = render_to_string('activation.html').encode("utf-8")

                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                # msg = EmailMessage(subject,
                #                    html_content,
                #                    from_email, [to])
                msg.send()
                request.session['email'] = email
                #messages.success(request, "Verification email has been sent to your account. Please check your email.")
                return HttpResponseRedirect("createAcountconfrmMessage")
                # return HttpResponseRedirect("logins")
            else:
                messages.error(request, "Password and Confirm Password does not match.")
                return HttpResponseRedirect("createnewAccount")

    return render(request, template)

def forgotPassword_view(request):
    template = 'forgotPassword.html'
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(username=email)
        except User.DoesNotExist:
            user = None
            messages.error(request,"User with this email does not exist")
        
        if user is not None:
            request.session['email'] = email
            subject, from_email, to = 'Password Reset', 'noreply@techoryze.com', email

            html_content = render_to_string('resetPasswordSentEmailFormat.html').encode("utf-8")

            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            #messages.success(request, "A password reset link has been sent to your email.")

            return HttpResponseRedirect("resetpassconfrmMessage")

        else:
            return HttpResponseRedirect("forgotPassword")

    return render(request, template)

def resetPassword_view(request):
    template = 'resetPassword.html'
    if request.method == 'POST':
        password = request.POST["password"]
        email = request.session['email']
        try:

            user = User.objects.get(username=email)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect("logins")
        except:
            return render(request, template)

    return render(request, template)

def ChatterBotAppView(request):
    template = "chatterbot.html"
    if request.user.is_authenticated():
        username = request.user.first_name
        context = {'username': username}
        return render(request, template, context)

def CourseSeries(request,course_id):
    if request.user.is_authenticated():
        template = "CoursesSeries.html"
        courses = Courses.objects.filter(pk=course_id)
        context = {'courses': courses}
        return render(request, template, context)

    else: return HttpResponseRedirect("/logins")

def view_confirm(request):
    template = "login.html"
    email = request.session["email"]

    user = User.objects.get(username=email)
    if user is not None:
        request.session["email_c"] = email
        user.is_active = True
        user.save()
        return HttpResponseRedirect("/logins")

def view_about_us(request):
        template = "AboutUs.html"
        return render(request, template)
       # return HttpResponseRedirect("/AboutUs")


def view_analytics(request):
    template = "Analytics.html"
    techoryze_tracking = TechoryzeAnalytics.objects.raw('SELECT id, Username, Page_Title, Asset_Title, COUNT(AssetID) as Views from mysite_techoryzeanalytics group by Asset_Title')
    context = {'data':techoryze_tracking}
    return render(request, template, context)

def view_forgot_message(request):
    template = "resetpassconfrmMessage.html"
    return render(request,template)

def view_create_account_confirmatio_message(request):
    template = "createAcountconfrmMessage.html"
    return render(request,template)

def view_password_reset_format(request):
    template = "resetPasswordSentEmailFormat.html"
    return render(request,template)

def view_conatact_us(request):
    template = "ContactUS.html"
    return  render(request,template)

def view_privacy_policy(request):
    template = "PrivacyPolicy.html"
    return  render(request,template)

def view_instructor(request):
    template = "instructor.html"
    return  render(request,template)

def view_blog(request):
    template = "Blog.html"
    return  render(request,template)

<<<<<<< HEAD
def view_safari(request):
    template = "safarivideo.html"
    return  render(request,template)
=======
def safariview(request):
    template = "safarivideo.html"
    return  render(request,template)
>>>>>>> c941cdec99f56e15f79f3e64f7f7c71673ff1a5a
