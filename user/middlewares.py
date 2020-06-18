from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse
from rest_framework import status
from rest_framework.utils import json


class AuthMD(MiddlewareMixin):  # 验证登录
    ret = {"errCode": 0, "errMsg": u""}  # 默认状态

    def process_request(self, request):  # 请求之前
        request_url = request.path_info
        role_id = request.session.get("role")
        param = request.GET

        if request_url == '/user/login/': #要登陆，执行登录流程
            return None

        if request.session.get("user"):
            if role_id == 1: # role_id 为 1 说明是管理员，不限制权限
                return None
            elif request_url == '/user/query/': # 其他角色，只能进行查询
                return None
            else: # 其他角色，进行修改操作时，提示权限不足
                self.ret["errMsg"] = "权限不足"
                self.ret['errCode'] = status.HTTP_403_FORBIDDEN
                return HttpResponse(json.dumps(self.ret, ensure_ascii=False))

        else:
            self.ret["errMsg"] = "用户未登录"
            self.ret['errCode'] = status.HTTP_400_BAD_REQUEST
        # 错误提示
        return HttpResponse(json.dumps(self.ret, ensure_ascii=False))