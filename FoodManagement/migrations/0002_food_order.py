# Generated by Django 2.2 on 2020-09-20 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrderManagement', '0001_initial'),
        ('FoodManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='OrderManagement.Order'),
        ),
    ]
