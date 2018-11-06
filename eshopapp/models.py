from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.
User = get_user_model()


def  generate_filename(instance, filename):
	 filename = instance.slug +'.'+ filename.split('.')[1]
	 return "{0}/{1}".format(instance, filename)


class Category(models.Model):
	""" Category model"""
	title = models.CharField('название', max_length=40)
	slug = models.SlugField('slug', max_length=40, unique=True)
	image = models.ImageField(upload_to=generate_filename, blank=True)

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


	def __str__(self):
		return self.title

class Brand(models.Model):
	"""Brand category"""
	title = models.CharField('название', max_length=40)
	slug = models.SlugField('slug', max_length=40, unique=True)
	image = models.ImageField(upload_to=generate_filename, blank=True)

	class Meta:
		verbose_name = 'Бренд'
		verbose_name_plural = 'Бренды'


	def __str__(self):
		return self.title


class Product(models.Model):
	"""Product models"""
	title = models.CharField('название', max_length=50)
	slug = models.SlugField('slug', max_length=50, unique=True)
	category = models.ForeignKey(
					Category,
					verbose_name='Категория',
					on_delete=models.SET_NULL,
					null=True)
	brand = models.ForeignKey(
					Brand,
					verbose_name='Бренд',
					on_delete=models.SET_NULL,
					null=True)
	description = models.TextField('Описание товара')
	image = models.ImageField(upload_to=generate_filename, blank=True)
	price = models.DecimalField(max_digits=11, decimal_places=2)
	available = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'


	def __str__(self):
		return self.title