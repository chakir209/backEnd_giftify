# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet

# router = DefaultRouter()
# router.register(r'users', UserViewSet)

# urlpatterns = router.urls

from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.UserViewSet.as_view({'get': 'list'})),
    path('api/<int:pk>',
         views.UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})),
    path('api/public', views.public),
    path('api/private', views.private),
    path('api/private-scoped', views.private_scoped),
]
