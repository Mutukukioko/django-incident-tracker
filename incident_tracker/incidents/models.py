from django.db import models

class Incident(models.Model):
    INCIDENT_TYPES = [
        ('security_breach', 'Security Breach'),
        ('data_loss', 'Data Loss'),
        ('malware_attack', 'Malware Attack'),
        # Add more incident types as needed
    ]

    type = models.CharField(max_length=20, choices=INCIDENT_TYPES)
    description = models.TextField()
    status = models.CharField(max_length=20, default='open')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_type_display()} - {self.timestamp}"
