# Generated by Django 4.1 on 2022-11-08 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_promotion_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='promotion',
            field=models.BinaryField(default=True),
        ),
    ]