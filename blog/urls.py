from django.conf.urls import include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

# router makes it possible to go to a general api site (api/v1) and from there route to different api's.
# You use Viewsets with routers.
router = DefaultRouter()
router.register(r'posts', views.PostViewSet, base_name='post')
router.register(r'user', views.UserViewSet, base_name='user')

api_urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]

#these URLs point Django to a view named post_list and post_detail
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^api/posts/$', views.APIPostList.as_view(), name='api_post_list'),
    url(r'^api/post/(?P<pk>\d+)/$', views.APIPostDetail.as_view(), name='api_post_detail'),
    url(r'^users/$', views.UserList.as_view(), name='api_user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='api_user_detail'),
    url(r'^api-auth/', include('rest_framework.urls')),
] + api_urlpatterns

#urlpatterns = format_suffix_patterns(urlpatterns)


'''     
 ^beginning
 $ ending
 post/   means the url contains this after the beginning
 (?P<pk>\d+) Django will take everything that you place here and transfer it to a view as a variable called pk. \d :  it can only be a digit, not a letter. + : more then one digit. So something like http://127.0.0.1:8000/post// is not valid, but http://127.0.0.1:8000/post/1234567890/ is perfectly OK!
 / – then we need a / again.
 
 That means if you enter http://127.0.0.1:8000/post/5/ into your browser, Django will understand that you are looking for a view called post_detail and transfer the information that pk equals 5 to that view.
 So Django expects in the view a function called post_detail now. 
'''

