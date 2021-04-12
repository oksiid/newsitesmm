from django.contrib import admin
from django.urls import path
from marketing import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('office/', views.office, name='office'),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
