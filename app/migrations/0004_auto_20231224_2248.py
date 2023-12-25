# Generated by Django 3.1.1 on 2023-12-24 17:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_busschedule_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('seats', models.IntegerField()),
                ('status', models.CharField(choices=[('1', 'Pending'), ('2', 'Paid')], default=1, max_length=2)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default=1, max_length=2)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default=1, max_length=2)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('schedule', models.DateTimeField()),
                ('fare', models.FloatField()),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Cancelled')], default=1, max_length=2)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='bus_schedule',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='arrival_time',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='departure_location',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='departure_time',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='price',
        ),
        migrations.AddField(
            model_name='bus',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bus',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='bus',
            name='seats',
            field=models.FloatField(default=0, max_length=5),
        ),
        migrations.AddField(
            model_name='bus',
            name='status',
            field=models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='bus',
            name='bus_number',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='BusSchedule',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.AddField(
            model_name='schedule',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bus'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='depart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depart_location', to='app.location'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='app.location'),
        ),
        migrations.AddField(
            model_name='booking',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.schedule'),
        ),
        migrations.AddField(
            model_name='bus',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]