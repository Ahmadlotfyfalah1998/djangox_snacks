from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
# Create your models here.

class Snack(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    
    purcheser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('snack_list')