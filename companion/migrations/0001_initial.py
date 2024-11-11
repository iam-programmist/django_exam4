# Generated by Django 5.0 on 2024-11-11 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=100)),
                ('car_number', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='companion.country')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField(auto_now=True)),
                ('end_time', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='companion.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField(auto_now=True)),
                ('available_seats', models.IntegerField()),
                ('price_per_seat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='companion.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_point', models.CharField(max_length=255)),
                ('end_point', models.CharField(max_length=255)),
                ('distance_km', models.IntegerField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='companion.trip')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_at', models.DateTimeField(auto_now_add=True)),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='companion.passenger')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='companion.trip')),
            ],
        ),
        migrations.CreateModel(
            name='DriverRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('review', models.TextField(blank=True, null=True)),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='companion.passenger')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='companion.trip')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats_reserved', models.IntegerField()),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='companion.passenger')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='companion.trip')),
            ],
        ),
        migrations.CreateModel(
            name='TripLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='companion.trip')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('is_driver', models.BooleanField(default=False)),
                ('is_passenger', models.BooleanField(default=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_city', to='companion.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_country', to='companion.country')),
            ],
        ),
        migrations.AddField(
            model_name='passenger',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='passenger', to='companion.user'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='companion.user')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='companion.user')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='companion.user'),
        ),
    ]
