# Generated by Django 3.2.4 on 2021-10-04 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0050_auto_20211002_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='classes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.addedclasses'),
        ),
    ]
