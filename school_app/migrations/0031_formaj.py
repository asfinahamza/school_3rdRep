# Generated by Django 3.2.4 on 2021-08-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0030_classteacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormAj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
            ],
        ),
    ]
