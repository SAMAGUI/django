from django.db import models

# Create your models here.

class Category(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return F"{self.label}"


class Customer(models.Model):
    class Meta:
        verbose_name_plural = "Clients"

    email = models.EmailField(verbose_name="Email", null=True, blank=True)
    phone = models.CharField(max_length=50, verbose_name="Téléphone", null=True, blank=True)
    first_name = models.CharField(max_length=150, verbose_name="Prénom(s)")
    last_name = models.CharField(max_length=150, verbose_name="Nom")
    address = models.CharField(max_length=200, verbose_name="Adresse", null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True,
                                  blank=True)
    updated_by = models.CharField(max_length=100, null=True,
                                  blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Item(models.Model):
    """
    ecommerce.Item
    Stores a single item entry for our shop
    """    

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ["id"]

    def __str__(self):
        return self.designation

    designation = models.CharField(max_length=150)
    qty_stock = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    marque = models.CharField(max_length=150)
    code = models.CharField(max_length=150)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    # def amount(self):
    #     # converts price from pence to pounds
    #     amount = float(self.price / 100)
    #     return amount

    def manage_stock(self, qty):
        # used to reduce Item stock
        new_stock = self.qty_stock - int(qty)
        self.qty_stock = new_stock
        self.save()

    def check_stock(self, qty):
        # used to check if order quantity exceeds stock levels
        if int(qty) > self.qty_stock:
            return False
        return True


