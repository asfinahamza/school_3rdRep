# Generated by Django 3.2.4 on 2021-10-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0043_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='status',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]