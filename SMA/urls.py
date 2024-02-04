
#NOTE - <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ROOOT URLS FILES>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


from django.contrib import admin
from django.urls import path,include    

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('auth_app.urls')),
    path('',include('core.urls')),
    path('',include('user.urls')),
    
]


#NOTE - extends the media urls and media files

urlpatterns.extend(
    
    static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
)