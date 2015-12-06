from django.db import models
from django.contrib.auth.models import User

class blog(models.Model):
  author = models.ForeignKey(User)
  title = models.CharField(max_length = 50)
  subtitle = models.CharField(max_length = 50 , default = "this is a good blog")
  text = models.CharField(max_length = 500)
  img = models.ImageField(null = True)
  def __unicode__(self):
    return self.title

class comment(models.Model):
  author = models.CharField(max_length = 50)
  text = models.CharField(max_length = 50)
  blog = models.ForeignKey(blog)
  def __unicode__(self):
    return self.blog.title
