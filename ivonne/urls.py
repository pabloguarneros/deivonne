from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, include
from django.conf import settings
from contracts.views import addContract
from users.views import logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('home',include('home.urls')),
    path('api/',include('api.urls')),
    path('c/',include('contracts.urls')),
    path('add/contract',addContract,name="addContract"),
    path('logout', logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls'))
    #path('c/',include('users.urls')),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    