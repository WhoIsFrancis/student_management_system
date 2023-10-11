from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from student_management_app.models import CustomUser

# Register your models here.
class UserModel(UserAdmin):
    pass
# Creo el user model vacio para que la contraseña este encriptada
admin.site.register(CustomUser, UserModel)


