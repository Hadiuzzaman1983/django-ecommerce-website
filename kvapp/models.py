from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    joined_on=models.DateField(auto_now=True)


    def __str__(self):
        return self.full_name

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    salling_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    warranty= models.CharField(max_length=100)
    return_policy = models.CharField(max_length=100)
    view_count = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Cart(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True, null=True)
    total= models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart :"+str(self.id)

class CartProduct(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal=models.PositiveIntegerField()

    def __str__(self):
        return "Cart: "+str(self.cart.id)+ "CartProduct: "+str(self.id)

ORDER_STATUS = (
    ("Order Received","Order Received"),
    ("Order Processing","Order Processing"),
    ("One th Way","One th Way"),
    ("Order Canceled","Order Canceled"),

)

class Order(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    ordered_by=models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=200)
    mobile=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,null=True,blank=True)
    subtotal=models.PositiveIntegerField()
    discount=models.PositiveIntegerField()
    ordered_status=models.CharField(max_length=100,choices=ORDER_STATUS)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order: "+str(self.id)









