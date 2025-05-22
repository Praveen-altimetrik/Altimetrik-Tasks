from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    path('', views.unified_login, name='unified_login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('faculty/dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('parent/dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]