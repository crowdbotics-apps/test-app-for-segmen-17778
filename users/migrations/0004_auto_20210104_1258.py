# Generated by Django 2.2.17 on 2021-01-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_auto_20210104_1256"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="field_10",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="field_11",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="field_12",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="field_13",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="field_14",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="field_15",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
