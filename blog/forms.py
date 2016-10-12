from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post    #indicamos a Django el modelo a utilizar.
        fields = ('title', 'text',) #Indicamos los campos de nuestro formulario.
