from django.contrib import admin
from django.urls import path, include
from teacher.views import *
from django.conf.urls.static import static
from markbookcrm import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teacher.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound