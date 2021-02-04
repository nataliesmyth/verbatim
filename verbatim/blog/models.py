# Create your models here.
# Now we will define the data models for our blog. A model is a Python class that subclasses django.db.models.Model, in which each attribute represents a database field. Using this subclass functionality, we automatically have access to everything within django.db.models.Models and can add additional fields and methods as desired. We will have a Post model in our database to store posts.

# import the class models
from django.db import models
from django.contrib.auth.models import User

# creating a tuple for post status allows us to keep drafts and published posts separated when rendered with templates
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
# create a subclass of models.Model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.titl

# The Meta class inside the model contains metadata. We tell Django to sort results in the created_on field in descending order by default when we query the database. We specify descending order using the negative prefix. By doing so, posts published recently will appear first.

# The __str__() method is the default human-readable representation of the object. Django will use it in many places, such as the administration site.

# Now that our new database model is created we need to create a new migration record for it and migrate the change into our database.

# (django) $ python manage.py makemigrations 
# (django) $ python manage.py migrate