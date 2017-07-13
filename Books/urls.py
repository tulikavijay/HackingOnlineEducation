"""Books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from newsletter import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^signup/',views.signup, name='signup'),
    url(r'^contact/',views.contact, name='contact'),
    url(r'^register/',views.register, name='register'),
    url(r'^login/',auth_views.login, name='login'),
    url(r'^accounts/logout/',auth_views.logout, name='logout'),
    url(r'^accounts/profile',views.profile, name='profile'),
    url(r'^explore',views.explore, name='explore'),
    url(r'^explore/(?P<category_name>.+)/$',views.pages, name='pages'),
#    url(r'^profile_images/(.*)$',django.views.static.serve,{'document_root':settings.MEDIA_ROOT}),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
     urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
