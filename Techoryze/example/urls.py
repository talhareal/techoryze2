from django.conf.urls import url, include
from example import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'), # Notice the URL has been named

    url(r'^game-design/$', views.GameDesignView.as_view(), name='game-design'),
    url(r'^graphic-design/$', views.GraphicDesignView.as_view(), name='graphic-design'),
    #codeCourses
    url(r'^codeCourses/Cplus', views.CPlusDesignView.as_view(), name='codeCourses/Cplus'),
    url(r'^codeCourses/hourOfCode', views.HourOfCodeDesignView.as_view(), name='codeCourses/hourOfCode'),
    url(r'^codeCourses/ios', views.iosView.as_view(), name='codeCourses/ios'),
    url(r'^codeCourses/java', views.JavaView.as_view(), name='codeCourses/java'),
    url(r'^codeCourses/python', views.PythonDesignView.as_view(), name='codeCourses/python'),
    url(r'^codeCourses/webDesign', views.WebDesignView.as_view(), name='codeCourses/webDesign'),
    #codeCoursespythonVideos
    url(r'^codeCoursesPythonVideos/python-and-the-crystal-skull-learning-conditions$',
        views.PythonCrystalSkullDesignView.as_view(),
        name='codeCoursesPythonVideos/python-and-the-crystal-skull-learning-conditions'),

    url(r'^codeCoursesPythonVideos/python-and-the-curse-of-the-unusually-high-waves$',
        views.PythonCurseOfUnusuallHighWaveDesignView.as_view(),
        name='codeCoursesPythonVideos/python-and-the-curse-of-the-unusually-high-waves'),

url(r'^codeCoursesPythonVideos/functionCreation$',
        views.FunctionCreationDesignView.as_view(),
        name='codeCoursesPythonVideos/functionCreation'),

    url(r'^chat/', views.ChatDesignView.as_view(), name='chat'),
    url(r'^chatterbot/', include('chatterbot.ext.django_chatterbot.urls', namespace='chatterbot')),
]