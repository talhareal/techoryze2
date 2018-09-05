from django.contrib.postgres.fields import ArrayField
from django.db import models


class CreateUser(models.Model):
    Email = models.EmailField(max_length=100, default='')
    First_name = models.CharField(max_length=100, default='')
    Last_name = models.CharField(max_length=100, default='')
    Password = models.CharField(max_length=100, default='')
    Confirm_password = models.CharField(max_length=100, default='')

    def __str__(self):
        return  self.First_name

class Courses(models.Model):
    class Meta:
        verbose_name = 'Courses'
        verbose_name_plural = 'Courses'

    PRODUCTIVITY = 'MOS'
    GRAPHIC = 'GD'
    SOUND = 'SM'
    WEBSITE = 'WD'
    ANIMATION = 'AP'
    VIDEO = 'VE'

    course_thumbnil_Image = models.ImageField()
    course_video = models.FileField(upload_to=u'video/', default='' , blank=True)
    course_title = models.TextField()
    course_detail = models.TextField()
    course_author_image = models.ImageField()
    course_author_name = models.TextField()
    course_date = models.TextField()
    course_duration = models.TextField()
    COURSE_CATEGORY_CHOICES = (
        (PRODUCTIVITY, 'Productivity'),
        (GRAPHIC, 'Creative Design'),
        (SOUND, 'Sound & Music'),
        (WEBSITE, '3D Modeling'),
        (ANIMATION, 'Animation Production'),
        (VIDEO, 'Video Editing'),
    )
    course_category = models.CharField(max_length=5,
                                      choices=COURSE_CATEGORY_CHOICES,
                                      default=PRODUCTIVITY)

    course_outline = models.CharField(max_length=500, default='')

    instructor_detail = models.CharField(max_length=500, default='')

    number_of_lesson = models.IntegerField(default=0)

    course_video_1 = models.FileField(upload_to=u'video/', default='' , blank=True)

    course_video_2 = models.FileField(upload_to=u'video/', default='' , blank=True)

    course_video_3 = models.FileField(upload_to=u'video/', default='' , blank=True)

    course_video_4 = models.FileField(upload_to=u'video/', default='' , blank=True)

    course_video_5 = models.FileField(upload_to=u'video/', default='', blank=True)


    def __str__(self):
        return self.course_title

class CoursesTopic(models.Model):

    class Meta:
        verbose_name = 'Course Topics'
        verbose_name_plural = 'Course Topics'

    BLUE = 'colorBlue mt-4'
    GREEN = 'colorGreen mt-4'
    PARPUL = 'colorparpup mt-4'
    ORANGE = 'colorOrange mt-4'
    PINK = 'colorpink mt-4'
    BROWN = 'colorbrown mt-4'

    course_thumbnil_Image = models.ImageField()
    course_title = models.TextField()
    course_detail = models.TextField()
    COLOR_CATEGORY_CHOICES = (
        (BLUE, 'BLUE'),
        (GREEN, 'GREEN'),
        (PARPUL, 'PARPUL'),
        (ORANGE, 'ORANGE'),
        (PINK, 'PINK'),
        (BROWN, 'BROWN'),
    )
    background_color = models.CharField(max_length=40,
                                       choices=COLOR_CATEGORY_CHOICES,
                                       default=BLUE)


    def __str__(self):
        return self.course_detail


class TechoryzeAnalytics(models.Model):
    class Meta:
        verbose_name = 'Techoryze Analytics'
        verbose_name_plural = 'Techoryze Analytics'

    AppID = models.CharField(max_length=50, default='')

    Username = models.CharField(max_length=50, default='')

    AssetID = models.CharField(max_length=50, default='')

    PageID = models.CharField(max_length=50, default='')

    Page_Title = models.CharField(max_length=30, default='')

    Asset_Title = models.CharField(max_length=30, default='')

    Asset_Type = models.CharField(max_length=30, default='')

    DateTime = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.Username


