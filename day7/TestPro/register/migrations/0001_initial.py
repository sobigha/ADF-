"""Migrations"""
# Generated by Django 3.2.4 on 2021-07-01 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """
    Migrations
    """

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='request_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, \
                                           serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_ofbirth', models.DateField()),
                ('gender', models.CharField(max_length=8)),
                ('nationality', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pin_code', models.IntegerField()),
                ('qualification', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('pan_number', models.CharField(max_length=20)),
                ('request_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='response_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, \
                                           serialize=False, verbose_name='ID')),
                ('response_message', models.CharField(max_length=150)),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, \
                                                 to='register.request_info')),
            ],
        ),
    ]