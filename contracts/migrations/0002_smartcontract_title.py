# Generated by Django 3.2 on 2021-06-26 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartcontract',
            name='title',
            field=models.CharField(blank=True, max_length=140),
        ),
    ]
