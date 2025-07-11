# Generated by Django 5.2.1 on 2025-06-14 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0017_category_products_is_top_deal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('emp_first_name', models.CharField(max_length=100)),
                ('emp_last_name', models.CharField(max_length=100)),
                ('emp_city', models.CharField(max_length=100)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
