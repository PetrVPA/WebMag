from django.urls import path
from blog.views import BlogListView, BlogAboutView, BlogCreateView, BlogArticleView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog'


urlpatterns = [
    path('index.html/', BlogListView.as_view(), name='blog_start'),#пути в адресной строке
    path('about.html/', BlogAboutView.as_view(), name='blog_about'),
    path('blog_form_article.html/', BlogCreateView.as_view(), name='blog_create_article'),
    path('<int:pk>.html/', BlogArticleView.as_view(), name='blog_article'),

]
# Добавление статических маршрутов для медиафайлов
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
