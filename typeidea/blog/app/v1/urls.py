# -*- coding: UTF-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    # 文章列表
    path('post_list/', views.PostsView.as_view(), name="app-v1-blog-post_list"),

    # test
    path('test_list/', views.TestListView.as_view()),
    path('test_create/', views.TestCreateView.as_view()),
    path('test_retrieve/<int:pk>/', views.TestRetrieveView.as_view()),
    path('test_destroy/<int:pk>/', views.TestDestroyView.as_view()),
    path('test_update/<int:pk>/', views.TestUpdateView.as_view()),
]
