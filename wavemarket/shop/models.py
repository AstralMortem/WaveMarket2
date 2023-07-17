from django.db import models

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ('-created_at', '-updated_at')



class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name


class AudioFragments(models.Model):
    name = models.CharField(max_length=250)
    audio_file = models.FileField(upload_to='audio_fragments')
    
    def __str__(self):
        return self.name


class Item(Base):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    audio = models.ManyToManyField(AudioFragments)


    def __str__(self):
        return self.name
    
    def get_price(self):
        if self.discount_price:
            return self.discount_price
        return self.price




class Order(Base):
    items = models.ManyToManyField(Item)
    is_payed = models.BooleanField(default=False)
    ordered_date = models.DateField(null=True, blank=True)
    address = models.ForeignKey('account.Address', on_delete=models.RESTRICT)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    
    def get_items_count(self):
        return self.items.count()
    
    def get_total_items_price(self):
        total = 0
        for item in self.items.all():
            total += item.get_price()
        return total
    
    def get_total(self):
        total = self.get_total_items_price()
        if self.coupon:
            total -= (self.coupon.discount*total)/100
        if self.user.discount > 0:
            total -= (self.user.discount*total)/100
        return total
    
    def __str__(self):
        return f"Order #{self.order.id} by {self.user.username} ({self.get_items_count} items on {self.get_total} UAH)"
            




class Coupon(Base):
    code = models.CharField(max_length=255)
    discount = models.IntegerField(default=5)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code + f"(-{self.discount}%)"