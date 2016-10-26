from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from testApp.serializers import UserSerializer, TestSerializer
from .models import Test

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def test_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        t = Test.objects.all()
        serializer = TestSerializer(t, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def test_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        t = Test.objects.get(pk=pk)
    except t.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TestSerializer(t)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TestSerializer(t, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        t.delete()
        return HttpResponse(status=204)
