from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.urls import reverse


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar/', blank=True, null=True)
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='article_user_set')
    description = models.TextField(blank=True)
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='article_user_set')

    def __str__(self):
        return self.username



class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    tags = models.ManyToManyField('Tag')
    featured_image = models.ImageField(upload_to='article_images/')
    views_count = models.PositiveIntegerField(default=0) 

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.timestamp}"



class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()

    def __str__(self):
        return f"Comment by {self.user} on {self.timestamp}"
