from django.conf.urls import url

from app import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 商品详情
    url(r'^details/(\d+)/$', views.details, name='details'),
    # 注册
    url(r'^registered/$', views.registered, name='registered'),
    # 退出
    url(r'^logout/$',views.logout,name='logout'),
    # 登录
    url(r'^login/$',views.login,name='login'),

    # 购物车
    url(r'^cart/$', views.cart, name='cart'),

    url(r'^addcart/$',views.addcart,name='addcart'),
    url(r'^addgood/$',views.addgood,name='addgood'),
    url(r'^delgood/$',views.delgood,name='delgood')

]