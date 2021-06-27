from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, include
from django.conf import settings
from contracts.views import addContract


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('api/',include('api.urls')),
    path('c/',include('contracts.urls')),
    path('add/contract',addContract)
    #path('c/',include('users.urls')),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    