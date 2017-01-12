from rest_framework.routers import DefaultRouter

import django.conf.urls as dcu
import skareas.views as sv

router = DefaultRouter()
router.register(r'skiareas', sv.SkiAreaViewSet)
#router.register(r'users', sv.UserViewSet)

urlpatterns = [
    dcu.url(r'^', dcu.include(router.urls)),
]
