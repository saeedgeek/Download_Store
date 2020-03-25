# Generated by Django 3.0.4 on 2020-03-25 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_store_admin'),
        ('production', '0003_auto_20200325_0057'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='_file',
            field=models.ManyToManyField(blank=True, null=True, to='production.File'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='production.Product'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='store',
            field=models.ManyToManyField(blank=True, null=True, through='user.StoreCustomer', to='store.Store'),
        ),
    ]
