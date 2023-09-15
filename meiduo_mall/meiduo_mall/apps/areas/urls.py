from django.urls import path
from rest_framework.routers import SimpleRouter
from areas.views import *

urlpatterns = [
    path('areas/', ListAreaView.as_view()),
    path('areas/<int:id>/', SubsAreaView.as_view())
]

# router = SimpleRouter()
# router.register('', AreaViewSet, basename='area')
# urlpatterns += router.urls