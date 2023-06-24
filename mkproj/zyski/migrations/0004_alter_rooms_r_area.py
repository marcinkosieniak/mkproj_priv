# Generated by Django 4.1.7 on 2023-05-03 16:50

from django.db import migrations, models
import zyski.models


class Migration(migrations.Migration):

    dependencies = [
        ('zyski', '0003_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='r_area',
            field=models.DecimalField(decimal_places=2, help_text='Powierzchnia w m2', max_digits=5, validators=[zyski.models.validate_positive]),
        ),
    ]
