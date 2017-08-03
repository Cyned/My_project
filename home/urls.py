from django.conf.urls import url

from . import views

app_name = 'home'

urlpatterns = [
    # /
    url(r'^$', views.Home.as_view(), name='home'),

    # /log_in
    url(r'^login$', views.Log_in.as_view(), name='login'),

    # /log_out
    url(r'^logout$', views.Log_out.as_view(), name='logout'),

    # /log_up
    url(r'^log_up$', views.Log_up.as_view(), name='log_up'),

    # /user/<user_id>/
    url(r'^user/(?P<pk>[0-9]+)$', views.DetailUser.as_view(), name='detail_user'),

    # /create_post/
    url(r'^create_post$', views.Create_post.as_view(), name='create_post'),
]
