# Generated by Django 3.0.7 on 2020-08-21 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200818_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='art_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
