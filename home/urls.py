
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('Serch/Home',views.serindex,name="serindex"),
    path('firstpage',views.firstpage,name="firstpage"),
    path('community',views.community,name="community"),
    path('community/Follow',views.commfoll,name="commfoll"),
    path('Community/Follow',views.sercommf,name="sercommf"),
    path('Community/Serch',views.sercomm,name="sercomm"),
    path('profile',views.profile,name="profile"),
    path('Profile Edit',views.pedit,name="pedit"),
    path('feedprofile/<int:uid>',views.feedprofile,name="feedprofile"),
    path('follow/<int:uid>/', views.follow_toggle, name='follow_toggle'),
    path('blog/<int:bwid>',views.blog,name="blog"),
    path('comment',views.comment,name="comment"),
    path('membership',views.membership,name="membership"),
    path('Payment',views.payment,name="payment"),
    path('writeblog',views.writeblog,name="writeblog"),
    path('register',views.register,name="register"),
    path('login_view',views.login_view,name="login_view"),
    path('logout_view',views.logout_view,name="logout_view"),
    path('like/blog/<int:bwid>/', views.like_blog, name='like_blog'),
    path('like/comment/<int:cid>/', views.like_comment, name='like_comment'),
    path('Save/<int:bwid>/', views.save, name='save'),
    path('Bookmark', views.bookmark, name='bookmark'),
    path('Following', views.ufollowing, name='ufollowing'),
    path('Followers', views.ufollowers, name='ufollowers'),
    path('Followers/<int:uid>', views.followersi, name='followersi'),
    path('Following/<int:uid>', views.followingi, name='followingi'),
    path('About', views.about, name='about'),
    path('Notification', views.notification, name='notification'),
]
