from django.db import models
from login.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Travel(models.Model):
    destination = models.CharField(max_length=100)
    plan = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="travels")
    joined = models.ManyToManyField(User, related_name="join")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)