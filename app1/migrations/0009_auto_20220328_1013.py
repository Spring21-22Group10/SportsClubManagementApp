# Generated by Django 3.0 on 2022-03-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20220328_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Player_username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]