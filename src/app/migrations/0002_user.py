# Generated by Django 4.0.2 on 2022-02-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('tg_id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phoneNumber', models.CharField(blank=True, max_length=16, unique=True)),
            ],
        ),
    ]
