#nestor file
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm): # la class Meta  est utilisée pour remplacer les champs par defaut en definissant le modele a notre CustomUser
                                  #et en utilisant les champs par defaut via meta.fields qui inclus tous les champs par defaut champs
        model = CustomUser
        #fields = UserCreationForm.Meta.fields + ('age',) #changement de cette ligne par la ligne suivante
        fields = ('username','email','age',)#new nestor



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        #fields = UserChangeForm.Meta.fields #changement de cette ligne par la ligne suivante
        fields = ('username','email','age',)
