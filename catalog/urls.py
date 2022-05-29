from django.urls import path
from .views import index, CourseListView, CourseDetailView

urlpatterns = [
  path('', index, name='index'),
  path('courses/', CourseListView.as_view(), name='course_list'),
  path('course/<int:pk>', CourseDetailView.as_view(), name='course_detail')
]
