# Generated by Django 4.1.7 on 2023-04-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projekt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nazwa projektu', max_length=90)),
                ('proj_start_date', models.DateField(verbose_name='Data utworzenia projektu.')),
                ('number', models.CharField(max_length=20, verbose_name='Numer projektu.')),
                ('description', models.CharField(help_text='Opis projektu', max_length=250)),
            ],
        ),
    ]
