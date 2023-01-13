from rest_framework import routers
from .api import VideogameViewSet

# From rest_framework we will use a router
# The router allows us to have an easy way of automatically determining the URL conf
# So we can make GET, POST, PUT, etc requests

# We create the router
router = routers.DefaultRouter()
# We define the url and the view
router.register('api/videogames', VideogameViewSet, 'videogames')
# We tell django the urlpatterns with the help of the urls created by our router
urlpatterns = router.urls

