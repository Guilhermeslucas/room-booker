# Generated by Django 2.1 on 2018-08-27 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0003_auto_20180827_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.IntegerField(),
        ),
    ]