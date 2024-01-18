from rest_framework import viewsets

from .permissions import IsOwnerOrAdmin
from .models import ECG, Lead
from .serializers import ECGSerializer, LeadSerializer


class ECGViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrAdmin]
    queryset = ECG.objects.all()
    serializer_class = ECGSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
