from rest_framework import generics
from squared_app.models import Squared
from squared_app.serializers import SquaredSerializer


class SquaredListView(generics.ListCreateAPIView):
    queryset = Squared.objects.all()
    serializer_class = SquaredSerializer

class SquaredItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Squared.objects.all()
    serializer_class = SquaredSerializer
