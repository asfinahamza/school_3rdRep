# Generated by Django 3.2.4 on 2021-07-03 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0008_classes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=50)),
            ],
        ),
    ]
