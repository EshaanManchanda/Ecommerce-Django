# Generated by Django 4.1.7 on 2023-04-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_alter_item_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='img/image_not_available.png', upload_to='Porduct'),
        ),
    ]
