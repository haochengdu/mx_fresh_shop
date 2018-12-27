# -*- coding:utf-8 -*-
import django_filters
from django.shortcuts import render
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics

from goods.filter import GoodsFilter
from goods.models import Goods, GoodsCategory
from goods.serializers import GoodsSerializer, CategorySerializer


# class GoodsListView(View):
#     """商品列表-通过django的view实现商品列表页"""
#
#     def get(self, request):
#         json_list = []
#         goods_list = Goods.objects.all()[:5]
#         # for good in goods_list:
#         #     good_dict = dict()
#         #     good_dict["category"] = good.category.id
#         #     good_dict["goods_sn"] = good.goods_sn
#         #     good_dict["name"] = good.name
#         #     good_dict["click_num"] = good.click_num
#         #     good_dict["sold_num"] = good.sold_num
#         #     good_dict["fav_num"] = good.fav_num
#         #     good_dict["goods_num"] = good.goods_num
#         #     good_dict["market_price"] = good.market_price
#         #     good_dict["shop_price"] = good.shop_price
#         #     good_dict["goods_brief"] = good.goods_brief
#         #     good_dict["ship_free"] = good.ship_free
#         #     good_dict["goods_front_image"] = str(good.goods_front_image)
#         #     good_dict["is_new"] = good.is_new
#         #     good_dict["is_hot"] = good.is_hot
#         #     good_dict["add_time"] = good.add_time.strftime('%Y-%m-%d %H:%M:%S')
#         #     json_list.append(good_dict)
#
#         # # 把模型对象序列化,同样时间和url不能序列化，需要转化成字符串
#         # from django.forms.models import model_to_dict
#         # for good in goods_list:
#         #     data_dict = model_to_dict(good, exclude=['goods_front_image', 'add_time'])
#         #     data_dict["goods_front_image"] = str(good.goods_front_image)
#         #     data_dict["add_time"] = good.add_time.strftime('%Y-%m-%d %H:%M:%S')
#         #     json_list.append(data_dict)
#         #
#         # from django.http import HttpResponse
#         # import json
#         # return HttpResponse(json.dumps(json_list, ensure_ascii=False), content_type='application/json')
#
#         # # 使用serializers来序列化模型, 使用JsonResponse多此一举，汉字还是unicode的
#         # from django.core import serializers
#         # json_list = serializers.serialize("json", goods_list)  # 所有的都可以序列化，返回json
#         # import json
#         # data = json.loads(json_list)
#         # from django.http import JsonResponse
#         # # In order to allow non-dict objects to be serialized set the safe parameter to False.
#         # return JsonResponse(data, safe=False)
#
#         # 使用serializers来序列化模型
#         from django.core import serializers
#         json_list = serializers.serialize("json", goods_list, ensure_ascii=False)  # 所有的都可以序列化，返回json
#         from django.http import HttpResponse
#         return HttpResponse(json_list, content_type='application/json')


# class GoodsListView(APIView):
#     """商品列表-使用rest_framework"""
#
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:5]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)

class GoodsPagination(PageNumberPagination):
    """商品列表自定义分页"""
    # 默认每页显示的个数
    page_size = 10
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     """
#     mixins和generic一起用
#     GenericAPIView继承APIView，封装了很多方法，比APIView功能更强大
#     用的时候需要定义queryset和serializer_class
#     GenericAPIView里面默认为空
#     queryset = None
#     serializer_class = None
#     ListModelMixin里面list方法帮我们做好了分页和序列化的工作，只要调用就好了
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

class GoodsListView(ListAPIView):
    """
    上面的代码优化，可以直接继承ListAPIView，ListAPIView主要做了两件事:
        ListAPIView(mixins.ListModelMixin,GenericAPIView)        继承了这两个类
        写好了get方法
    """
    pagination_class = GoodsPagination
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


# class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """商品列表页"""
#
#     # 分页
#     pagination_class = GoodsPagination
#     # 这里必须要定义一个默认的排序,否则会报错
#     queryset = Goods.objects.all().order_by('id')
#     serializer_class = GoodsSerializer


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """商品列表页-分页，搜索，过滤，排序"""

    # 这里必须要定义一个默认的排序,否则会报错
    queryset = Goods.objects.all().order_by('id')
    # 分页
    pagination_class = GoodsPagination
    serializer_class = GoodsSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)

    # 设置filter的类为我们自定义的类
    filter_class = GoodsFilter
    # 搜索,=name表示精确搜索，也可以使用各种正则表达式
    search_fields = ('name', 'goods_brief', 'good_desc')
    # 排序
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    商品分类列表数据
    要想获取某一个商品的详情的时候，继承 mixins.RetrieveModelMixin  就可以了
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer



