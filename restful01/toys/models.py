from django.db import models


class Toy(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    was_included_in_home = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ("name",)
