# Generated by Django 5.2.1 on 2025-05-14 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('student_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('student_roll', models.IntegerField()),
            ],
        ),
    ]
