from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    # Social Media Platform
    social_media_platform = models.CharField(max_length=50)
    # Social Media Handle
    social_media_handle = models.CharField(max_length=150)
    # Category
    category = models.CharField(max_length=30)
    # Description
    description = models.TextField()
    # Created At
    created_at =  models.DateTimeField(auto_now_add=True)
    # Reported By
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
