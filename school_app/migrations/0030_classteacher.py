# Generated by Django 3.2.4 on 2021-08-18 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0029_declinedstudentdetails_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.addedclasses')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.staff')),
            ],
        ),
    ]
