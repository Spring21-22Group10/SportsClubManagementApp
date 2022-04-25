# Generated by Django 3.0 on 2022-04-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0040_auto_20220425_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandise',
            name='stock',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='item_image',
            field=models.ImageField(upload_to='merch'),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='item_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='price',
            field=models.IntegerField(),
        ),
    ]