# Generated by Django 3.2.7 on 2022-02-10 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiAPP', '0002_product_user_profile_user_wishlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_profile',
        ),
        migrations.RemoveField(
            model_name='user_wishlist',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='user_wishlist',
            name='user',
        ),
        migrations.DeleteModel(
            name='product',
        ),
        migrations.DeleteModel(
            name='user_wishlist',
        ),
    ]