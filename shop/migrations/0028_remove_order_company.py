# Generated by Django 4.1.7 on 2023-04-02 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_remove_orderitem_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='company',
        ),
    ]
