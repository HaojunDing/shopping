from django.conf.urls import url
from .views import views,userviews,typesviews


urlpatterns = [
    url(r'^$', views.index,name='index'),

    # 用户的增删改查
    url(r'^add/$', userviews.add,name='useradd'),
    url(r'^lists/$', userviews.lists,name='userlists'),
    url(r'^delete/$', userviews.delete,name='userdelete'),
    url(r'^edit/$', userviews.edit,name='useredit'),


    # 商品的增删改查
    url(r'^tadd/$', typesviews.add,name='typesadd'),
    url(r'^tlists/$', typesviews.lists,name='typeslists'),
    url(r'^tdelete/$', typesviews.delete,name='typesdelete'),
    url(r'^tedit/$', typesviews.edit,name='typesedit'),

]
