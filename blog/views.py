from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from blog.models import Blog
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class BlogListView(ListView):
    model = Blog
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        print(request.FILES)

    def get_queryset(self):
        return super().get_queryset().filter(publication_indicator=True)

class BlogAboutView(ListView):
    model = Blog
    template_name = 'about.html'


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_form_article.html'
    fields = ('title_article','content', 'preview', 'created_at', 'publication_indicator', 'number_views')
    success_url = reverse_lazy('blog:blog_start')


class BlogArticleView(DetailView):
    model = Blog
    template_name = 'article.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.number_views += 1
        obj.save()
        return obj

class BlogUpdateArticle(UpdateView):
    model = Blog
    fields = ('title_article','content', 'preview', 'created_at', 'publication_indicator', 'number_views')
    template_name = 'blog_form_article_edit.html'
    success_url = reverse_lazy('blog:blog_start')

class BlogDeleteArticle(DeleteView):
    model = Blog
    template_name = 'blog_form_article_delete.html'
    success_url = reverse_lazy('blog:blog_start')