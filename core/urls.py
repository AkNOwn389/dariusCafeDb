from django.contrib import admin
from django.urls import path
from feeds.views import feedback_api, get_user_feedback
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('feedback/', feedback_api),
    path('get-feedback/', get_user_feedback),
    path('', admin.site.urls),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

