"""mysite URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
import account_app.views
import blog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add_user/', account_app.views.add_user, name = 'add_user'),
    url(r'^remove_user/', account_app.views.remove_user, name = 'remove_user'),
    url(r'^login/', account_app.views.login, name = 'login'),
    url(r'^change_profile_image/', account_app.views.change_profile_image, name = 'change_profile_image'),
    url(r'^upload_post/', blog.views.upload_post, name = 'upload_post'),
    url(r'^delete_post/', blog.views.delete_post, name = 'delete_post'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
