import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Women

class WomenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = "__all__"

# TESTOVIE CLASS
# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# TESTOVAYA FUNKSIYA DLA TETOVOGO CLASSA
# def encode():
#     model = WomenModel('Angelina Jolie', 'content: Angelina Jolie')
#     model_sr = WomenSerializers(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data) 
#     print(json)   


# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie", "content":"content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializers(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)