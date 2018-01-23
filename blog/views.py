from django.shortcuts import render
from django.utils import timezone
from .models import Post

#. before models import means in current directory

#return a function render that will render (put together) our template blog/post_list.html.
#the request has info we received from the user via internet.
#'blog/post_list.html' is the template file
#in between {} add something for the template. Here the QuerySet named posts.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})



