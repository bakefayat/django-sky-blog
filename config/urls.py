from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
from accounts.views import Login, RegisterPendingView, RegisterCompleteView
from accounts.views import RegisterCreateView, activate

handler500 = 'exception_handling.views.handler500'
handler404 = 'exception_handling.views.handler404'

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("register/", RegisterCreateView.as_view(), name="register"),
    path("register/pending/", RegisterPendingView.as_view(), name="register-pending"),
    path("register/complete/", RegisterCompleteView.as_view(), name="register-complete"),
    path("activate/<str:uidb64>/<str:token>/", activate, name="activate"),
    path("accounts/", include("accounts.urls"), name="home"),
    path("admin/doc/", include("django.contrib.admindocs.urls"), name="admin_doc"),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/", include("api.urls"), name="api"),
    path("pages/", include("pages.urls"), name="pages"),
    path("", include("django.contrib.auth.urls")),
    path("", include("blog.urls")),
    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
