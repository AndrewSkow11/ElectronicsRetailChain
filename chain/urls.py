from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chain.views import LinkOfChainViewSet

router = DefaultRouter()
router.register(r'', LinkOfChainViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
