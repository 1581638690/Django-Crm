from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  # 用于验证用户的用户名和密码，检查用户提供的平局是否有效
from django.contrib import messages  # 用于向用户发送反馈通知
from django import forms
from .forms import *
from .models import *
# Create your views here.
def home(request):
    Records=Record.objects.all()
    if request.method == "POST":
        user = request.POST["username"]
        passwd = request.POST["password"]
        user = authenticate(request, username=user, password=passwd)
        if user is not None:
            # 登录成功
            login(request, user)  # 进行登录
            messages.success(request, "你已经成功登录！")
            return redirect("home")
        else:
            messages.success(request, '登录失败，请尝试再次登录！！')
            return redirect("home")
    else:
        return render(request, "home.html", {"Records":Records})


def log_out(request):
    logout(request)
    messages.success(request, "你已经成功退出登录！")
    return redirect("home")

def register(request):
    if request.method=='POST':
        #传入POST表单信息
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password1"]
            user=authenticate(username=username,password=password)
            #登录 验证信息
            login(request,user)
            messages.success(request,"You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

def view_records(request,pk):
    if request.user.is_authenticated:#判断是否登录
        single_data=Record.objects.get(pk=pk)
        if single_data:
            messages.success(request,"查询成功！")
            return render(request,"view_records.html",{"single_data":single_data})
        else:
            messages.success(request,"查询失败！")
    else:
        messages.success(request,"请先登录,在进行查看详情数据！")

def delete_record(request,pk):
    if request.user.is_authenticated:#判断是否为登录
        delete_data=Record.objects.get(pk=pk)
        delete_data.delete()
        messages.success(request, "删除成功！")
        return render(request,"home.html")
    else:
        messages.success(request,"请先登录,在进行删除数据！")
        return render(request,"home.html")

def update_record(request,pk):
    if request.user.is_authenticated:

        current_record=Record.objects.get(pk=pk)
        form=AddRecordsForm(request.POST or None,instance=current_record)#保存数据库模型
        if form.is_valid():
            form.save()
            messages.success(request,"修改成功！")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request,"请先登录,在进行修改数据！")
        return redirect('home')
def add_record(request):
    form = AddRecordsForm(request.POST or None)#作为一个 全局变量进行处理
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()#将表单数据保存到数据库
                messages.success(request,"Record add ...")
                return redirect('home')
        return render(request,'add_record.html',{"form":form})
    else:
        messages.success(request,"请先登录,在进行添加数据！")
        return redirect('home')
                # first_name=form.cleaned_data['first_name']
                # last_name=form.cleaned_data["last_name"]
                # email=form.cleaned_data["email"]
                # phone=form.cleaned_data["phone"]
                # address=form.cleaned_data["address"]
                # city=form.cleaned_data["city"]
                # state=form.cleaned_data["state"]
                # zipcode=form.cleaned_data['zipcode']
