# Generated by Django 4.2.7 on 2023-11-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshopapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/'),
        ),
    ]