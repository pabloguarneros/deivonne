# Generated by Django 3.2 on 2021-06-27 04:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0005_auto_20210627_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartcontract',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smartcontract',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
