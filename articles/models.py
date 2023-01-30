from email import *
#from tkinter import Tk
#from turtle import *
from django.db import models
from django.conf import * 
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Article(models.Model):
    """cette class permet de créer la table article dans la base de donné et  definir les propriétées et types des propriétées liées  à chaque propriété"""
    title = models.CharField(max_length = 255)
    body = RichTextField(blank=True, null= True)
    #body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(
        get_user_model(), on_delete = models.CASCADE
        )

    
    
    def __str__(self):
        """methode __str__ permettant dafficher le modele dans notre interface d'administration et retourne le titre """
        return self.title

    def get_absolute_url(self):
        """methode permettant dafficher le modele dans notre interface d'administration et retourne le detail de larticle  """
        return reverse('article_detail', args=[str(self.id)])

class Comment(models.Model):
        """cette class permet de créer la table Comment dans la base de donné et  definir les propriétées et types des propriétées liées à chaque propriété """
        article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name = 'comments',) #le releated_name ajouter ici est un champs lié a un commentaire spécifique qui sera peut etre requeté  par un utilisateur
        comment = RichTextField(blank=True, null= True)
        #comment = models.TextField()
        author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
        def __str__(self):
            """methode __str__ permettant d'afficher le modele dans linterface d'administration et retourne le commentaire"""
            return self.comment

        def get_absolute_url(self):
            """cette methode permet d'afficher le modele dans notre interface d'administration la liste darticle"""
            return reverse('article_list')


#nestor : creation de model pour subscribe


class SubscribedUsers(models.Model):
    email = models.CharField(unique=True, max_length=50)
    #name = models.CharField(max_length=50)
    #message = models.TextField()

    

    def isExists(self):
        if SubscribedUsers.objects.filter(email = self.email):
            return True
        return False






