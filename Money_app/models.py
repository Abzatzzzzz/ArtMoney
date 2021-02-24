from django.db import models
from django.urls import reverse


class Expenses(models.Model):
    money = models.FloatField(verbose_name='How much am I spending?')
    category = models.ForeignKey('Category', related_name='expenses', on_delete=models.PROTECT)
    month = models.ForeignKey('Month', on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Added')

    def __str__(self):
        return f'Потрачено :{str(self.money)} UAN'

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
        ordering = ['-created_at']


class TranshMvf(models.Model):
    money = models.FloatField(verbose_name='How much I got?')
    category = models.ForeignKey('Category', related_name='Source_type', on_delete=models.PROTECT)
    month = models.ForeignKey('Month', on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Added')

    def __str__(self):
        return f'Получено :{str(self.money)} UAN'

    class Meta:
        verbose_name = 'Income'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self): # встроенная в джанго функция, позволяет сформировать url - category/i_tyt_slug_bydet
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Month(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='url', unique=True)
    year = models.ForeignKey('Year', verbose_name='Year', on_delete=models.PROTECT, related_name='year')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Added')

    def get_absolute_url(self):
        return reverse('month', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Month'


class Year(models.Model):
    title = models.CharField(max_length=50)
    month = models.ManyToManyField(Month, verbose_name='month', related_name='month', blank=True)
    slug = models.SlugField(max_length=50, unique=True, verbose_name='url')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Added')

    def get_absolute_url(self):
        return reverse('year', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Year'
