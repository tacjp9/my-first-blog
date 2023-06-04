from django.urls import path
from . import views
app_name = 'blog' #名前空間の設定

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
]