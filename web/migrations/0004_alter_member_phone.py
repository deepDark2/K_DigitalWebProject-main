# Generated by Django 3.2.12 on 2022-03-09 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20220309_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
