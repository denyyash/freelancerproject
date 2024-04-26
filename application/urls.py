"""Project6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('aboutus/', views.aboutus, name='aboutus' ),
    path('problem-statement/', views.problem_statement, name='problem_statement' ),
    path('reg-form/', views.reg, name='reg' ),
    path('login/', views.login_user, name='login' ),
    path('dashboard/', views.dashboard, name='dashboarddemo'),
    path('enquiry-details/', views.enquiry_details, name='enquiry_details'),
    path('delete/<int:id>/', views.delete_record, name ='delete_record'),
    path('edit/<int:id>/', views.edit_record, name ='edit_record'),
    path('update/<int:id>/', views.update_record, name ='update_record'),
    path('logout', views.logout_user, name ='logout'),
    path('reports/', views.reports, name ='reports'),
    path('student_data', views.student_data.as_view(), name ='student_data'),

]
