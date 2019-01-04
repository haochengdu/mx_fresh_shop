#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/4 10:01
@Author  : TX
@File    : serializers.py
@Software: PyCharm
"""
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from user_operation.models import UserFav


class UserFavSerializer(serializers.ModelSerializer):

    # class Meta:
    #     model = UserFav
    #     fields = "__all__"
    # 获取当前登录的用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        # validate实现唯一联合，一个商品只能收藏一次
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                # message的信息可以自定义
                message="已经收藏"
            )
        ]
        model = UserFav
        # 收藏的时候需要返回商品的id，因为取消收藏的时候必须知道商品的id是多少
        fields = ("user", "goods", 'id')











