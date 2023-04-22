from django.urls import path
from .views import NewsListView, PostDetailView
 
 
urlpatterns = [
    path('', NewsListView.as_view(), name='post_list'),  
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
]