from xml.etree.ElementTree import Comment
from django.contrib import admin

from .models import Article, Comment, SubscribedUsers#new nestor

# Register your models here.

class CommentInline(admin.TabularInline):#new nestor , StackedInline peut etre utiliser a la place de tabularinline juste une question de preference
    model = Comment 

class ArticleAdmin(admin.ModelAdmin): #new nestor
    inlines = [
        CommentInline,
    ]
admin.site.register(Article, ArticleAdmin) # new nestor
admin.site.register(Comment) #new nestor
admin.site.register(SubscribedUsers)

