# Generated by Django 3.0 on 2022-04-14 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0039_leagues'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leagues',
            old_name='league_t2_points',
            new_name='rank',
        ),
        migrations.RemoveField(
            model_name='leagues',
            name='league_t3_points',
        ),
        migrations.RemoveField(
            model_name='leagues',
            name='league_t4_points',
        ),
        migrations.RemoveField(
            model_name='leagues',
            name='league_t5_points',
        ),
        migrations.RemoveField(
            model_name='leagues',
            name='league_team2',
        ),
        migrations.RemoveField(
            model_name='leagues',
            name='league_team3',
        ),
        migrations.RemoveField(
            model_name='leagues',
            name='league_team4',
        ),
        migrations.RemoveField(
            model_name='leagues',
            name='league_team5',
        ),
    ]
