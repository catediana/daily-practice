from rest_framework import serializers
from .models import Book

#  1. serializer for my book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
