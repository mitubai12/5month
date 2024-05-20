from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        db_table = 'category'
        ordering = ['name']


class Product(models.Model):
    title = models.CharField(max_length=85)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        db_table = 'product'
        ordering = ['title']


class Review(models.Model):
    text = models.CharField(max_length=155)
    stars = models.IntegerField(
        choices=[
            (1, '1 Star'),
            (2, '2 Stars'),
            (3, '3 Stars'),
            (4, '4 Stars'),
            (5, '5 Stars')
        ],
        default=5
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text}"
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        db_table = 'review'
        ordering = ['text']
