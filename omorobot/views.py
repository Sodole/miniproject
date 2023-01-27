from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

context = {
    "signupmessage" : "",
    "signinmessage" : ""
}

# Create your views here.
def landing(request):
    return render(request, "landing.html")

def signin(request):
    global context
    context = {
    "signinmessage" : ""
}
    return render(request, "signin.html", context)

def signup(request):
    global context
    context = {
    "signupmessage" : ""
}
    return render(request, "signup.html", context)

def index(request, pk):
    if User.objects.filter(user_name = f"{pk}").exists() :
        old_user = User.objects.get(user_name=f"{pk}")
        old_name = old_user.user_name
        context = {
            "User" : old_name
        }
        return render(request, "index.html", context)
    elif pk == "main" :
        context = {
            "User" : "main"
        }
        return render(request, "index.html", context)

def detail(request, pk):
    if User.objects.filter(user_name = f"{pk}").exists() :
        old_user = User.objects.get(user_name=f"{pk}")
        old_name = old_user.user_name
        context = {
            "User" : old_name
        }
        return render(request, "detail.html", context)
    elif pk == "main" :
        context = {
            "User" : "main"
        }
        return render(request, "detail.html", context)

def input(request, pk):
    if User.objects.filter(user_name = f"{pk}").exists() :
        old_user = User.objects.get(user_name=f"{pk}")
        old_name = old_user.user_name
        context = {
            "User" : old_name
        }
        return render(request, "input.html", context)
    elif pk == "main" :
        context = {
            "User" : "main"
        }
        return render(request, "input.html", context)


def record(request, pk):
    if User.objects.filter(user_name = f"{pk}").exists() :
        old_user = User.objects.get(user_name=f"{pk}")
        old_name = old_user.user_name
        context = {
            "User" : old_name
        }
        return render(request, "record.html", context)
    elif pk == "main" :
        context = {
            "User" : "main"
        }
        return render(request, "record.html", context)

def realtime(request, pk):
    if User.objects.filter(user_name = f"{pk}").exists() :
        old_user = User.objects.get(user_name=f"{pk}")
        old_name = old_user.user_name
        context = {
            "User" : old_name
        }
        return render(request, "realtime.html", context)
    elif pk == "main" :
        context = {
            "User" : "main"
        }
        return render(request, "realtime.html", context)


# 회원가입로직
def create_user(request) :
    global context
    if request.method == "POST":
        signup_username = request.POST.get("username")
        signup_password = request.POST.get("password")
        signup_confirm = request.POST.get("password_confirm")
        signup_model = request.POST.get("model_selector")

        # 빈칸 확인
        if signup_username == "" :
            context = {
                "signupmessage" : "ID를 입력하세요"
            }
            return HttpResponseRedirect(reverse("omorobot:create_user"))
        # 중복아이디 확인
        elif User.objects.filter(user_name = f"{signup_username}").exists() :
            context = {
                "signupmessage" : "중복id가있다."
            }
            return HttpResponseRedirect(reverse("omorobot:create_user"))  
        else :
            # 암호 빈칸확인
            if signup_password == "" :
                context = {
                    "signupmessage" : "PW가 비어있습니다"
                }
                return HttpResponseRedirect(reverse("omorobot:create_user"))
            # 암호가 같은지 확인
            # 같으면 로그인 된 회원페이지로 이동
            else :
                if signup_password == signup_confirm :
                    new_user = User()
                    new_user.user_name = signup_username
                    new_user.user_password = signup_password
                    new_user.model_name = signup_model
                    new_user.save()
                    return HttpResponseRedirect(f"/index/{signup_username}")
                else : 
                    context ={
                        "signupmessage" : "비밀번호 확인하세요"
                    }
                    return HttpResponseRedirect(reverse("omorobot:create_user"))
    else :
        return render(request, "signup.html", context)


## 로그인 로직
def read_user(request) :
    global context
    if request.method == "POST":
        signin_username = request.POST.get("username")
        signin_password = request.POST.get("password")

        # 빈칸 확인
        if signin_username == "" :
            context = {
                "signinmessage" : "ID를 입력하세요"
            }
            return HttpResponseRedirect(reverse("omorobot:signin"))
                
        else :
            # 암호 빈칸확인
            if signin_password == "" :
                context = {
                    "signinmessage" : "PW가 비어있습니다"
                }
                return HttpResponseRedirect(reverse("omorobot:signin"))
            # 같으면 로그인 된 회원페이지로 이동
            else :
                if User.objects.filter(user_name = f"{signin_username}").exists() :
                    old_user = User.objects.get(user_name = f"{signin_username}")
                    user_password = old_user.user_password
                    if user_password != signin_password :
                        context ={
                            "signinmessage" : "비밀번호 확인하세요"
                        }
                        return HttpResponseRedirect(reverse("omorobot:signin"))
                    else : 
                        return HttpResponseRedirect(f"/index/{signin_username}/")
                else :
                    context ={
                        "signinmessage" : "등록된 정보가 없습니다."
                    }
                    return HttpResponseRedirect(reverse("omorobot:signin"))
    else :
        return render(request, "signin.html", context)
