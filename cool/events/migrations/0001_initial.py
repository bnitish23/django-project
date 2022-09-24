# Generated by Django 4.0.2 on 2022-09-24 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyClubUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email address')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Venue name')),
                ('address', models.TextField()),
                ('zipcode', models.CharField(max_length=6, verbose_name='Zipcode')),
                ('phone', models.CharField(max_length=10, verbose_name='contact')),
                ('web', models.URLField(verbose_name='Website address')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email address')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('event_date', models.DateTimeField(verbose_name='Event Date')),
                ('manager', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('Venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue')),
                ('attendees', models.ManyToManyField(blank=True, to='events.MyClubUser')),
            ],
        ),
    ]
