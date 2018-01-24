from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

'''
forms.ModelForm : tells Django this form is a ModelForm
class Meta: tells Django which model should be used to create this form (model = Post)
fields in the form

now create URL, view and template.
'''