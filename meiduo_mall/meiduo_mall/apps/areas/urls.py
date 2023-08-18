from django.urls import path
from rest_framework.routers import SimpleRouter
from areas.views import AreaViewSet

urlpatterns = [
]

router = SimpleRouter()
router.register('', AreaViewSet, basename='area')
urlpatterns += router.urls