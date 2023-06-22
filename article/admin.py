from django.contrib import admin

# Register your models here.
from .models import User, Article, Category, Tag, Comment, Rating

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Rating)