from django.contrib import admin
from django.urls import path, include
from api.api.router import router_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_post.urls))
]
