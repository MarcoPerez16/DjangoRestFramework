from django.db import models

# We neeed to create a model, in this example is videogame
# as we know Django will create a table depending the selected database(sqlite, postgress, etc)
# Lets create a model that contains information about a videogame
class Videogame(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)