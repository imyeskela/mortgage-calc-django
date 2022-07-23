from rest_framework import routers

from .views import MortgageViewSet

router = routers.DefaultRouter()
router.register(r'mortgage', MortgageViewSet, basename='mortgage')
