# Generated by Django 3.2.6 on 2021-09-19 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('merlin', '0003_dynamicjobinput'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamicjobinput',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
