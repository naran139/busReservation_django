# Generated by Django 3.1.1 on 2023-12-25 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20231224_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='code',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]