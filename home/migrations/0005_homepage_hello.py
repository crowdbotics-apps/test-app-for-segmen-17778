# Generated by Django 2.2.17 on 2021-01-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_student"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="hello",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]