# Generated by Django 5.0.6 on 2024-07-29 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0006_prescription_dosage_prescription_prescription_and_more'),
        ('authentication', '0006_remove_patientprofile_allergies_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='prescription',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='appointment',
            name='prescription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointment_prescriptions', to='appointments.prescription'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='authentication.doctorprofile'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='authentication.patientprofile'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='appointments.appointment'),
        ),
    ]
