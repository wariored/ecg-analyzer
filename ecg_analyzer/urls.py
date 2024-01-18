from django.contrib import admin
from django.urls import path, include
from .views import ECGViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"ecgs", ECGViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls))
]
