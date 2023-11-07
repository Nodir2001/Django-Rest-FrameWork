from django.shortcuts import render
from django.forms import model_to_dict

from .serializers import WomenSerializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response 
1
from .models import Women

# prejni class pered glazami
#class WomenAPIView(generics.ListAPIView):
#    queryset = Women.objects.all()
#    serializer_class = WomenSerializers

class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers

class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers   

class WomanAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers   
    
#APIView stavitsa tak kak on bazoviy    
# class WomenAPIView(APIView):
#     def get(self, request):
#             # tut mi dostaem vsu info is Women class ono predstavleno v formate queryset()
#             # choti poluchit v JSOn dobavim .values()     
#         # lst = Women.objects.all().values()  
#             # s pomoshyu response mi vozvrashaem polzovaletu jsong zapros
#             # no v dannom sluchai method POST ne rasreshon    
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializers(w, many=True).data})
                        
#     def post(self, request):
#         serializer = WomenSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # pri methode POST me poluchim resultat    
#         return Response({'post': serializer.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
        
#         try:
#             isinstance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not allowed"})
        
#         serializer = WomenSerializers(data=request.data, instance=isinstance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
        
#         # here you can delete wrote with key pk
#         try:
#             isinstance=Women.objects.get(pk=pk)
#             isinstance.delete()
#         except:
#             return Response({"error":"Object not found !"})    

#         return Response({"post": "delete post" + str(pk)})