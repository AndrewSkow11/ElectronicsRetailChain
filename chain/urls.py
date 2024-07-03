from chain.views import LinkOfChainViewSet, ProductViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register('main', LinkOfChainViewSet)
router.register('product', ProductViewSet)


urlpatterns = []
urlpatterns += router.urls
