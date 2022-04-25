# Generated by Django 3.0 on 2022-04-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0042_auto_20220425_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=30)),
                ('position', models.CharField(choices=[('Goalkeeper', 'Goalkeeper'), ('Defender', 'Defender'), ('Midfielder', 'Midfielder'), ('Forward', 'Forward')], max_length=30)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='teams')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='male', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='teams'),
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('Goalkeeper', 'Goalkeeper'), ('Defender', 'Defender'), ('Midfielder', 'Midfielder'), ('Forward', 'Forward')], default='Goalkeeper', max_length=30),
            preserve_default=False,
        ),
    ]
