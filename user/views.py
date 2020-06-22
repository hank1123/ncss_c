from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.views.decorators.csrf import csrf_protect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UsersSerializer
from .models import Users
from .forms import LoginForm, UserForm

# Create your views here.

def insert_user(request):
    if request.method != 'POST':
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:index'))
    context = {'form': form}
    return render(request, 'user/insert.html', context) 

def delete_user(request):
    pass
    
    def delete(self, request):
        return self.del_user(request)
    
def users(request):
    users = Users.objects.order_by('id')
    context = {'users': users}
    return render(request, 'user/users.html', context)

def user(request, id):
    user = Users.objects.get(id=id)
    if user.role_id == 1:
        user.role_name = '系统管理员'
    elif user.role_id == 2:
        user.role_name = '日志审计员'
    else:
        user.role_name = '用户'
        
    context = {'user': user}
    return render(request, 'user/user.html', context)


def update_user(request, id):
    user = Users.objects.get(id=id)

    if request.method != 'POST':
        form = UserForm(instance=user)
    else:
        form = UserForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:index'))
    context = {'form': form, 'user': user}
    return render(request, 'user/update.html', context)
    
def login(request):
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            account = form.data.get("account")
            pwd = form.data.get("password")
            user_obj = Users.objects.all().filter(account=account).first()
            ser_obj = UsersSerializer(user_obj)
            if ser_obj.data["password"] == pwd:
                request.session["id"] = ser_obj.data["id"]
                return HttpResponseRedirect(reverse('user:index'))
    context = {'form': form}
    return render(request, 'user/login.html', context)

def index(request):
    return render(request, 'user/index.html')