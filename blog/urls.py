from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
#from django.conf.urls.static import static
#from django.conf import settings
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    # url(r'^post/image/$', views.upload, name='upload'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup_ok/$', TemplateView.as_view(
        template_name='blog/signup_ok.html'), name='signup_ok'
    ),
    url(r'^login/$', views.user_login, name='login_url'),
    url(r'^logout/$', views.user_logout, name='logout_url'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
