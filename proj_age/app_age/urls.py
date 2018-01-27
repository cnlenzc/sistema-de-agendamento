from django.conf.urls import url, include
from app_age import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'agendamento', views.AgendamentoViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
]
