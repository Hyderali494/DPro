from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^test/$',views.test,name = "test"),
url(r'^showLogin/$',views.showLogin,name="showLogin"),
url(r'^getLogin/$',views.getLogin,name='getLogin'),
url(r'^showRegister/$',views.showRegister,name='showRegister'),
url(r'^getRegister/$',views.getRegister,name='getRegister'),
url(r'^jsonview/$',views.jsonview,name = 'jsonview'),
url(r'^showContact/$',views.showContact,name='showContact'),
url(r'^getContact/$',views.getContact,name='getContact'),
url(r'^dispContacts/$',views.dispContacts,name='dispContacts'),
url(r'^showUpdate/$',views.showUpdate,name = 'showUpdate'),
url(r'^getUpdate/$',views.getUpdate,name = 'getUpdate'),
url(r'^showUp/$',views.showUp,name = 'showUp'),
url(r'^showDelete/$',views.showDelete,name = 'showDelete'),
url(r'^getDelete/$',views.getDelete,name = 'getDelete'),
url(r'^getFixed/$',views.getFixed,name='getFixed'),
]
