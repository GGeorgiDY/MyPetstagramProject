from django.urls import path
from MyPetstagramProject.common.views import index

urlpatterns = (
    path('', index, name='index'),
)
