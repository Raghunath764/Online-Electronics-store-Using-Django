# Generated by Django 3.0.7 on 2020-06-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminModule', '0007_auto_20200618_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='category',
            field=models.CharField(max_length=40),
        ),
    ]
