
from django.contrib import admin
from django.urls import path, include

from dzDjango import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.koko),
    #path('revers/', views.revers),
    path('koko/', views.koko),
]
