# Generated by Django 2.2.17 on 2021-01-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210104_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='bio',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]