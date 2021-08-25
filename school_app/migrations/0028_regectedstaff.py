# Generated by Django 3.2.4 on 2021-08-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0027_auto_20210816_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegectedStaff',
            fields=[
                ('registration_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('last_name', models.CharField(default=None, max_length=50)),
                ('email', models.CharField(default=None, max_length=50)),
                ('contact', models.BigIntegerField(default=None)),
                ('address', models.CharField(default=None, max_length=500)),
                ('dob', models.DateField(default=None)),
                ('user_name', models.CharField(default=None, max_length=50)),
                ('password', models.CharField(default=None, max_length=50)),
                ('profile_pic', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
