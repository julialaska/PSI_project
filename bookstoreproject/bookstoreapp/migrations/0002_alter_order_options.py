# Generated by Django 4.1.2 on 2022-11-21 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('client',)},
        ),
    ]