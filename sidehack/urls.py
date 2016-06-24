"""sidehack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login, name='login'),
    url(r'^hacker/(?P<hacker_name>[a-zA-Z0-9]+)/$',
        views.get_hacker,
        name='get_hacker'
        ),
    url(r'^hacker/(?P<hacker_name>[a-zA-Z0-9]+)/hack/(?P<hack>[a-zA-Z0-9]+)/$',
        views.get_hacker_hack,
        name='get_hacker_hack'
        ),
    url(r'^org/(?P<org_name>[a-zA-Z0-9]+)/$',
        views.get_org,
        name='get_org'
        ),
    url(r'^org/(?P<org_name>[a-zA-Z0-9]+)/hack/(?P<hack>[a-zA-Z0-9]+)/$',
        views.get_org_hack,
        name='get_org_hack'
        ),
    url(r'^$', views.index, name='index'),
]
