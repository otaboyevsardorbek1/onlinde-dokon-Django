# Generated by Django 4.0.5 on 2022-08-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_address_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
