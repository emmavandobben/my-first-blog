from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .forms import PostForm
from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
from .serializers import UserSerializer


#. before models import means in current directory

#return a function render that will render (put together) our template blog/post_list.html.
#the request has info we received from the user via internet.
#'blog/post_list.html' is the template file
#in between {} add something for the template. Here the QuerySet named posts.

def post_list(request):
    posts = Post.objects.filter()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

"""
save the form with form.save
commit=False means that we don't want to save the Post model yet – we want to add the author first.
add an author 
preserve changes
go to the post_detail view, this view requires a pk variable. 

als het geen POST is, naar else. Create new post form.

"""

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


class APIPostList(generics.ListCreateAPIView):
    """
    List or create a post instance.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class APIPostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a post instance.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # Overriding a .perform_create() method.
    # Modify how the instance save is managed
    # The create() method of our serializer will now be passed
    # an additional 'owner' field, along with validated data from the request

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('api_user_list', request=request, format=format),
        'posts': reverse('api_post_list', request=request, format=format)
    })