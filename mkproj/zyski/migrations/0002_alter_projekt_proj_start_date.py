# Generated by Django 4.1.7 on 2023-04-29 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zyski', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projekt',
            name='proj_start_date',
            field=models.DateField(auto_now_add=True, verbose_name='Data utworzenia projektu.'),
        ),
    ]
