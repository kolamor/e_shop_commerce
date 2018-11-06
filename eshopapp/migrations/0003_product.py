# Generated by Django 2.1.2 on 2018-11-06 15:08

from django.db import migrations, models
import django.db.models.deletion
import eshopapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshopapp', '0002_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('image', models.ImageField(blank=True, upload_to=eshopapp.models.generate_filename)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('available', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eshopapp.Brand', verbose_name='Бренд')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eshopapp.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]