from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse, reverse
from rest_framework import status

class AuthMD(MiddlewareMixin):  # 验证登录

    def process_request(self, request):  # 请求之前
        request_url = request.path_info

        if request_url == 'login/' or request.session.get("id"): #要登陆或已登录
            return None
        else:
            self.ret["errMsg"] = "用户未登录"
            self.ret["errCode"] = status.HTTP_400_BAD_REQUEST
            self.ret["url"] = "login/"
        # 错误提示
        return render(request, 'user/error.html', self.ret)
