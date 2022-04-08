from django.shortcuts import render
from rest_framework import  generics
from rest_framework.response import Response

from places_to_rest.models import PlacesToRest
from places_to_rest.serializers import PlacesSerializer


class PlacesAPIView(generics.ListAPIView):
    def get(self, request):
        p = PlacesToRest.objects.all()
        return Response({'posts1': PlacesSerializer(p, many=True).data})

    def post(self, request):
        serializer = PlacesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return  Response({"error": "Method PUT not allowed"})

        try:
            instance = PlacesToRest.objects.get(pk=pk)
        except:
            return  Response({"error": "Object does not exist"})

        serializer = PlacesSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return  Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            instance = PlacesToRest.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})
        instance.delete()
        return Response({"post": "delete post " + str(pk)})







