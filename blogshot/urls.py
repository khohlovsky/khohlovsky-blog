from django.conf.urls import include, patterns, url
from blogshot import views
from models import Post, IptablePost,IptableComment

urlpatterns=patterns('',
url(r'^save/comment/$',views.comment_save,),
url(r'^save/post_rating$',views.save,{'model':IptablePost}),
url(r'^save/comment_rating$',views.save,{'model':IptableComment}),
url(r'^get/comment/$',views.get_comment,),
url(r'^/?(category/(?P<slug>[0-9A-Za-z-]+))/$',views.lists,{'url':'category'}),
url(r'^/?(tag/(?P<slug>[0-9A-Za-z-]+))/?$',views.lists,{'url':'tag'}),
url(r'^/?$',views.lists,{'url':'main','slug':None}),
url(r'^(?P<slug>[0-9A-Za-z-]+)/?$',views.post),
)
