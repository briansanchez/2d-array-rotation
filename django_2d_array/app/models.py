from django.db import models

class Visit(models.Model):
    ip_address              = models.CharField(null = True, max_length = 255)
    grid                    = models.TextField(null = True)
    cols                    = models.IntegerField(null=True)
    rows                    = models.IntegerField(null=True)
    rotation                = models.IntegerField(null=True)

    created_at              = models.DateTimeField(auto_now_add = True, null=True)
    updated_at              = models.DateTimeField(auto_now = True, null=True)