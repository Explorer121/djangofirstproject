# Generated by Django 3.0.6 on 2020-05-28 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(1, 'Worst'), (2, 'Bad'), (3, 'Not Bad'), (4, 'Good'), (5, 'Excellent')]),
        ),
    ]
