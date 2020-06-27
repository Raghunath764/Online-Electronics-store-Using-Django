# Generated by Django 3.0.7 on 2020-06-18 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminModule', '0003_auto_20200610_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.FloatField(default=200)),
                ('quantity', models.FloatField(default=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminModule.Category')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminModule.Product')),
            ],
            options={
                'db_table': 'Cart',
            },
        ),
    ]
