from django.conf.urls import  patterns,url
from myapp import  views
urlpatterns = patterns('' ,
                       url(r'^$', views.first_page),
                       url(r'^yahoo_finanace/$',views.yahoo_finanace, name="yahoo_finanace")
                       )
