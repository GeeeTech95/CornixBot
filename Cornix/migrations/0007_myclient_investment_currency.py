# Generated by Django 3.2.9 on 2022-04-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cornix', '0006_alter_myorder_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='myclient',
            name='investment_currency',
            field=models.CharField(default='USDT', max_length=20),
        ),
    ]