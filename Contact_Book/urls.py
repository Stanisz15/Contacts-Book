"""Contact_Book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from book_app.views import new_person, person_list, show_person, modify_person, del_person, add_address, del_address,\
    add_phone, add_email, del_phone, del_email, modify_address, modify_phone, modify_email, groups_list, new_group,\
    show_group, add_to_group, mod_group, del_group, back_to_group, del_from_group

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^new/$', new_person),
    url(r'^modify/(?P<id>\d+)/$', modify_person),
    url(r'^delete/(?P<id>\d+)/$', del_person),
    url(r'^show/(?P<id>\d+)/$', show_person),
    url(r'^$', person_list),
    url(r'^modify/(?P<id>\d+)/addAddress/$', add_address),
    url(r'^delete/(?P<id_person>\d+)/delAddress/(?P<id_address>\d+)/$', del_address),
    url(r'^modify/(?P<id>\d+)/addPhone/$', add_phone),
    url(r'^modify/(?P<id>\d+)/addEmail/$', add_email),
    url(r'^delete/(?P<id_person>\d+)/delPhone/(?P<id_phone>\d+)/$', del_phone),
    url(r'^delete/(?P<id_person>\d+)/delEmail/(?P<id_email>\d+)/$', del_email),
    url(r'^modify/(?P<id_person>\d+)/modifyAddress/(?P<id_address>\d+)/$', modify_address),
    url(r'^modify/(?P<id_person>\d+)/modifyPhone/(?P<id_phone>\d+)/$', modify_phone),
    url(r'^modify/(?P<id_person>\d+)/modifyEmail/(?P<id_email>\d+)/$', modify_email),
    url(r'^groups/$', groups_list),
    url(r'^new_group/$', new_group),
    url(r'^show_group/(?P<id>\d+)/$', show_group),
    url(r'^modify/(?P<id>\d+)/add_to_group/$', add_to_group),
    url(r'^modify_group/(?P<id_group>\d+)/$', mod_group),
    url(r'^del_group/(?P<id>\d+)/$', del_group),
    url(r'^back_to_group/(?P<id>\d+)/$', back_to_group),
    url(r'^delete/(?P<id_person>\d+)/del_from_group/(?P<id_group>\d+)/$', del_from_group),
]
