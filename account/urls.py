from django.urls import path, include

from . import views

urlpatterns = [
    # path('', ),
    path('registration/', views.RegistrationApiView.as_view()),
    path('auth/', include('rest_framework.urls'))
    # path('login/', ),
    # path('logout/', )
]