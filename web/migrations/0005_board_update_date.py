# Generated by Django 3.2.12 on 2022-03-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_member_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
