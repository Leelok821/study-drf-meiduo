from django.urls import path
from rest_framework.routers import SimpleRouter
from areas.views import ListSubsAreaViewSet

urlpatterns = [
    # path('areas/', ListSubsAreaViewSet.as_view({'get':'list'})),
    # path('areas/<int:id>/', ListSubsAreaViewSet.as_view({'get':'retrieve'}))
]

router = SimpleRouter()
router.register('areas', ListSubsAreaViewSet, basename='')
urlpatterns += router.urls