from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class meta:
        ordering =['title',]
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title
class Post(models.Model):
    category = models.ForeignKey(Category,related_name= 'posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    intro = models.TextField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering =['-created_on']

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.EmailField()
    body=models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)