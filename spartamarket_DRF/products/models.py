from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    view = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField()
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)