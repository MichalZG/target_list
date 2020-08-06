# Generated by Django 3.0.8 on 2020-08-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='target',
            name='days_from_last_observations',
        ),
        migrations.RemoveField(
            model_name='target',
            name='observations_number',
        ),
        migrations.AddField(
            model_name='target',
            name='eclipse_duration',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='target',
            name='m0',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=14, null=True),
        ),
        migrations.AddField(
            model_name='target',
            name='p',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=14, null=True),
        ),
    ]