# Generated by Django 3.0.7 on 2020-08-18 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=255),
        ),
    ]