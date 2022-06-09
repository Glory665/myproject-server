from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='имя продукт', max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    description = models.CharField(verbose_name='описание', max_length=256)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True).order_by('category', 'name')



