# Generated by Django 3.2.4 on 2021-06-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0005_alter_staffregistration_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('contact', models.BigIntegerField()),
            ],
        ),
    ]
