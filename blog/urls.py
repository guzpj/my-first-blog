from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.post_list),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
                # ^ el principio.
                # post/ después del comienzo, la dirección URL debe contener la palabra post y /.
                # (?P<pk>[0-9]+) Django llevará todo lo que coloques aquí y lo transferirá
                # a una vista como una variable llamada pk (primary key). [0-9], indica que
                # sólo puede ser un número, no una letra (todo debería estar entre 0 y 9).
                # + significa que tiene que haber uno o más dígitos.
                #/ necesario para que la url termine en /.
                #$ indica el final.
        url(r'^post/new/$', views.post_new, name='post_new'),
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

    ]
