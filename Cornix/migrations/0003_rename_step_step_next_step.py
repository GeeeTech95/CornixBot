# Generated by Django 3.2.9 on 2022-03-17 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cornix', '0002_myclient_myorder_step'),
    ]

    operations = [
        migrations.RenameField(
            model_name='step',
            old_name='step',
            new_name='next_step',
        ),
    ]
