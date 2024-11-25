from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("frontend.urls")),  # Include the app's URLs
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
