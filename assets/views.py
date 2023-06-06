from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View
from .models import AssetsCategory, Assets


class AssetsCategoryListView(View):
    """
    使用Django最基础的类，来处理http请求，并生成响应。
    """
    def get(self, request):
        """
        定义了 get 方法，用于处理 GET 请求。
        """
        page_num = request.GET.get('page_num', 1)
        page_size = request.GET.get('page_size', 10)

        categories = AssetsCategory.objects.all()
        paginator = Paginator(categories, page_size)
        page_obj = paginator.get_page(page_num)

        data = {
            'code': 200,
            'message': 'Success',
            'data': {
                # 总条数
                'count': paginator.count,
                # 总页数
                'num_pages': paginator.num_pages,
                # 当前页码
                'page_number': page_obj.number,
                # 是否有上一页
                'has_previous': page_obj.has_previous(),
                # 是否有下一页
                'has_next': page_obj.has_next(),
                'results': [{'id': category.id, 'name': category.name} for category in page_obj]
            }
        }

        return JsonResponse(data)

    def post(self, request):
        # 处理创建资产分类的逻辑
        # 获取请求中的数据
        name = request.POST.get('name')
        parent_category_id = request.POST.get('parent_category')

        # 创建资产分类对象
        category = AssetsCategory.objects.create(name=name, parent_category_id=parent_category_id)

        data = {
            'code': 201,
            'message': 'Created',
            'data': {
                'id': category.id,
                'name': category.name,
                'parent_category': category.parent_category_id
            }
        }

        return JsonResponse(data, status=201)

    def put(self, request):
        # 处理更新资产分类的逻辑
        # 获取请求中的数据
        category_id = request.POST.get('id')
        name = request.POST.get('name')
        parent_category_id = request.POST.get('parent_category')

        try:
            category = AssetsCategory.objects.get(id=category_id)
        except AssetsCategory.DoesNotExist:
            data = {'code': 404, 'message': 'Category not found'}
            return JsonResponse(data, status=404)

        # 更新资产分类对象
        category.name = name
        category.parent_category_id = parent_category_id
        category.save()

        data = {
            'code': 200,
            'message': 'Success',
            'data': {
                'id': category.id,
                'name': category.name,
                'parent_category': category.parent_category_id
            }
        }

        return JsonResponse(data)

    def delete(self, request):
        # 处理删除资产分类的逻辑
        # 获取请求中的数据
        category_id = request.GET.get('id')

        try:
            category = AssetsCategory.objects.get(id=category_id)
        except AssetsCategory.DoesNotExist:
            data = {'code': 404, 'message': 'Category not found'}
            return JsonResponse(data, status=404)

        # 删除资产分类对象
        category.delete()

        data = {'code': 204, 'message': 'Category deleted'}
        return JsonResponse(data, status=204)


class AssetsListView(View):
    def get(self, request):
        page_num = request.GET.get('page_num', 1)
        page_size = request.GET.get('page_size', 10)

        # assets = Assets.objects.all()
        assets = Assets.objects.select_related('assets_category').order_by('id')

        paginator = Paginator(assets, page_size)
        page_obj = paginator.get_page(page_num)

        data = {
            'code': 200,
            'message': 'Success',
            'data': {
                'count': paginator.count,
                'num_pages': paginator.num_pages,
                'page_number': page_obj.number,
                'has_previous': page_obj.has_previous(),
                'has_next': page_obj.has_next(),
                'results': [
                    {
                        'id': asset.id,
                        'name': asset.name,
                        'address': asset.address,
                        'is_active': asset.is_active,
                        'assets_category': asset.assets_category_id,
                        # 'assets_category': {
                        #     "category_id": asset.assets_category.id,
                        #     "category_name": asset.assets_category.name
                        # },
                        'created_by': asset.created_by,
                        'updated_by': asset.updated_by,
                        'date_created': asset.date_created,
                        'date_updated': asset.date_updated,
                        'desc': asset.desc
                    }
                    for asset in page_obj
                ]
            }
        }

        return JsonResponse(data)

    def post(self, request):
        # 处理创建资产的逻辑
        # 获取请求中的数据
        name = request.POST.get('name')
        address = request.POST.get('address')
        is_active = request.POST.get('is_active')
        assets_category_id = request.POST.get('assets_category')

        # 创建资产对象
        asset = Assets.objects.create(name=name, address=address, is_active=is_active,
                                      assets_category_id=assets_category_id)

        data = {
            'code': 201,
            'message': 'Created',
            'data': {
                'id': asset.id,
                'name': asset.name,
                'address': asset.address,
                'is_active': asset.is_active,
                'assets_category': asset.assets_category_id,
                'created_by': asset.created_by,
                'updated_by': asset.updated_by,
                'date_created': asset.date_created,
                'date_updated': asset.date_updated,
                'desc': asset.desc
            }
        }

        return JsonResponse(data, status=201)

    def put(self, request):
        # 处理更新资产的逻辑
        # 获取请求中的数据
        asset_id = request.POST.get('id')
        name = request.POST.get('name')
        address = request.POST.get('address')
        is_active = request.POST.get('is_active')
        assets_category_id = request.POST.get('assets_category')

        try:
            asset = Assets.objects.get(id=asset_id)
        except Assets.DoesNotExist:
            data = {'code': 404, 'message': 'Asset not found'}
            return JsonResponse(data, status=404)

        # 更新资产对象
        asset.name = name
        asset.address = address
        asset.is_active = is_active
        asset.assets_category_id = assets_category_id
        asset.save()

        data = {
            'code': 200,
            'message': 'Success',
            'data': {
                'id': asset.id,
                'name': asset.name,
                'address': asset.address,
                'is_active': asset.is_active,
                'assets_category': asset.assets_category_id,
                'created_by': asset.created_by,
                'updated_by': asset.updated_by,
                'date_created': asset.date_created,
                'date_updated': asset.date_updated,
                'desc': asset.desc
            }
        }

        return JsonResponse(data)

    def delete(self, request):
        # 处理删除资产的逻辑
        # 获取请求中的数据
        asset_id = request.GET.get('id')

        try:
            asset = Assets.objects.get(id=asset_id)
        except Assets.DoesNotExist:
            data = {'code': 404, 'message': 'Asset not found'}
            return JsonResponse(data, status=404)
        #
        # # 删除资产对象
        # asset.delete()
        asset.is_delete = True
        asset.save()

        data = {'code': 204, 'message': 'Asset deleted'}
        return JsonResponse(data, status=204)

