# Generated by Django 3.0 on 2022-04-06 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_auto_20220405_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('item', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
