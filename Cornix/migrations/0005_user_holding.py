# Generated by Django 3.2.9 on 2022-03-18 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cornix', '0004_myclient_client_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='holding',
            field=models.BooleanField(default=False),
        ),
    ]
