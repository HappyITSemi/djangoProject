#
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status, views
from rest_framework.response import Response
from django_filters import rest_framework as filters


class BookListCreateAPIView(views.APIView):
    # """本モデルの取得（⼀覧） ・登録API クラス"""

    @staticmethod
    def get(request, *args, **kwargs):
        # """本モデルの取得（⼀覧） API に対応するハンドラメソッド"""  # モデルオブジェクトの⼀覧を取得

        book_list = Book.objects.all()  # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book_list, many=True)  # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_200_OK)

    @staticmethod
    def post(request, *args, **kwargs):
        # """本モデルの登録API に対応するハンドラメソッド"""  # シリアライザオブジェクトを作成

        serializer = BookSerializer(data=request.data)  # バリデーション
        serializer.is_valid(raise_exception=True)  # モデルオブジェクトを登録
        serializer.save()  # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_201_CREATED)


class BookRetrieveUpdateDestroyAPIView(views.APIView):
    # """本モデルの取得（詳細） ・更新・⼀部更新・削除API クラス"""

    @staticmethod
    def get(request, pk, *args, **kwargs):
        # """本モデルの取得（詳細） API に対応するハンドラメソッド"""  # モデルオブジェクトを取得

        book = get_object_or_404(Book, pk=pk)  # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book)  # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_200_OK)

    @staticmethod
    def put(request, pk, *args, **kwargs):
        # """本モデルの更新API に対応するハンドラメソッド"""  # モデルオブジェクトを取得

        book = get_object_or_404(Book, pk=pk)  # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book, data=request.data)  # バリデーション
        serializer.is_valid(raise_exception=True)  # モデルオブジェクトを更新
        serializer.save()  # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_200_OK)

    @staticmethod
    def patch(request, pk, *args, **kwargs):
        # """本モデルの⼀部更新API に対応するハンドラメソッド"""  # モデルオブジェクトを取得

        book = get_object_or_404(Book, pk=pk)  # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book, data=request.data, partial=True)  # バリデーション
        serializer.is_valid(raise_exception=True)  # モデルオブジェクトを⼀部更新
        serializer.save()  # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_200_OK)

    @staticmethod
    def delete(request, pk, *args, **kwargs):
        # """本モデルの削除API に対応するハンドラメソッド"""  # モデルオブジェクトを取得

        book = get_object_or_404(Book, pk=pk)

        # モデルオブジェクトを削除
        book.delete()  # レスポンスオブジェクトを返す
        return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
