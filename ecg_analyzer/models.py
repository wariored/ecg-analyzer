from django.db import models


class ECG(models.Model):
    date = models.DateTimeField(auto_now_add=True)


class Lead(models.Model):
    ecg = models.ForeignKey(ECG, related_name="leads", on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    number_of_samples = models.IntegerField(null=True, blank=True)
    signal = models.TextField()

    def get_signal(self):
        return str(self.signal).split()

    def set_signal(self, signal_list):
        self.signal = signal_list.join("")

    def save(self, *args, **kwargs):
        if isinstance(self.signal, list):
            self.set_signal(self.signal)
        super().save(*args, **kwargs)