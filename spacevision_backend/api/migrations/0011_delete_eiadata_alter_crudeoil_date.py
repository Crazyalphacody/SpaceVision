# Generated by Django 4.1.7 on 2023-04-23 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_eiadata_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EIAData',
        ),
        migrations.AlterField(
            model_name='crudeoil',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]