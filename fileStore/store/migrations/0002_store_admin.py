# Generated by Django 3.0.4 on 2020-03-25 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Admin'),
        ),
    ]