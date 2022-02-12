from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('despegar.urls', 'despegar')),
    path('', include('login.urls')),
    path('docs/',include_docs_urls(title="BlogAPI",public=False)),
    path('schema', get_schema_view(
        title="Despegar API",
        description="API for Despegar",
        version="1.0.0"
    ), name='openapi-schema'),
]
