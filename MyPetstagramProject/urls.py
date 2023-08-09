from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('MyPetstagramProject.common.urls')),
    path('accounts/', include('MyPetstagramProject.accounts.urls')),
    path('pets/', include('MyPetstagramProject.pets.urls')),
    path('photos/', include('MyPetstagramProject.photos.urls')),
]
