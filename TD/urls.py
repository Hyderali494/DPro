from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^test/$',views.test,name = "test"),
url(r'^showLogin/$',views.showLogin,name="showLogin"),
url(r'^getLogin/$',views.getLogin,name='getLogin'),
url(r'^showRegister/$',views.showRegister,name='showRegister'),
url(r'^getRegister/$',views.getRegister,name='getRegister'),
url(r'^jsonview/$',views.jsonview,name = 'jsonview'),
]
