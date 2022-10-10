from django.urls import path
from blog import views

urlpatterns = [
    path('bloglist',views.BlogListView.as_view(),name='blog-bloglist'),
    path('bloggrid',views.BlogGridView.as_view(),name='blog-bloggrid'),
    path('blogdetails',views.BlogDetailsView.as_view(),name='blog-blogdetails'),
]