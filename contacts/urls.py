from django.urls import path
from contacts import views

urlpatterns = [
    path('usergrid',views.UserGridView.as_view(),name='contacts-usergrid'),
    path('userlist',views.UserListView.as_view(),name='contacts-userlist'),
    path('profile',views.ProfileView.as_view(),name='contacts-profile'),
]