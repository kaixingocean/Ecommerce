# Generated by Django 2.1 on 2019-03-21 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='Quantity',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='emailAddress',
            field=models.EmailField(blank=True, max_length=250, verbose_name='Email Address'),
        ),
    ]
