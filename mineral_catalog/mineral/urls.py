from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.mineralsList, name='mineral_list'),
    url(r'^random/$', views.randomMineral, name='random_mineral'),
    url(r'^(?P<name>.*)/$', views.mineralDetail, name='mineral_detail'),
]
