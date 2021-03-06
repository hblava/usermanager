"""usermanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf.urls import include, url
from app01.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/', login),
    url(r'^index/', index),
    url(r'^logout/', logout),
    url(r'^classes$', handle_classes),
    url(r'^student$', handle_student),
    url(r'^teacher$', handle_teacher),
    url(r'^login.html/', Login.as_view()),
    url(r'^add_classes', handle_add_classes),
    url(r'^edit_classes', handle_edit_classes),
    url(r'^add_student', handle_add_student),
    url(r'^edit_student', handle_edit_student),
    url(r'^dele_student', handle_dele_student),
    url(r'^add_teacher', handle_add_teacher),
    url(r'^edit_teacher-(\d+)', handle_edit_teacher),
    url(r'^dele_teacher', handle_dele_teacher),
    url(r'^upload', upload),
    url(r'^menu', menu),
    url(r'^fetch_city', fetch_city),
    url(r'^fetch_xian', fetch_xian),




]
