"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# importamos esto para poder utilizar adminLTE
from django.conf.urls.static import static
from student_management_system import settings

# importacion para ver las vistas de las paginas de la app
from student_management_app import views

urlpatterns = [
    path('', views.showLoginPage),
    path('demo/', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('doLogin', views.doLogin),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
