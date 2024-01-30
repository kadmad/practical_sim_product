from django.db import models
from base.models import BaseModel


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25, null=False)

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0.0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
