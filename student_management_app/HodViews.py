import datetime
from MySQLdb import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages 

from student_management_app.models import CustomUser, Staffs, Courses

def admin_home(request):
    return render(request, "hod_template/home_content.html")

def add_staff(request):
    return render(request, "hod_template/add_staff_template.html")

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
        

def add_course(request):
    return render(request, "hod_template/add_course_template.html")


def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        course=request.POST.get("course")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Successfully added Course")
            return HttpResponseRedirect("/add_course")
        
        except IntegrityError as e:
            # Maneja la excepción de violación de integridad (por ejemplo, si el curso ya existe)
            messages.error(request, f"Failed to add Course: {e}")
            return HttpResponseRedirect("/add_course")
        
        except Exception as e:
            # Maneja otras excepciones generales
            messages.error(request, f"An error occurred: {e}")
            return HttpResponseRedirect("/add_course")

        except: 
            messages.error(request, "Failed to add course")
            return HttpResponseRedirect("/add_course")


def add_student(request):
    courses=Courses.objects.all()
    return render(request, "hod_template/add_student_template.html", {"courses":courses})

def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        course_id = request.POST.get("course")
        sex = request.POST.get("sex")


        try:
            # Intenta crear un nuevo usuario de tipo "Student"
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
            user.students.address=address
            course_obj=Courses.objects.get(id=course_id)
            user.students.course_id=course_obj
            user.students.session_start_year=session_start
            user.students.session_end_year=session_end
            user.students.gender=sex
            user.students.profile_pic=""
            user.save()
            messages.success(request, "Successfully added Student")
            return HttpResponseRedirect("/add_student")
        
        except IntegrityError as e:
            # Maneja la excepción de violación de integridad (por ejemplo, si el usuario ya existe)
            messages.error(request, f"Failed to add Student: {e}")
            return HttpResponseRedirect("/add_student")
        
        except Exception as e:
            # Maneja otras excepciones generales
            messages.error(request, f"An error occurred: {e}")
            return HttpResponseRedirect("/add_student")
        