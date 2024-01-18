from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrAdmin
from .models import ECG, Lead
from .serializers import ECGSerializer, LeadSerializer


class ECGViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    queryset = ECG.objects.all()
    serializer_class = ECGSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
