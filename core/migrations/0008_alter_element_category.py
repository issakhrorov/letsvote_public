# Generated by Django 4.1 on 2022-11-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_element_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]
