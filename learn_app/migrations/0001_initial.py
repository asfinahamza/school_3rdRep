# Generated by Django 3.2.4 on 2021-10-02 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.BigIntegerField()),
                ('dob', models.DateField()),
            ],
        ),
    ]
