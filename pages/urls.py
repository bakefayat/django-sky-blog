from django.urls import path
from .views import PageDetailView

app_name = "pages"

urlpatterns = [
    path("<str:slug>/", PageDetailView.as_view(), name="page_detail"),
]
