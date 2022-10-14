from django.db import models

# Create your models here.
class Register(models.Model):
    user_name = models.CharField(max_length=60)
    user_email = models.EmailField()
    user_address = models.CharField(max_length=200)
    user_contact = models.CharField(max_length=15)
    Password = models.CharField(max_length=100)
    c_Password = models.CharField(max_length=100)

    class Meta:
        db_table='Register'
class Product(models.Model):
    pname=models.CharField(max_length=30)
    psize=models.CharField(max_length=10)
    pcolor=models.CharField(max_length=20)
    pdetail=models.CharField(max_length=200)
    pimage = models.ImageField(upload_to='upload')

    class Meta:
        db_table='Product'



