# Generated by Django 3.0.2 on 2020-02-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crate',
            name='country',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='crate',
            name='year',
            field=models.IntegerField(default=2020, verbose_name='year'),
        ),
    ]
