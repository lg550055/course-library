from django.shortcuts import render
from .models import Course, CourseInstance, Author, Topic
from django.views.generic import ListView, DetailView


def index(request):
  # active Courses (status = 'a')
  num_instances_active = CourseInstance.objects.filter(status__exact='a').count()

  context = {
    'num_courses': Course.objects.count(),
    'num_instances': CourseInstance.objects.count(),
    'num_instances_active': num_instances_active,
    'num_authors': Author.objects.count(),
    'num_topics': Topic.objects.count(),
  }

  return render(request, 'index.html', context)

class CourseListView(ListView):
  template_name = 'course_list.html'
  model = Course

class CourseDetailView(DetailView):
  template_name = 'course_detail.html'
  model = Course

