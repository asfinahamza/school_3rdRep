# Generated by Django 3.2.4 on 2021-06-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0004_alter_registration_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffregistration',
            name='contact',
            field=models.BigIntegerField(),
        ),
    ]
