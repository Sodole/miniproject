from django.shortcuts import render
from .models import User, Mycar, Model
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
    models = Model.objects.all()
    context = {
    "signupmessage" : "",
    "sel_models" : models
}
    return render(request, "signup.html", context)

def index(request, pk):
    global inputmessage
    inputmessage = {
            "errormessage" :""}
    speed_data_set =[]
    battery_data_set=[]
    if User.objects.filter(user_name = f"{pk}").exists() :
        old_user = User.objects.get(user_name=f"{pk}")
        old_name = old_user.user_name
        mycars = Mycar.objects.filter(user_name=f"{pk}").order_by("-pk")
        record_mycars = mycars[:5]
        last_mycar = Mycar.objects.filter(user_name=f"{pk}").last()
        mycar_dataset = mycars.order_by("-pk")[:10]
        for data in mycar_dataset :
            speed_data_set.append(data.mycar_speed)
            battery_data_set.append(data.mycar_battery)
        battery_data_set = battery_data_set[:5]
        battery_data_set.reverse()
        speed_data_set.reverse() 
        allcontext = {
            "context" : {"User" : old_name},
            "mycars" : record_mycars,
            "last_mycar" : last_mycar,
            "speed" : speed_data_set,
            "battery" : battery_data_set
        }
        return render(request, "index.html", allcontext)
    elif pk == "main" :
        mycars = Mycar.objects.all().order_by("-pk")
        last_mycar = Mycar.objects.all().last()
        record_mycars = mycars[:5]
        mycar_dataset = mycars.order_by("-pk")[:10]
        for data in mycar_dataset :
            speed_data_set.append(data.mycar_speed)
            battery_data_set.append(data.mycar_battery)
        battery_data_set = battery_data_set[:5]
        battery_data_set.reverse()
        speed_data_set.reverse() 
        allcontext = {
            "context" : {"User" : "main"},
            "mycars" : record_mycars,
            "last_mycar" : last_mycar,
            "speed" : speed_data_set,
            "battery" : battery_data_set
        }
        return render(request, "index.html", allcontext)

def detail(request, pk):
    global inputmessage
    inputmessage = {
            "errormessage" :""}
    if User.objects.filter(user_name = f"{pk}").exists() :
        old_user = User.objects.get(user_name=f"{pk}")
        old_name = old_user.user_name
        old_model = old_user.model_name
        mymodel = Model.objects.filter(model_name = old_model)
        allcontext = {
            "context" : {"User" : old_name},
            "mymodel" : mymodel
        }
        return render(request, "detail.html", allcontext)
    elif pk == "main" :
        mymodel = Model.objects.all()
        allcontext = {
            "context" : {"User" : "main"},
            "mymodel" : mymodel

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
        mycars = Mycar.objects.filter(user_name=f"{pk}").order_by("-pk")
        allcontext = {
            "context" : {"User" : old_name},
            "mycars" : mycars
        }
        return render(request, "record.html", allcontext)
    elif pk == "main" :
        mycar = Mycar.objects.all().order_by("-pk")
        mycars = mycar[:15]
        allcontext = {
            "context" : {"User" : "main"},
            "mycars" : mycars
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
                "signupmessage" : "중복id가 있습니다"
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

def delete_mycar(request, pk, fk):
    del_car = Mycar.objects.filter(user_name = f"{fk}")
    del_mycar = del_car.filter(pk=pk)
    del_mycar.delete()
    return HttpResponseRedirect(f"/record/{fk}")

def delete_mycar_index(request, pk, fk):
    del_car = Mycar.objects.filter(user_name = f"{fk}")
    del_mycar = del_car.filter(pk=pk)
    del_mycar.delete()
    return HttpResponseRedirect(f"/index/{fk}")

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



## 모델관리
# 모델생성페이지
def model(request):
    return render(request, "model.html")

# create 모델
def create_model(request) : 
    new_model = Model()
    new_model.model_name = request.GET.get("model_name")
    new_model.model_size = request.GET.get("model_size")
    new_model.model_battery = request.GET.get("model_battery")
    new_model.model_weight = request.GET.get("model_weight")
    new_model.model_firmware = request.GET.get("model_firmware")
    new_model.save()
    context ={
        "message" : "모델생성이 완료되었습니다."
    }
    return render(request, "model.html", context)