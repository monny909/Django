"""reports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'report/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admin-home/$', views.admin_home, name='admin_home'),
    url(r'^user-home/$', views.user_home, name='user_home'),
    url(r'^create-reports/$', views.add_report, name='add_reports'),
    url(r'^add-school/$', views.add_school, name='add_school'),
    url(r'^my-school/$', views.school_data, name='school_data'),
    url(r'^my-school/(?P<id>\d+)/edit$', views.edit_school, name='edit_school'),
    url(r'^my-school/(?P<id>\d+)/delete$', views.delete_school, name='delete_school'),
    url(r'^add-news/$', views.add_news, name='add_news'),
    url(r'^add-cases/$', views.add_cases, name='add_cases'),
    url(r'^user-reports/$', views.user_data, name='user_reports'),
    url(r'^user-reports/(?P<id>\d+)/edit$', views.edit_report, name='user_edit_reports'),
    url(r'^user-reports/(?P<id>\d+)/delete$', views.delete_report, name='delete_reports'),
    url(r'^view-reports/(?P<id>\d+)$', views.view_single_report, name='view_single_report'),
    url(r'^news/$', views.news, name='news'),
    url(r'^news/(?P<id>\d+)$', views.view_single_article, name='view_single_report'),
    url(r'^my-news/$', views.news_data, name='news_data'),
    url(r'^my-news/(?P<id>\d+)/edit$', views.edit_news, name='edit_news'),
    url(r'^my-news/(?P<id>\d+)/delete$', views.delete_news, name='delete_news'),
    url(r'^cases/$', views.cases, name='cases'),
    url(r'^cases/(?P<id>\d+)$', views.view_case, name='view_case'),
    url(r'^my-cases/$', views.cases_data, name='cases_data'),
    url(r'^my-cases/(?P<id>\d+)/edit$', views.edit_cases, name='edit_cases'),
    url(r'^my-cases/(?P<id>\d+)/delete$', views.delete_cases, name='delete_cases'),
    url(r'^activity/$', views.activity, name='activity'),
    url(r'^add-activity/$', views.add_activity, name='add_activity'),
    url(r'^my-activity/$', views.activity_data, name='activity_data'),
    url(r'^my-activity/(?P<id>\d+)/edit$', views.edit_activity, name='edit_activity'),
    url(r'^my-activity/(?P<id>\d+)/delete$', views.delete_activity, name='delete_activity'),
    url(r'^view-reports/$', views.view_report, name='view_reports'),
]
