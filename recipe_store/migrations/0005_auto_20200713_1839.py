# Generated by Django 3.0.6 on 2020-07-13 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_store', '0004_auto_20200713_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='abbreviation',
            field=models.CharField(max_length=5),
        ),
    ]
