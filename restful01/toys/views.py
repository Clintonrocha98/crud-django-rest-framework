from rest_framework.viewsets import ModelViewSet
from .models import Toy
from .serializers import ToySerializer


class ToysViewSet(ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer