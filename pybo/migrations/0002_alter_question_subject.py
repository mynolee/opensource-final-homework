# Generated by Django 4.0.5 on 2022-06-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.CharField(max_length=300),
        ),
    ]
