from django.views.decorators.csrf import csrf_protect
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsersSerializer
from .models import Users, Roles
from rest_framework import status

# Create your views here.

class GenericAPIView(APIView):
    query_set = None
    serializer_class = None

    def get_queryset(self):
        return self.query_set

    def get_serializer(self, *args, **kwargs):
        try:
            return self.serializer_class(*args, **kwargs)
        except:
            raise ValueError("请传入正确的参数")
class InsertUser(GenericAPIView):
    query_set = Users.objects.all()
    serializer_class = UsersSerializer

    def insert(self, request):
        ser_obj = self.get_serializer(data=request.data)
        data = {'errCode': 0, 'errMsg': u'', 'data': {}}

        if ser_obj.is_valid():
            ser_obj.save()
            data["errCode"] = status.HTTP_200_OK
            data["errMsg"] = "插入成功"
        else:
            data["errCode"] = status.HTTP_400_BAD_REQUEST
            data["errMsg"] = "请传入正确的参数"
        return Response(data)


    def post(self, request):
        return self.insert(request)

class UpdateUser(GenericAPIView):
    query_set = Users.objects.all()
    serializer_class = UsersSerializer

    def update_by_id(self, request):
        data = {'errCode': 0, 'errMsg': u'', 'data': {}}
        param = request.data
        id = None
        try:
            id = param["id"]
        except:
            pass
        if id:
            user = self.get_queryset().filter(id=id).first()
            ser_obj = self.get_serializer(instance=user, data=request.data, partial=True)
            if ser_obj.is_valid():
                ser_obj.save()
                data["errCode"] = status.HTTP_200_OK
                data["errMsg"] = "修改数据成功"
                return Response(data)
        else:
            data["errCode"] = status.HTTP_400_BAD_REQUEST
            data["errMsg"] = "参数错误，请输入想要修改的用户 id"
            return Response(data)

    def put(self, request):
        return self.update_by_id(request)


class DeleteUser(GenericAPIView):
    query_set = Users.objects.all()

    def del_user(self, request):
        data = {'errCode': 0, 'errMsg': u'', 'data': {}}
        param = request.data
        id = None
        account = None
        user = None
        try:
            id = param["id"]
            account = param["account"]
        except:
            pass
        if id is None:
            if account is None:
                data["errCode"] = status.HTTP_400_BAD_REQUEST
                data["errMsg"] = "请输入要删除的用户 id 或账号"
                return Response(data)
            else:
                user = self.get_queryset().filter(account=account).first()

        else:
            user = self.get_queryset().filter(id=id).first()
        if user:
            user.delete()
            data["errCode"] = status.HTTP_200_OK
            data["errMsg"] = "成功删除"
        else:
            data["errCode"] = status.HTTP_400_BAD_REQUEST
            data["errMsg"] = "要删除的用户不存在"
        return Response(data)


    def delete(self, request):
        return self.del_user(request)

class QueryUser(GenericAPIView):
    def query_by_id(self, request):
        data = {'errCode': 0, 'errMsg': u'', 'data':{}}
        param = request.GET
        id = None
        try:
            id = param["id"]
        except:
            pass
        if id is None:
            queryset = Users.objects.all()
            ser_obj = UsersSerializer(queryset, many=True)
        else:
            user_obj = Users.objects.all().filter(id=id).first()
            ser_obj = UsersSerializer(user_obj)
        data["data"] = ser_obj.data
        return Response(data)

    def get(self, request):
        return self.query_by_id(request)

class Login(GenericAPIView):
    query_set = Users.objects.all()
    serializer_class = UsersSerializer

    def post(self, request):
        account = request.data.get("account")
        pwd = request.data.get("password")
        data = {"errCode": status.HTTP_400_BAD_REQUEST,
                "errMsg": u"密码错误，请重新输入"
                }
        try:
            if account:
                user_obj = self.get_queryset().filter(account=account).first()

                ser_obj = self.get_serializer(user_obj)
            if ser_obj.data["password"] == pwd:
                request.session["user"] = ser_obj.data["account"]
                request.session["role"] = ser_obj.data["role_id"]
                data["errCode"] = status.HTTP_200_OK
                data["errMsg"] = "登陆成功"
        except:
            data["errCode"] = status.HTTP_403_FORBIDDEN
            data["errMsg"] = "账号或密码错误"

        return Response(data)