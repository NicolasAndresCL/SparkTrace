from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView
)
from django.shortcuts import render

def custom_swagger_ui_view(request):
    return render(request, "swagger/custom_swagger.html")

urlpatterns = [
    # 🛠️ Administración
    path('admin/', admin.site.urls),

    # 🏠 Vista principal
    path('', custom_swagger_ui_view, name='home_swagger-ui'),


    path('api/productos/', include('productos.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', custom_swagger_ui_view, name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
