# Generated by Django 2.2 on 2020-09-20 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerManagement', '0008_auto_20200920_1844'),
        ('OrderManagement', '0005_remove_order_bill'),
        ('BillManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CustomerManagement.Customer'),
        ),
        migrations.AddField(
            model_name='bill',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='OrderManagement.Order'),
        ),
    ]
