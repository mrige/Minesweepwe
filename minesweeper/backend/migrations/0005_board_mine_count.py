# Generated by Django 3.0.2 on 2020-02-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20200210_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='mine_count',
            field=models.IntegerField(default=0),
        ),
    ]