
from rest_framework.routers import DefaultRouter
from toys.views import ToysViewSet

router = DefaultRouter()

router.register(r'toys', ToysViewSet)

toys_urls = router.urls