# Generated by Django 2.2.17 on 2021-01-04 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_hello'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='name',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
