# The views used below are normally mapped in the AdminSite instance.
# This URLs file is used to provide a reliable view deployment for test purposes.
# It is also provided as a convenience to those who want to deploy these URLs
# elsewhere.

from django.contrib.auth import views
from django.urls import path
from .views import Home, ArticleList, CreateArticle, UpdateArticle, DeleteArticle, PreviewArticle, UpdateProfile, Login
app_name = 'account'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += [
    path('', Home.as_view(), name='home'),
    path('articles/', ArticleList.as_view(), name='list'),
    path('articles/create/', CreateArticle.as_view(), name='create'),
    path('articles/upadte/<int:pk>/', UpdateArticle.as_view(), name='update'),
    path('articles/delete/<int:pk>/', DeleteArticle.as_view(), name='delete'),
    path('articles/preview/<str:slug>/', PreviewArticle.as_view(), name='preview'),
    path('profile/', UpdateProfile.as_view(), name='profile'),
]
