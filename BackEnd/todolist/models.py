from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class nguoi_dung(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class to_do_list(models.Model):
    name = models.CharField(max_length=50)
    date_create = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    user = models.ForeignKey(nguoi_dung, on_delete=models.CASCADE)

class item(models.Model):
    name = models.CharField(max_length=250)
    to_do = models.ForeignKey(to_do_list, on_delete=models.CASCADE,related_name='todoitem')

class to_do_share(models.Model):
    to_do = models.ForeignKey(to_do_list, on_delete=models.CASCADE,related_name='todoshare_todo')
    user = models.ForeignKey(nguoi_dung, on_delete=models.CASCADE,related_name='todoshare_user')