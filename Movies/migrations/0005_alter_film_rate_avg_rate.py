# Generated by Django 4.0.1 on 2022-01-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0004_alter_film_rate_avg_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film_rate',
            name='avg_rate',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
