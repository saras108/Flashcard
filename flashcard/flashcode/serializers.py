from rest_framework import serializers
from .models import *

class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = "__all__"