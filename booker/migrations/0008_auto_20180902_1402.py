# Generated by Django 2.1 on 2018-09-02 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0007_auto_20180901_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='begin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booker.Room'),
        ),
    ]
