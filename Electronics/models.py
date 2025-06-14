from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    image=models.ImageField(upload_to='post_images/',null=True,blank=True)

    def __str__(self):
        return self.name
    