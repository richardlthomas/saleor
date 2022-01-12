# Generated by Django 3.2.6 on 2021-12-17 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tax", "0001_initial"),
        ("channel", "0003_alter_channel_default_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="channel",
            name="tax_setting",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="channels",
                to="tax.taxsetting",
            ),
        ),
    ]
