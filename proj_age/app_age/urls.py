from django.conf.urls import url, include
from app_age import views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'agendamento', views.AgendamentoViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^docs/', include_docs_urls(title='API REST para o sistema de agendamento')),
    url(r'^', include(router.urls)),
]
