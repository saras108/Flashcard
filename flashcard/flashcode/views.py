from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CardSerializers
from .models import *


"""  Get all the flashcards   """
@api_view(['GET'])
def cards(request):
    cards = Flashcard.objects.all()
    serializer = CardSerializers(cards , many= True)
    return Response(serializer.data)


""" Get the flashcard data having id pk. """
@api_view(['GET'])
def card_data(request, pk):
    cards = Flashcard.objects.get(id = pk)
    serializer = CardSerializers(cards , many= False)
    return Response(serializer.data)

