from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from places_to_rest.models import UsersActivity
from testsite.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsAdminOrOwnerOrReadOnly
from .models import PlacesToRest, Category
from .serializers import PlacesSerializer

# class PlacesViewSet(viewsets.ModelViewSet):
#     #queryset = PlacesToRest.objects.all()
#     serializer_class = PlacesSerializer
#
#     def get_queryset(self):
#         pk =self.kwargs.get("pk")
#
#         if not pk:
#             return PlacesToRest.objects.all()[:2]
#         return PlacesToRest.objects.filter(pk=pk)
#
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return  Response({'cats': cats.name})


#
class PlacesAPIList(generics.ListCreateAPIView):
    queryset = PlacesToRest.objects.all()
    serializer_class = PlacesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
#
class PlacesAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = PlacesToRest.objects.all()
    serializer_class = PlacesSerializer
    permission_classes = (IsAdminOrOwnerOrReadOnly,)

#
# class PlacesAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = PlacesToRest.objects.all()
#     serializer_class = PlacesSerializer
#     permission_classes = (IsAdminOrReadOnly, )
#
class PlacesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlacesToRest.objects.all()
    serializer_class = PlacesSerializer
    permission_classes = (IsAdminOrOwnerOrReadOnly, )

# class PlacesAPIView(generics.ListAPIView):
#     def get(self, request):
#         p = PlacesToRest.objects.all()
#         return Response({'posts1': PlacesSerializer(p, many=True).data})
#
#     def post(self, request):
#         serializer = PlacesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return  Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = PlacesToRest.objects.get(pk=pk)
#         except:
#             return  Response({"error": "Object does not exist"})
#
#         serializer = PlacesSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return  Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         try:
#             instance = PlacesToRest.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
#         instance.delete()
#         return Response({"post": "delete post " + str(pk)})







