from django.urls import path, include

from rest_framework.routers import DefaultRouter
from barecode import views


router = DefaultRouter()
router.register('barcode',views.BarcodeViewSet,base_name='barcode')


urlpatterns = [
    path('',include(router.urls)),
]
