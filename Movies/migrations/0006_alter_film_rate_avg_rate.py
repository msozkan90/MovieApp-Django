# Generated by Django 4.0.1 on 2022-01-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0005_alter_film_rate_avg_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film_rate',
            name='avg_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
