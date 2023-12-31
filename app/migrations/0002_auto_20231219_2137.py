# Generated by Django 3.1.1 on 2023-12-19 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='reservation',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='bus_schedule',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
        migrations.RenameField(
            model_name='bus',
            old_name='fare',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='arrival_location',
        ),
        migrations.AlterField(
            model_name='bus',
            name='departure_location',
            field=models.CharField(choices=[('Bharatpur', 'Bharatpur'), ('Kathmandu', 'Kathmandu'), ('Pokhara', 'Pokhara'), ('Baglung', 'Baglung'), ('Butwal', 'Butwal')], max_length=50),
        ),
        migrations.DeleteModel(
            name='BusSchedule',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
