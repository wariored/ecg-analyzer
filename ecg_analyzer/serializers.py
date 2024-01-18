from rest_framework import serializers
from .models import ECG, Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ["name", "number_of_samples", "signal"]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["signal"] = instance.get_signal()  # Deserialize signal for API response
        return ret


class ECGSerializer(serializers.ModelSerializer):
    leads = LeadSerializer(many=True, read_only=True)

    class Meta:
        model = ECG
        fields = ["id", "date", "leads"]
