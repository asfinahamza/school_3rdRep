# Generated by Django 3.2.4 on 2021-07-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0013_rename_addclasses_addedclasses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_id', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('contact', models.BigIntegerField()),
            ],
        ),
    ]