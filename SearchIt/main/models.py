from django.db import models
class Item(models.Model):
    name = models.CharField(max_length=255, null=True, default="",blank=True)
    image = models.ImageField(null=True, blank = True, upload_to='images/')
    about = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
