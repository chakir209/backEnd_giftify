# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet

# router = DefaultRouter()
# router.register(r'users', UserViewSet)

# urlpatterns = router.urls

from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserViewSet.as_view({'get': 'list'})),
    path('<int:pk>',
         views.UserViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
    path('public', views.public),
    path('private', views.private),
    path('private-scoped', views.private_scoped),
]
