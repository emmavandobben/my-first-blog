from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    # Is a form that is bound to a model. Can refresh page and show data again to us, by saving it to the db.
    # forms.Form is not connected to a model (its an unbound form), so won t store the data necessarily.

    class Meta:
        model = Post
        fields = ('title', 'text',)

'''
forms.ModelForm : tells Django this form is a ModelForm
class Meta: tells Django which model should be used to create this form (model = Post)
fields in the form

Model metadata is “anything that’s not a field”, 
such as ordering options (ordering), 
database table name (db_table), 
or human-readable singular and plural names 
(verbose_name and verbose_name_plural). 
None are required, and adding class Meta to a 
model is completely optional.

now create URL, view and template.
'''