# Generated by Django 4.2.3 on 2023-07-30 22:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="qrcode",
            name="validated",
            field=models.BooleanField(default=False),
        ),
    ]
