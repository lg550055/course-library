from django.contrib import admin
from .models import Author, Course, Topic, CourseInstance


admin.site.register(Author)
admin.site.register(Course)
admin.site.register(CourseInstance)
admin.site.register(Topic)
