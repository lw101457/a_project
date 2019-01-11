from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    # url(r'^registere/$',views.registere,name='registere'),
    # url(r'^phone/$',views.phone,name='phone'),
]