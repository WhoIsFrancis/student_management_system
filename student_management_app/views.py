from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse 


from student_management_app.EmailBackend import EmailBackend

# Create your views here.
def showDemoPage(request):
    return render(request, 'demo.html')

def showLoginPage(request):
    return render(request, "login_page.html")

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2> No se permite este metodo</h2>")
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = EmailBackend.authenticate(request,username=email, password=password)
        if user != None: 
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect("/admin_home")
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("staff_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(request, "Invalid Login")
            return HttpResponseRedirect("/")
        

def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User: "+ request.user.email + " usertype: " + request.user.user_type)
    else:
        return HttpResponse("Por favor realice el login primeramente.")
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
