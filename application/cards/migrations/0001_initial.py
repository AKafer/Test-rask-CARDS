# Generated by Django 4.1.3 on 2022-12-05 18:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1000)])),
                ('number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999999), django.core.validators.MinValueValidator(100000000000)])),
                ('date_issue', models.DateTimeField(auto_now_add=True)),
                ('date_expiration', models.DateTimeField()),
                ('limit', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('not_activated', 'not_activated'), ('active', 'active'), ('expired', 'expired')], default='created', max_length=30)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.IntegerField()),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('purchase', 'purchase'), ('adding', 'adding'), ('transfer', 'transfer')], max_length=30)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to='cards.card')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
