# Generated by Django 3.1.1 on 2020-09-29 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_author_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='sex',
            field=models.CharField(max_length=255),
        ),
    ]
