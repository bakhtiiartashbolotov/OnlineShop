# Generated by Django 4.2.7 on 2023-11-29 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshopapp', '0002_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=16),
        ),
    ]