# -*- coding: utf-8 -*-
from base.apps import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView
from blog.models import Post, Test, Contact, Product, Company
from .serializers import PostsSerializer, TestSerializer, ProductSerializer, CompanySerializer
from base.funtion import value_judge
from base.code import API_1_CONTACT_FAIL


# class PostsViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostsSerializer


class PostsView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    def list(self, request, *args, **kwargs):
        results = super(PostsView, self).list(self, request, *args, **kwargs)
        items = results.data.get('results')
        data = []
        for item in items:
            data.append({
                'id': item.get('id'),
                'title': item.get('title'),
                'created_time': item.get('created_time'),
            })
        return self.response({'code': 0, 'data': data})


class TestListView(ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def list(self, request, *args, **kwargs):
        sql = 'SELECT * FROM blog_test'
        rows = self.get_all_by_sql(sql)
        print('==================================================')
        print(kwargs)
        print(self.request.parser_context)  # url参数 <int:....>
        print(self.request.GET)  # 参数信息
        print(self.request.META)  # 头部信息
        print(self.request.user)
        print('==================================================')

        result_list = []
        result_list.append({'id': 1, 'image': 'http://47.107.69.2:8001/media/a.jpeg'})
        result_list.append({'id': 2, 'image': 'http://47.107.69.2:8001/media/a.jpeg'})
        result_list.append({'id': 3, 'image': 'http://47.107.69.2:8001/media/a.jpeg'})
        return self.response({'code': 0, 'data': result_list})


class TestCreateView(CreateAPIView):
    serializer_class = TestSerializer


class TestRetrieveView(RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return self.response({'code': 0, 'data': serializer.data})


class TestDestroyView(DestroyAPIView):
    queryset = Test.objects.all()

    def delete(self, request, *args, **kwargs):
        super(TestDestroyView, self).delete(self, request, *args, **kwargs)
        return self.response({'code': 0})


class TestUpdateView(UpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestPostView(ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        print(request.data['id'])  # POST的数据

        from django.http import JsonResponse
        return JsonResponse({'code': 0, 'data': '111', 're_data': request.data})

        # return self.response({'code': 0, 'data': '111'})


# ande
class ContactPostView(ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        if value_judge(request, 'name', 'phone', 'email', 'position', 'address') is not True:
            return self.response({'code': API_1_CONTACT_FAIL, 'data': request.data})
        else:
            contact = Contact()
            contact.name = request.data['name']
            contact.phone = request.data['phone']
            contact.email = request.data['email']
            contact.position = request.data['position']
            contact.company = request.data['company']
            contact.address = request.data['address']
            contact.save()

            import datetime
            print(datetime.datetime.now())

            return self.response({'code': 0, 'data': request.data})


class ProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        results = super(ProductView, self).list(request, *args, **kwargs)
        items = results.data.get('results')
        data = dict()
        for item in items:
            data.update({
                item['id']: {'id': item['id'],
                             'name': item['name'],
                             'cover_url': item['cover_url'],
                             'posts_url': item['posts_url'],
                             'video_url': item['video_url'], }

            })
        return self.response({'code': 0, 'data': data})


class CompanyView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request, *args, **kwargs):
        results = super(CompanyView, self).list(request, *args, **kwargs)
        items = results.data.get('results')
        return self.response({'code': 0, 'data': items[0]})

