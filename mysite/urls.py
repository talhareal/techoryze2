# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from mysite.views import ChatterBotAppView

from . import views
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^', include('cms.urls')),
    url(r'^$', views.coursesTopic_view, name='index'),
    url(r'^logins', views.login_view, name='logins'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^createnewAccount', views.createAccount_view, name='createnewAccount'),
    url(r'^forgotPassword', views.forgotPassword_view, name='forgotPassword'),
    url(r'^resetPassword', views.resetPassword_view, name='resetPassword'),
    url(r'^(?P<course_name>[\w\-]+)/courses', views.courses_view, name='courses'),
    url(r'^(?P<course_name>[\w\-]+)/(?P<course_id>[\w\-]+)/video/', views.video_view, name='video'),
    url(r'^api/chatterbot/', include(chatterbot_urls, namespace='chatterbot')),
    url(r'^chatterbot/', views.ChatterBotAppView, name='chatterbot'),
    url(r'^(?P<course_id>[\w\-]+)/video/course_series',
        views.CourseSeries, name='course_series'),
    url(r'^ActivationMessage/', views.activateaccount_view, name='ActivationMessage'),
    url(r'^confirm', views.view_confirm, name='confirm'),
    url(r'^AboutUs',views.view_about_us, name='AboutUs'),
    url(r'^Analytics',views.view_analytics, name='Analytics'),
    url(r'^resetpassconfrmMessage',views.view_forgot_message,name='resetpassconfrmMessage'),
    url(r'^createAcountconfrmMessage', views.view_create_account_confirmatio_message, name='createAcountconfrmMessage'),
    url(r'^resetPasswordSentEmailFormat',views.view_password_reset_format,name='resetPasswordSentEmailFormat'),
    url(r'^ContactUs',views.view_conatact_us, name='ContactUs'),
    url(r'^PrivacyPolicy',views.view_privacy_policy,name='PrivacyPolicy'),
    url(r'^Instructor',views.view_instructor,name='Instructor'),
    url(r'^Blogs',views.view_blog,name='Blog'),
<<<<<<< HEAD
    url(r'^safarivideo',views.view_safari,name='safarivideo')
=======

url(r'^safarivideo',views.safariview,name='safarivideo')
>>>>>>> c941cdec99f56e15f79f3e64f7f7c71673ff1a5a
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
<<<<<<< HEAD
                  ] + staticfiles_urlpatterns() + urlpatterns
=======

        ] + staticfiles_urlpatterns() + urlpatterns
>>>>>>> c941cdec99f56e15f79f3e64f7f7c71673ff1a5a
