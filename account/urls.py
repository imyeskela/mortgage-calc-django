from django.urls import path, include

from . import views

urlpatterns = [
    path('<user_id>/', views.UserApiView.as_view()),
    path('registration/', views.RegistrationApiView.as_view()),
    path('auth/', include('rest_framework.urls'))
    # path('login/', ),
    # path('logout/', )
]