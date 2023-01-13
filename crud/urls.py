from django.contrib import admin
from django.urls import path, include

# We add the urls in the app information
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('information.urls'))
]
