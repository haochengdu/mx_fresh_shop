# -*- coding:utf-8 -*-
"""mx_fresh_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.urls import re_path
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

import xadmin
from goods.views import GoodsListView, GoodsListViewSet, CategoryViewSet
from mx_fresh_shop.settings import MEDIA_ROOT

router = DefaultRouter()
# 配置goods的url
router.register(r'goods', GoodsListViewSet)
# 配置Category的url
router.register(r'categorys', CategoryViewSet, base_name="categorys")

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    # 媒体文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    # drf文档，title自定义
    path('docs', include_docs_urls(title='仙剑奇侠传')),
    path('api-auth/', include('rest_framework.urls')),
    re_path('^', include(router.urls)),
    # path('goods/', GoodsListView.as_view(), name='goods-list'),  # 商品列表页

    # token
    path('api-token-auth/', views.obtain_auth_token),
]
