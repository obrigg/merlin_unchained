# Generated by Django 3.2.6 on 2021-09-11 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merlin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowIPIntBrief',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pyats_alias', models.TextField()),
                ('os', models.TextField()),
                ('interface', models.TextField()),
                ('interface_status', models.TextField()),
                ('ip_address', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
