from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, WordViewSet

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', WordViewSet, base_name='words')

urlpatterns = router.urls