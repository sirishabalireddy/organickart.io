from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('food_carts:product_list_by_category', args=[
            self.slug
        ])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return  reverse('food_carts:product_detail', args=[
            self.id,
            self.slug
        ])



'''
class Product(models.Model):
    CATEGORY = (
        ('DR', 'Drinks'),
        ('FF', 'Fast Foods'),
        ('SN', 'Snacks'),
        ('SD', 'Salads')
    )

    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100)
    p_price = models.IntegerField()
    p_description = models.TextField()
    p_pics = models.CharField(max_length=250)
    p_category = models.CharField(max_length=4, choices=CATEGORY)
    slug = model

class User(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)


class Inventiory(models.Model):
    p_id = models.OneToOneField(Product)
    amount_in_stock = models.IntegerField()

class Sales(models.Model):

    MOP = (
        ('CC', 'Credit Card'),
        ('DC', 'Debit Card'),
        ('MP', 'M-Pesa')
    )

    CH = (
        ('TR', 'True'),
        ('FL', 'False')
    )

    p_id = models.ManyToManyField(Product)
    user_id = models.ManyToManyField(User)
    no_bought = models.IntegerField()
    amount_paid = models.IntegerField()
    means_of_payment = models.CharField(max_length=10, choices=MOP)
    location = models.CharField(max_length=100)
    deliverd = models.CharField(max_length=2, choices=CH)

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    p_id = models.OneToOneField(Product)
    amount = models.IntegerField()
'''

