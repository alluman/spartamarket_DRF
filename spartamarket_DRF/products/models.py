from django.db import models

class Hashtag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    view = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField()
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    like_user = models.ManyToManyField('accounts.User', related_name='like_products', default=0)
    hashtags = models.ManyToManyField(Hashtag, related_name='products')
    image = models.ImageField(upload_to='images/', blank=True)
    
    def __str__(self):
        return self.title