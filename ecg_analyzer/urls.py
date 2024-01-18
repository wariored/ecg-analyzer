from django.contrib import admin
from django.urls import path
from .views import ECGViewSet, LeadViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"ecgs", ECGViewSet)
router.register(r"leads", LeadViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
]
