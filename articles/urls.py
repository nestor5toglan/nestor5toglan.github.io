from django.urls import path
from . import views 
from .views  import (
    ArticleListView, #new nestor
    ArticleUpdateView,# new nestor
    ArticleDetailView,# new nestor
    ArticleDeleteView, # new nestor
    ArticleCreateView,# new nestor 
    CommentCreateView, #new nestor

  
    
    )

urlpatterns = [
    
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name= 'article_edit'), #new nestor
    path('<int:pk>/', ArticleDetailView.as_view(), name = 'article_detail'), #new nestor
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name = 'article_delete'),# new nestor
    path('new/', ArticleCreateView.as_view(), name = 'article_new'), #new nestor
    path('<int:pk>/comment/', CommentCreateView.as_view(), name= 'create_comment') ,#nestor
    path('search_article/', views.ArticleSearchView.as_view(), name='search_article'),
    path('index_portfolio/', views.index_portfolio,name='index_portfolio'),
    
   
    path('', ArticleListView.as_view(), name='article_list'),
]