from django.db import models
# Create your models here.
class BlogPost(models.Model):
  title = models.CharField(max_length = 150)
  slug = models.CharField(max_length = 150)
  body = models.TextField()
  pub_date = models.DateTimeField()

 
