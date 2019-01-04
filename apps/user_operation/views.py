from django.shortcuts import render
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets

from user_operation.models import UserFav
from user_operation.serializers import UserFavSerializer


class UserFavViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """当前用户对商品的收藏取消收藏，查询所有收藏"""
    # 先要让用户登录，没有登录不执行操作
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer








