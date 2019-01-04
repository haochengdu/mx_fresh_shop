#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 18-11-21 下午5:08
@Author  : TX
@File    : serializers.py.py
@Software: PyCharm
"""
from rest_framework import serializers

from goods.models import Goods, GoodsCategory, GoodsImage


# # 用Serializer实现的，需要自己手动添加字段，如果用Modelserializer，会更加的方便，直接用__all__就可以全部序列化
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()


class CategorySerializer3(serializers.ModelSerializer):
    """三级分类"""

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    """二级分类"""
    # 在parent_category字段中定义的related_name="sub_cat" 
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """商品一级类别序列化"""
    # 在parent_category字段中定义的related_name="sub_cat"
    sub_cat = CategorySerializer2(many=True)
    # category_type = serializers.CharField(source='get_category_type_display')

    class Meta:
        model = GoodsCategory
        fields = "__all__"
        depth = 2


class GoodsImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsImage
        fields = ["image", ]


class GoodsSerializer(serializers.ModelSerializer):
    # category只显示分类的id，Serialzer还可以嵌套使用，覆盖外键字段，也可以直接使用depth
    category = CategorySerializer()  # 外键字段的覆盖
    # 这种选择显示只能嵌套一层
    # category_type = serializers.CharField(source='category.get_category_type_display')
    # images是数据库中设置的related_name="images"，把轮播图嵌套进来
    images = GoodsImagesSerializer(many=True)

    class Meta:
        model = Goods()
        fields = "__all__"
        depth = 2




