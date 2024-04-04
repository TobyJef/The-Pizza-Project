from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Customer Review model

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntergerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['+created_on']
    
    def __str__(self):
        return self.title
    
# Customer Review model

# Review reply model

class Comment(models.Model):
    