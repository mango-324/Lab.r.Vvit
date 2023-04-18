from django.contrib import admin
from articles import views
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('archive/', views.archive),
    re_path(r'^article/(?P<article_id>\d+)$', views.get_article, name='get_article'),
    path('article/new/', views.create_post),
]



