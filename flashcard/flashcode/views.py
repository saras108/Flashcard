from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CardSerializers
from .models import *


"""  Get all the flashcards   """
@api_view(['GET'])
def cards(request):
    cards = Flashcard.objects.all().order_by('-id')
    serializer = CardSerializers(cards , many= True)
    return Response(serializer.data)


""" Get the flashcard data having id pk. """
@api_view(['GET'])
def card_data(request, pk):
    cards = Flashcard.objects.get(id = pk)
    serializer = CardSerializers(cards , many= False)
    return Response(serializer.data)


""" Save the card's data to the database."""
@api_view(['POST'])
def card_create(request):
    serializer = CardSerializers(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

""" Update the card's data to the database."""
@api_view(['POST'])
def card_update(request , pk):
    card = Flashcard.objects.get(id = pk)
    serializer = CardSerializers( instance = card ,data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


""" Delete the card's data from the database."""
@api_view(['DELETE'])
def card_delete(request , pk):
    card = Flashcard.objects.get(id = pk)
    card.delete()    
    return Response("Selected data sucessfully deleted!")


""" Update the status to remembred to False to True and True to False respectively!"""
@api_view(['POST'])
def card_remember(request , pk):    
    card = Flashcard.objects.get(id = pk)
    serializer = CardSerializers( instance = card ,data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)