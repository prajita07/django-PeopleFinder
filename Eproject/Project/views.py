from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Order_item, Order, Product, Product_Category, Shipping
from .serializers import Order_itemSerializer, OrderSerializer, Product_CategorySerializer, ProductSerializer, ShippingSerializer,UserSerializer,User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_list_or_404
from django.contrib.auth.models import User
# Create your views here.
class UserViewSet(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    lookup_field = 'id'

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, id = None):

        if id:
            return self.retrieve(Request)
        else:
            return self.list(request)

    def post(self, request):

        return self.create(request)

class UserAPIView( APIView ):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response (serializer.data)


    def post(self, request):
        serializer= UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):

    def get_object(self, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return HttpResponse(Status=status.HTTP_404_NOT_FOUND)


    def get (self, request, id):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
  




class ProductViewSet(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
  
   


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    lookup_field = 'id'

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, id = None):

        if id:
            return self.retrieve(Request)
        else:
            return self.list(request)

    def post(self, request):

        return self.create(request)

    
    def put(self, request, id=None):

        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class ProductAPIView( APIView ):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response (serializer.data)


    def post(self, request):
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetails(APIView):

    def get_object(self, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return HttpResponse(Status=status.HTTP_404_NOT_FOUND)


    def get (self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    def put (self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, id):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderViewSet(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
  
   


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = OrderSerializer
    queryset =Order.objects.all()

    lookup_field = 'id'

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, id = None):

        if id:
            return self.retrieve(Request)
        else:
            return self.list(request)

    def post(self, request):

        return self.create(request)

    
    def put(self, request, id=None):

        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class OrderAPIView( APIView ):
    def get(self,request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response (serializer.data)


def post(self, request):
    serializer= OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetails(APIView):

    def get_object(self, id):
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return HttpResponse(Status=status.HTTP_404_NOT_FOUND)


    def get (self, request, id):
        order = self.get_object(id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


    def put (self, request, id):
        order = self.get_object(id)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, id):
        order = self.get_object(id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ShippingViewSet(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ShippingSerializer
    queryset = Shipping.objects.all()
  
   


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ShippingSerializer
    queryset =Shipping.objects.all()

    lookup_field = 'id'

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):

        return self.create(request)

    
    def put(self, request, id=None):

        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

class ShippingAPIView( APIView ):
    def get(self,request):
        shippings = Shipping.objects.all()
        serializer = ShippingSerializer(shippings, many=True)
        return Response (serializer.data)
        
    def post(self, request):
        serializer= ShippingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShippingDetails(APIView):

    def get_object(self, id):
        try:
            shipping = Shipping.objects.get(id=id)
        except Shipping.DoesNotExist:
            return HttpResponse(Status=status.HTTP_404_NOT_FOUND)


    def get (self, request, id):
        shipping = self.get_object(id)
        serializer = ShippingSerializer(shipping)
        return Response(serializer.data)


    def put (self, request, id):
        shipping = self.get_object(id)
        serializer = ShippingSerializer(shipping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, id):
        shipping = self.get_object(id)
        shipping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



