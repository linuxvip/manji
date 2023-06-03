import json
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Database

# FBV
def database_info(request):
    if request.method == "GET":
        database_list = Database.objects.all()
        result = {
            "code": 200,
            "msg": "Succeed",
            "data": list(database_list.values())
        }
        return JsonResponse(result)

    elif request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        host = data.get('host')
        user = data.get('user')
        password = data.get('password')
        port = data.get('port')

        database = Database.objects.create(name=name, host=host, user=user,password=password, port=port)
        result = {
            "code": 201,
            "msg": "Succeed",
            "data": {
                "name": database.name,
                "host": database.host,
                "user": database.user,
                "password": database.password,
                "port": database.port
            }
        }
        return JsonResponse(result)



# CBV class based view

class DatabaseView(View):
    def post(self, request):
        # 创建数据库
        data = json.loads(request.body)
        name = data.get('name')
        host = data.get('host')
        user = data.get('user')
        password = data.get('password')
        port = data.get('port')

        database = Database(name=name, host=host, user=user, password=password, port=port)
        database.save()

        return JsonResponse({'message': 'Database created successfully'})

    def get(self, request, pk=None):
        # 获取所有数据库或单个数据库
        if pk is None:
            databases = Database.objects.order_by('id').values()
            # 添加分页逻辑
            page_number = request.GET.get('page')  # 获取当前页码参数
            page_size = request.GET.get('page_size', 10)  # 获取每页显示数量，默认为10条

            # 分页器
            paginator = Paginator(databases, page_size)  # 创建Paginator实例，传入数据集和每页显示数量
            page = paginator.get_page(page_number)  # 获取指定页的数据

            # 构建分页结果
            result = {
                'total_pages': paginator.num_pages,  # 总页数
                'current_page': page.number,  # 当前页码
                'databases': list(page.object_list)  # 当前页的数据库列表
            }
            return JsonResponse(result)

        else:
            database = get_object_or_404(Database, id=pk)
            return JsonResponse({'database': {
                'name': database.name,
                'host': database.host,
                'user': database.user,
                'password': database.password,
                'port': database.port,
            }})

    def put(self, request, pk):
        # 更新数据库
        database = get_object_or_404(Database, id=pk)
        data = json.loads(request.body)

        database.name = data.get('name')
        database.host = data.get('host')
        database.user = data.get('user')
        database.password = data.get('password')
        database.port = data.get('port')
        database.save()

        return JsonResponse({'message': 'Database updated successfully'})

    def delete(self, request, pk):
        # 删除数据库
        database = get_object_or_404(Database, id=pk)
        database.delete()

        return JsonResponse({'message': 'Database deleted successfully'})
