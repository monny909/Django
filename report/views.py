# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import  AddReportForm, AddNewsForm, AddCasesForm, AddSchoolForm, AddActivityForm, RegisterForm, ProfileForm, loginForm
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib import messages
from .models import Report, News, Cases, Activity, Institution
from django.contrib.auth.models import User



#------------------------------------------------------------------------------
def index(request):
    if request.user.is_authenticated():
        if request.user.is_superuser or request.user.is_staff:
            return redirect("admin_home")
        else:
            return redirect("user_home")
    return render(request, 'report/index.html', {})
#------------------------------------------------------------------------------
def user_home(request):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    return render(request, 'report/user_home.html', {})


#------------------------------------------------------------------------------
def admin_home(request):

    return render(request, 'report/admin_home.html', {})


#------------------------------------------------------------------------------
def user_data(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    user_reports = Report.objects.filter(username = request.user).order_by('-id')
    context = {
        'user_reports': user_reports,
    }
    return render(request, 'report/view_user_data.html', context)


#------------------------------------------------------------------------------
def add_report(request):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")

    form = AddReportForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.username = request.user
            instance.institution = request.user.profile.institution
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'report/form_temp.html', context)

#------------------------------------------------------------------------------
def add_school(request):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    elif not request.user.is_superuser:
        messages.error(request, 'أنت لاتمتلك الصلاحيات!')
        return redirect("home")

    if request.method == 'POST':
        form = AddSchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddSchoolForm()

    context = {
        'form': form
    }
    return render(request, 'report/add_school.html', context )

#------------------------------------------------------------------------------
def edit_school(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    instance = get_object_or_404(Institution,id=id)
    form = AddSchoolForm(request.POST or None, instance=instance)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect("/my-school")
    context = {
        'reports': instance,
        'form': form,
    }
    return render(request, 'report/form_temp3.html', context)

#------------------------------------------------------------------------------
def delete_school(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    instance = get_object_or_404(Institution,id=id)
    instance.delete()
    return redirect("admin_home")


#------------------------------------------------------------------------------
def school_data(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    school_data = Institution.objects.order_by('-id')
    context = {
        'school_data': school_data,
    }
    return render(request, 'report/view_school_data.html', context)

#------------------------------------------------------------------------------
def add_news(request):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")

    form = AddNewsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.username = request.user
            instance.institution = request.user.profile.institution
            instance.save()
            return redirect("news")
    context = {
        'form': form,
    }
    return render(request, 'report/form_temp_news.html', context)

#------------------------------------------------------------------------------
def edit_news(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    instance = get_object_or_404(News,id=id)
    form = AddNewsForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect("/my-news")
    context = {
        'reports': instance,
        'form': form,
    }
    return render(request, 'report/form_temp_news.html', context)

#------------------------------------------------------------------------------
def delete_news(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    instance = get_object_or_404(News,id=id)
    instance.delete()
    return redirect("admin_home")

#------------------------------------------------------------------------------
def news_data(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    news_data = News.objects.filter(username = request.user).order_by('-id')
    context = {
        'news_data': news_data,
    }
    return render(request, 'report/view_news_data.html', context)


#------------------------------------------------------------------------------
def add_cases(request):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")

    form = AddCasesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.username = request.user
            instance.institution = request.user.profile.institution
            instance.save()
            return redirect("cases")
    context = {
        'form': form,
    }
    return render(request, 'report/form_temp.html', context)

#------------------------------------------------------------------------------
def edit_cases(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    instance = get_object_or_404(Cases,id=id)
    form = AddReportForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect("/my-cases")
    context = {
        'reports': instance,
        'form': form,
    }
    return render(request, 'report/form_temp.html', context)

#------------------------------------------------------------------------------
def delete_cases(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    instance = get_object_or_404(Cases,id=id)
    instance.delete()
    return redirect("admin_home")

#------------------------------------------------------------------------------
def cases_data(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    cases_data = Cases.objects.filter(username = request.user).order_by('-id')
    context = {
        'cases_data': cases_data,
    }
    return render(request, 'report/view_cases_data.html', context)
#------------------------------------------------------------------------------
def delete_report(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    instance = get_object_or_404(Report,id=id)
    instance.delete()
    return redirect("user_reports")


#------------------------------------------------------------------------------
def edit_report(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    instance = get_object_or_404(Report,id=id)
    form = AddReportForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'reports': instance,
        'form': form,
    }
    return render(request, 'report/form_temp.html', context)


#------------------------------------------------------------------------------
def view_report(request):
    reports = Report.objects.order_by('-id')
    context = {
        'reports': reports,
    }

    return render(request, 'report/view_report.html', context)


#------------------------------------------------------------------------------
def news(request):

    news = News.objects.order_by('-id')
    context = {
        'news': news,
    }

    return render(request, 'report/news.html', context)

#------------------------------------------------------------------------------
def cases(request):

    cases = Cases.objects.order_by('-id')
    context = {
        'cases': cases,
    }

    return render(request, 'report/cases.html', context)

#------------------------------------------------------------------------------
def view_case(request, id=None):

    instance = get_object_or_404(Cases,id=id)
    context = {
        'instance': instance,

    }
    return render(request, 'report/view_case.html', context)
#------------------------------------------------------------------------------
def activity(request):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    activities = Activity.objects.order_by('-id')
    context = {
        'activities': activities,
    }

    return render(request, 'report/activity.html', context)

#-----------------------------------------------------------------------------
def add_activity(request):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")

    form = AddActivityForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.username = request.user
            instance.save()
            return redirect("activity")
    context = {
        'form': form,
    }
    return render(request, 'report/form_temp2.html', context)

#------------------------------------------------------------------------------
def edit_activity(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    instance = get_object_or_404(Activity,id=id)
    form = AddActivityForm(request.POST or None, instance=instance)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.save()
            return redirect("activity")
    context = {
        'reports': instance,
        'form': form,
    }
    return render(request, 'report/form_temp2.html', context)

#------------------------------------------------------------------------------
def delete_activity(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    instance = get_object_or_404(Activity,id=id)
    instance.delete()
    return redirect("admin_home")

#------------------------------------------------------------------------------
def activity_data(request, id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'أنت لم تقم بتسحيل الدخول!')
        return redirect("home")
    activities_data = Activity.objects.order_by('-id')
    context = {
        'activities_data': activities_data,
    }
    return render(request, 'report/view_activity_data.html', context)

#------------------------------------------------------------------------------
def view_single_article(request, id=None):

    instance = get_object_or_404(News,id=id)
    context = {
        'instance': instance,

    }
    return render(request, 'report/view_single_article.html', context)

#------------------------------------------------------------------------------
def view_single_report(request, id=None):
    instance = get_object_or_404(Report,id=id)
    context = {
        'instance': instance,

    }
    return render(request, 'report/view_single_report.html', context)
