from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('despegar.urls', 'despegar')),
    path('api/', include('login.urls')),
    #path('api/login/', include('login.urls'))
]
