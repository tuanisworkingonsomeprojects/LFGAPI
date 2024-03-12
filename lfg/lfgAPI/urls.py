from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

router.register('api/user', UserDataViewSet, 'user')
router.register('api/session', SessionDataViewSet, 'session')
router.register('api/sessionlist', SessionListViewSet, 'sessionlist')

urlpatterns = router.urls
