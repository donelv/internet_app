"""mysite URL Configuration

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
from django.urls import path
from application import views

urlpatterns = [
    path('', views.index),
    path('class', views.dispclass_list),
    path('class/create', views.DisplayClassCreate.as_view()),
    path('class/<int:disp_id>/update', views.DisplayClassUpdate.as_view(), name='class_update'),
    path('class/<int:disp_id>/delete', views.DisplayClassDelete.as_view(), name='class_delete'),
    path('computer', views.computers_list),
    path('computer/create', views.ComputerCreate.as_view()),
    path('computer/<int:comp_id>/update', views.ComputerUpdate.as_view(), name='computer_update'),
    path('computer/<int:comp_id>/delete', views.ComputerDelete.as_view(), name='computer_delete'),
    path('report', views.report)
]
