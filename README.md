# DjangoRestFramework
Here you will find a little project created with Django that uses Django REST Framework so you can understand and see what are the possibilities with REST FRamework :)
This is a little project that is for any person that has a basic understanding in Django and wants to meet Django REST Framework

### How to use
First clone this repo into your personal computer, this contains the environment and you just have to run it, depending what system you are using
Run py manage.py runserver and use a client to make petitions to the API created
You can use the view created by Django REST Framework, but it´s better with a client like POSTMAN, THUNDERCLIENT, ETC.
Before you continue to the next section, read the code and our comments so you can understand better what we are doing

### Examples
With this project we can make a lot of REST petitions with the Api created

BASIC GET URL: http://localhost:8000/api/videogames/
When you run this Django will send you all the objects of our Model Videogame

If you add numbers after that url you will get the specific object with that id, for example:
http://localhost:8000/api/videogames/1/

BASIC POST URL: http://localhost:8000/api/videogames/
You will need to send a Json with just the name and description, then Django will create the object in the database

BASIC PUT OR PATCH URL: http://localhost:8000/api/videogames/1/
You will need to send a Json with the the part that you want to modify from an object, you need to add the id in the url

As you can see we have a lot of urls, so we created a huge API but really basic, Django REST Framwework is doing all the job
It creates the urls, the petitions in the database and more!
You read the code and there are just few lines, imagine what you can create with the power of REST Framework
