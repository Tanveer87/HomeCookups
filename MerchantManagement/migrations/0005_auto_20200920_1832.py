# Generated by Django 2.2 on 2020-09-20 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MerchantManagement', '0004_merchant_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='Phone_Number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='FoodManagement.Food'),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='OrderManagement.Order'),
        ),
    ]
