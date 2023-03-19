from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('projects', views.Projects, name="projects"),
    path('<str:project_name>/', views.ProjectDetails, name="ProjectDetails"),
    path('about', views.About, name="about"),
    path('services', views.Services, name="services"),
    path('login', views.LoginPage, name="LoginPage"),
    path('logout', views.logoutPage, name='logout'),
    path('dashboard', views.Dashboard, name="dashboard"),
    path('add', views.Add, name="add"),
    path('contact', views.Contact, name="contact"),
    path('Update/<str:pk>', views.Update, name='update'),
    path('Delete/<str:pk>', views.Delete, name='delete')

]
