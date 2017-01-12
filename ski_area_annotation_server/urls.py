from django.conf.urls import url, include
from skareas import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('skareas.urls'))
]
