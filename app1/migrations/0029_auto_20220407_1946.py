# Generated by Django 3.0 on 2022-04-07 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_merchandise_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
