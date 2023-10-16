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
from student_management_app import views, HodViews

urlpatterns = [
    path('', views.showLoginPage),
    path('demo/', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('doLogin', views.doLogin),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user),
    path('admin_home', HodViews.admin_home),
    # Para agregar staff y guardarlo
    path('add_staff', HodViews.add_staff),
    path('add_staff_save', HodViews.add_staff_save),
    # Para agregar course y guardarlo
    path('add_course', HodViews.add_course),
    path('add_course_save', HodViews.add_course_save),
    # Para agregar student y guardarlo
    path('add_student', HodViews.add_student),
    path('add_student_save', HodViews.add_student_save),
    # Para agregar subject
    path('add_subject', HodViews.add_subject),
    path('add_subject_save', HodViews.add_subject_save),
    # Administrar staff
    path('manage_staff', HodViews.manage_staff),
    # Administrar student
    path('manage_student', HodViews.manage_student),
    # Administrar cursos
    path('manage_course', HodViews.manage_course),
    # Administrar subject
    path('manage_subject', HodViews.manage_subject),
    # Editar staff y guardarlo
    path('edit_staff/<str:staff_id>', HodViews.edit_staff),
    path('edit_staff_save', HodViews.edit_staff_save),
    # Editar student y guardarlo
    path('edit_student/<str:student_id>', HodViews.edit_student),
    path('edit_student_save', HodViews.edit_student_save),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
