from django.db import models

# Create your models here.
class Order_item(models.Model):
    id = models.AutoField(primary_key=True)
    product= models.CharField(max_length=50)
    name= models.CharField(max_length=50)
    order= models.CharField(max_length=50)
    quantity= models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_file= models.ImageField(upload_to = 'uploads/', null = False) 

    def __str__(self):
        return self.product
        
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user= models.CharField(max_length=50)
    product= models.CharField(max_length=50)
    payment_method=models.CharField(max_length=50)
    is_Paid= models.BooleanField(db_index=True, default=False)
    is_Delivered= models.BooleanField(db_index=True, default=False)
    created_at = models.DateTimeField(auto_now=True)
    Paid_at = models.DateTimeField(auto_now=True)
    Delivered_at = models.DateTimeField(auto_now=True)
    Total_price= models.DecimalField(max_digits=10, decimal_places=2)
    Shipping_price=  models.DecimalField(max_digits=10, decimal_places=2)
   

    def __str__(self):
        return self.product

class Product_Category(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


    class Meta:
        verbose_name ='Product Category'
        verbose_name_plural ='Product Categories'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    user= models.CharField(max_length=50)
    name= models.CharField(max_length=50)
    image_file= models.ImageField(upload_to = 'uploads/', null = False) 
    brand= models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    description= models.TextField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Product_Category, on_delete= models.CASCADE)
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    countInStock = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Shipping(models.Model):
    id = models.AutoField(primary_key=True)
    order= models.CharField(max_length=50)
    address= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    Shipping_price = models.DecimalField(max_digits=10, decimal_places=2)
    Post_code = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order
