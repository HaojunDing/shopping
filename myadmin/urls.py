from django.conf.urls import url
from .views import views,userviews


urlpatterns = [
    url(r'^$', views.index,name='index'),

    # 用户的增删改查
    url(r'^add/$', userviews.add,name='useradd'),
    url(r'^lists/$', userviews.lists,name='userlists'),
    url(r'^delete/$', userviews.delete,name='userdelete'),
    url(r'^edit/$', userviews.edit,name='useredit'),

]
