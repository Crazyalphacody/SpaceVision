# Generated by Django 4.1.7 on 2023-04-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_crudeoil'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrudeOil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('SAE', models.FloatField(max_length=20)),
                ('SAX', models.FloatField(max_length=20)),
                ('SAS', models.FloatField(max_length=20)),
            ],
        ),
    ]
