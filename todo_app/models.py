from django.db import models

# Create your models here.
# create table todo (id int primary key, title varchar(200)):
# id is created by django automatically
# if there is any change in file (models.py),then always run the following commands:
# python manage.py makemigrations 
#=> detect changes from previous state to current state and create a migration file
# python manage.py migrate 
#=> run the created migration file 
class Todo(models.Model):
    title = models.CharField(max_length=200) 

    def __str__(self):
        return self.title
