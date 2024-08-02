from django.db import models


class Toy(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=250, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    category = models.CharField(max_length=50, blank=False)
    was_included_in_home = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
