# Generated by Django 5.0.2 on 2024-03-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(default='added', max_length=100),
        ),
    ]
