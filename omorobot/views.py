from django.shortcuts import render
from .models import User, Mycar
from django.http import HttpResponseRedirect
from django.urls import reverse

context = {
    "signupmessage" : "",
    "signinmessage" : ""
}
inputmessage ={
    "errormessage" :"asdf"}

## 페이지 로직
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
    global inputmessage
    inputmessage = {
            "errormessage" :""}
    mycar = Mycar.objects.all()
    if User.objects.filter(user_name = f"{pk}").exists() :
        old_user = User.objects.get(user_name=f"{pk}")
        old_name = old_user.user_name
        allcontext = {
            "context" : {"User" : old_name, "mycars": mycar}
        }
        return render(request, "index.html", allcontext)
    elif pk == "main" :
        allcontext = {
            "context" : {"User" : "main"}
        }
        return render(request, "index.html", allcontext)

def detail(request, pk):
    global inputmessage
    inputmessage = {
            "errormessage" :""}
    if User.objects.filter(user_name = f"{pk}").exists() :
        old_user = User.objects.get(user_name=f"{pk}")
        old_name = old_user.user_name
        allcontext = {
            "context" : {"User" : old_name}
        }
        return render(request, "detail.html", allcontext)
    elif pk == "main" :
        allcontext = {
            "context" : {"User" : "main"}
        }
        return render(request, "detail.html", allcontext)

def input(request, pk):
    global inputmessage
    if User.objects.filter(user_name = f"{pk}").exists() :
        old_user = User.objects.get(user_name=f"{pk}")
        old_name = old_user.user_name
        allcontext = {
            "context" : {"User" : old_name},
            "text" : inputmessage
        }

        return render(request, "input.html", allcontext)
    elif pk == "main" :
        allcontext = {
            "context" : {"User" : "main"},
            "text" : inputmessage
         }
        return render(request, "input.html", allcontext)


def record(request, pk):
    global inputmessage
    inputmessage = {
            "errormessage" :""}
    if User.objects.filter(user_name = f"{pk}").exists() :
        old_user = User.objects.get(user_name=f"{pk}")
        old_name = old_user.user_name
        allcontext = {
            "context" : {"User" : old_name}
        }
        return render(request, "record.html", allcontext)
    elif pk == "main" :
        allcontext = {
            "context" : {"User" : "main"}
        }
        return render(request, "record.html", allcontext)

def realtime(request, pk):
    global inputmessage
    inputmessage = {
            "errormessage" :""}
    if User.objects.filter(user_name = f"{pk}").exists() :
        old_user = User.objects.get(user_name=f"{pk}")
        old_name = old_user.user_name
        allcontext = {
            "context" : {"User" : old_name}
        }
        return render(request, "realtime.html", allcontext)
    elif pk == "main" :
        allcontext = {
            "context" : {"User" : "main"}
        }
        return render(request, "realtime.html", allcontext)


## user관리
def delete_user(request, pk):
    del_user = User.objects.filter(pk=pk)
    del_user.delete()
    return HttpResponseRedirect(reverse("omorobot:index"))

def update_user(request, pk) :
  if request.method == "POST" :
    user_model = request.POST.get("model")
    old_user = User.objects.get(pk=pk)
    old_user.models = user_model
    old_user.save()
    return HttpResponseRedirect(reverse("omorobot:index"))


## 회원가입로직
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


# mycar 관리
def create_mycar(request, pk):
    input_speed = request.GET.get("speed")
    input_battery = request.GET.get("battery")
    input_color = request.GET.get("color")
    global inputmessage
    print(input_speed, input_battery, input_color)
    if User.objects.filter(user_name = f"{pk}").exists() :
        new_mycar = Mycar()
        try :
            new_mycar.mycar_speed = int(input_speed)
            new_mycar.mycar_battery = int(input_battery)
            new_mycar.mycar_color = input_color
            new_mycar.user_name = User.objects.get(user_name=f"{pk}")
            new_mycar.save()
            inputmessage = {
            "errormessage" : "생성되었습니다"
            }
            return HttpResponseRedirect(f"/input/{pk}/")
        except :
            inputmessage = {
            "errormessage" : "올바른 값을하세요"
        }
            return HttpResponseRedirect(f"/input/{pk}/")
    else : 
        inputmessage = {
        "errormessage" : "로그인을해주세요"
        }
        return HttpResponseRedirect(f"/input/{pk}/")

def delete_mycar(request, pk):
    del_mycar = Mycar.objects.filter(pk=pk)
    del_mycar.delete()
    return HttpResponseRedirect(reverse("omorobot:index"))

def update_mycar(request, pk) :
  if request.method == "POST" :
    mycar_speed = request.POST.get("speed")
    mycar_battery = request.POST.get("battery")
    mycar_color = request.POST.get("color")
    old_minicar = Mycar.objects.get(pk=pk)
    old_minicar.speed = mycar_speed
    old_minicar.battery = mycar_battery
    old_minicar.color = mycar_color
    old_minicar.save()
    return HttpResponseRedirect(reverse("omorobot:index"))