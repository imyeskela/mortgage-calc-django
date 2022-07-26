from django.urls import path, include

from .routers import router


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls'))
]