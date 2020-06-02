from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
User = get_user_model()
# Create your models here.
class Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    class Meta:
        unique_together = [('user', 'name')]
    
    def __str__(self):
        return "{}".format(self.name)

class Contact(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    birthdate = models.DateField(null=True, default=None)
    phone = models.CharField(max_length=10)
    email = models.CharField(null=True, default=None ,max_length=30)
    url = models.CharField(null=True, default=None ,max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        unique_together = [('phone', 'group')]
    
    
