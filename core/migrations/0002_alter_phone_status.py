# Generated by Django 5.1.2 on 2024-10-22 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='status',
            field=models.CharField(choices=[('E', 'Exist'), ('N', 'NotExist')], default='E', max_length=10),
        ),
    ]