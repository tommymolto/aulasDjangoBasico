
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('enquetes/', include('enquete.urls')),
    path('admin/', admin.site.urls),
]