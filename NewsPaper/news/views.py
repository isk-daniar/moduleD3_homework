from django.views.generic import ListView, DetailView
from .models import Post
 
 
class NewsListView(ListView):
    model = Post 
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation') 


class PostDetailView(DetailView):
    model = Post 
    template_name = 'post.html'
    context_object_name = 'post' 


