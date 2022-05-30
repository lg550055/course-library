from django.urls import path
from .views import index, CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView


urlpatterns = [
  path('', index, name='index'),
  path('courses/', CourseListView.as_view(), name='course_list'),
  path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
  path('course/create/', CourseCreateView.as_view(), name='course_create'),
  path('course/<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),
  path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete')
]
