from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Topic(models.Model):
  """ Course's main technology """
  name = models.CharField(max_length=32, help_text='Enter course topic, e.g. Django')

  def __str__(self):
    return self.name


class Author(models.Model):
  """ Represents and author """
  name = models.CharField(max_length=32)
  email = models.EmailField(max_length=32)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    """ Returns the url to access a detail record for this author """
    return reverse('author_detail', args=[str(self.id)])


class Course(models.Model):
  """ Represents a course """
  title = models.CharField(max_length=32)
  author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
  summary = models.CharField(max_length=256, help_text='Enter a brief description of the course')
  code = models.CharField(max_length=16, unique=True, help_text='Enter the courses unique identifier code')
  topic = models.ManyToManyField(Topic, help_text='Select topics for this course')
  LEVELS = (('a','Advanced'),('b','Beginner'),('i','Intermediate'))
  level = models.CharField(max_length=1, choices=LEVELS, default='b')
  created = models.DateField(auto_now_add=True)
  modified = models.DateField(auto_now=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    """ Returns the url to access a detail record for this course """
    return reverse('course_detail', args=[str(self.id)])


class CourseInstance(models.Model):
  """ Represents a specific copy of the course created for a student """
  course = models.ForeignKey(Course, on_delete=models.RESTRICT)
  created = models.DateField(auto_now_add=True)
  modified = models.DateField(auto_now=True)
  finishes = models.DateField()
  STATUS_OPTIONS = (('a','Active'),('p','Paused'),('t','Terminated'),('c','Completed'))
  status = models.CharField(max_length=1, choices=STATUS_OPTIONS, default='a')
  student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  class Meta:
    ordering = ['finishes']
  
  def __str__(self):
    return f'{self.student} ({self.course.title})'
