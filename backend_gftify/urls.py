from django.urls import include, path
from rest_framework import routers
import product.views as test 

router = routers.DefaultRouter()


urlpatterns = [
    path('', include('users.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
     path('api/products/', test.liste_products),
    path('api/products/<int:pk>/', test.detail_products),
]
