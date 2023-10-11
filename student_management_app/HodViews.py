from MySQLdb import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages 

from student_management_app.models import CustomUser, Staffs

def admin_home(request):
    return render(request, "hod_template/home_content.html")

def add_staff(request):
    return render(request, "hod_template/add_staff_template.html")

# def add_staff_save(request):
#     if request.method != "POST":
#         return HttpResponse("Method not allowed")
#     else:
#         first_name=request.POST.get("first_name")
#         last_name=request.POST.get("last_name")
#         username=request.POST.get("username")
#         email=request.POST.get("email")
#         password=request.POST.get("password")
#         adress= request.POST.get("adress")

#         # objeto CustomUser
#         try:
#             user= CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, adress=adress, user_type=2)
#             user.save()
#             messages.success(request, "Successfully added Staff")
#             return HttpResponseRedirect("/add_staff")
#         except:
#             messages.error(request, "Failed to add Staff")
#             return HttpResponseRedirect("/add_staff")

def add_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")

        try:
            # Intenta crear un nuevo usuario de tipo "Staff"
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.staffs.address=address
            user.save()
            messages.success(request, "Successfully added Staff")
            return HttpResponseRedirect("/add_staff")
        
        except IntegrityError as e:
            # Maneja la excepción de violación de integridad (por ejemplo, si el usuario ya existe)
            messages.error(request, f"Failed to add Staff: {e}")
            return HttpResponseRedirect("/add_staff")
        
        except Exception as e:
            # Maneja otras excepciones generales
            messages.error(request, f"An error occurred: {e}")
            return HttpResponseRedirect("/add_staff")