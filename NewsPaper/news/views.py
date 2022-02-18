from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class PostList(ListView):
    model = Post
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # добавим переменную текущей даты time_now
        context['time_now'] = datetime.utcnow()
        # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['value1'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post_list.html'
    context_object_name = 'post'