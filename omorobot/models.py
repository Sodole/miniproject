from django.db import models

# Create your models here.
# User
class User(models.Model):
  user_name = models.CharField(max_length=20, primary_key=True, null=False)
  model_name = models.CharField(max_length=20)
  user_password = models.CharField(max_length=20, null=False)
  
  def __str__(self):
   return self.user_name

  def get_delete_url(self) :
    return f"deleteuser/{self.pk}/"
  
  def get_update_url(self) :
    return f"updatemyuser/{self.pk}/"



class Model(models.Model):
  model_name = models.CharField(max_length=20, null=False,  default="r1")
  model_size = models.TextField(max_length=200, null=False)
  model_battery =  models.IntegerField(default=0, null=True)
  model_weight = models.IntegerField(default=0, null=True)
  model_firmware = models.CharField(max_length=200, null=True)

  def __str__(self):
    return self.model_name


class Mycar(models.Model):
  mycar_speed = models.IntegerField(default=0, null=True)
  mycar_battery = models.IntegerField(default=0, null=True)
  mycar_color = models.TextField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user_name = models.ForeignKey("User", on_delete=models.CASCADE, db_column='user_name')

  def get_delete_url(self) :
    return f"deletemycar/{self.pk}/"
  
  def get_update_url(self) :
    return f"updatemycar/{self.pk}/"