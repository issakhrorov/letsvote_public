# Generated by Django 4.1 on 2022-11-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_vote_votes_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='element_id',
            field=models.CharField(max_length=100),
        ),
    ]