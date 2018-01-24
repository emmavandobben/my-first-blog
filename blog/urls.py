from django.conf.urls import url
from . import views

#these URLs point Django to a view named post_list and post_detail
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]

'''     
 ^beginning
 $ ending
 post/   means the url contains this after the beginning
 (?P<pk>\d+) Django will take everything that you place here and transfer it to a view as a variable called pk. \d :  it can only be a digit, not a letter. + : more then one digit. So something like http://127.0.0.1:8000/post// is not valid, but http://127.0.0.1:8000/post/1234567890/ is perfectly OK!
 / – then we need a / again.
 
 That means if you enter http://127.0.0.1:8000/post/5/ into your browser, Django will understand that you are looking for a view called post_detail and transfer the information that pk equals 5 to that view.
 So Django expects in the view a function called post_detail now. 
'''

