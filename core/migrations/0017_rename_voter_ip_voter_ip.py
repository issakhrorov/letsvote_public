# Generated by Django 4.1 on 2022-11-21 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_vote_element_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voter',
            old_name='voter_ip',
            new_name='ip',
        ),
    ]
