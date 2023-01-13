from .models import Videogame
from .serializers import VideogameSerializer
from rest_framework import viewsets, permissions

# Then we need to create a ViewSe, this defines the view behavior
# More info at "https://www.django-rest-framework.org/tutorial/quickstart/#views"
# We declare a queryset, allow any service make a petition, and we use our serializer
class VideogameViewSet(viewsets.ModelViewSet):
    queryset = Videogame.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VideogameSerializer