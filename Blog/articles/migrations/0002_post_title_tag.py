# Generated by Django 3.0.7 on 2020-08-18 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My blog', max_length=255),
        ),
    ]
