# Generated by Django 3.2.4 on 2021-08-11 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0022_studentregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddedSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.addedclasses')),
            ],
        ),
    ]
