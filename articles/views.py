#from itertools import product
#from multiprocessing import context
#from pyexpat import model
#from re import L, T
from sqlite3 import IntegrityError
#from turtle import home, title
#from urllib import request
from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,UserPassesTestMixin) # new nestor 
from django.views.generic.edit import UpdateView, DeleteView #new nestor
from django.views.generic import ListView, DetailView, CreateView # new nestor 
from .models import Article, Comment, SubscribedUsers
from django.urls import reverse_lazy # new nestor
#from django.contrib import messages
#from django.shortcuts import get_object_or_404
#from django.http import HttpResponseRedirect
from django.shortcuts import redirect

#import re


#from django.http import HttpResponse
#from django.conf import settings

# Create your views here.
class ArticleListView(LoginRequiredMixin,ListView): #new nestor ajout du  LoginRequiredMixin au paramettre
    model = Article
    template_name = 'article_list.html'
    
       

 
  

    


    

class ArticleDetailView(LoginRequiredMixin, DetailView): #new nestor ajout du  LoginRequiredMixin au paramettre
        model = Article
        template_name = 'article_detail.html'



class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #new nestor ajout du  LoginRequiredMixin au paramettre
    model = Article
    fields = ('title', 'body',) 
    template_name = 'article_edit.html'
    #ajout du test function de UserPassesTestMixin
    def test_func(self): #new nestor
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #new nestor ajout du  LoginRequiredMixin au paramettre
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    #ajout du test function de UserPassesTestMixin
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin,CreateView): #new nestor ajout du  LoginRequiredMixin au paramettre
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)# new nestor on enlève la liste d'auteur  coorrespondant au champ auteur puis on defini une méthode qui prend automatiquement en compte l'auteur du poste 

    def form_valid(self, form) :
        """cette méthode est utilisée pour capturer automatiquement le nom de l'auteur d' un post"""
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, CreateView): # nestor
    model = Comment
    template_name = 'create_comment.html'
    fields = ('article','comment')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
       
#nestor new  : ici il sagit dune "classe base view" pour effectuer une recherche sur le formulaire de liste d'articles
class ArticleSearchView(ListView):
    """cette classe va nous permettre d'effectuer une recherche dans la base de donnee article """
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        query = self.request.GET.get('q') 
        return Article.objects.filter(title__icontains=query).order_by('date')
            
#nestor fonction 
   
def index_portfolio(request):
   try:
       if request.method == 'POST':

       
          post_data = request.POST.copy()
          email = post_data.get("email", None)
          #name = post_data.get("name", None)
          #message = post_data.get("message", None)
          subscribedUsers = SubscribedUsers()
          subscribedUsers.email = email
          #subscribedUsers.name = name
          #subscribedUsers.message = message
          subscribedUsers.save()
         
       
          #return  HttpResponse("success! Veuillez retourner à la page article  ici  ")
       return render(request, 'index_portfolio.html')
   except IntegrityError:
        return redirect('index_portfolio')
   finally:
        return render(request,'index_portfolio.html')

    



    



       
      
 # send a confirmation mail
#subject = 'NewsLetter Subscription'
#messages = 'Hello ' + name + ', Thanks for subscribing us. You will get notification of latest articles posted on our website. Please do not reply on this email.'
#email_from = settings.EMAIL_HOST_USER
#recipient_list = [email, ]
#send_mail(subject, messages, email_from, recipient_list)
#res = JsonResponse({'msg': 'Thanks. Subscribed Successfully!'}
#return render(request, 'index_portfolio.html')
   






        #elif subscribedusers.isExists():
            #error_message = 'Email addresse already registrated '
 #saving
       
    

   




         








