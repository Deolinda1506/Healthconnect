# Generated by Django 5.0.6 on 2024-07-30 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0008_prescription_unique_link_prescription_valid'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='refill_request',
            field=models.BooleanField(default=False),
        ),
    ]
