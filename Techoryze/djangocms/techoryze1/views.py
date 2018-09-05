# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"

class GameDesignView(TemplateView):
    template_name = "game-design.html"

class GraphicDesignView(TemplateView):
    template_name = "graphic-design.html"

class ChatDesignView(TemplateView):
    template_name = "chat.html"

class PythonDesignView(TemplateView):
    template_name = "codeCourses/python.html"

class CPlusDesignView(TemplateView):
    template_name = "codeCourses/Cplus.html"

class HourOfCodeDesignView(TemplateView):
    template_name = "codeCourses/hourOfCode.html"

class iosView(TemplateView):
    template_name = "codeCourses/ios.html"

class JavaView(TemplateView):
    template_name = "codeCourses/java.html"

class WebDesignView(TemplateView):
    template_name = "codeCourses/webDesign.html"

class PythonCrystalSkullDesignView(TemplateView):
    template_name = "codeCoursesPythonVideos/python-and-the-crystal-skull-learning-conditions.html"

class PythonCurseOfUnusuallHighWaveDesignView(TemplateView):
    template_name = "codeCoursesPythonVideos/python-and-the-curse-of-the-unusually-high-waves.html"

class FunctionCreationDesignView(TemplateView):
    template_name = "codeCoursesPythonVideos/function-creation-in-python.html"