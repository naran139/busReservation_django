# Generated by Django 3.1.1 on 2023-12-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20231229_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='code',
            field=models.CharField(default=81950, max_length=255, primary_key=True, serialize=False),
        ),
    ]
