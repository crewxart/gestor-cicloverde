# Generated by Django 3.1.4 on 2020-12-09 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotiza', '0006_auto_20201209_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asesorias',
            name='monto',
        ),
        migrations.RemoveField(
            model_name='asesorias',
            name='tipo_asesoria',
        ),
        migrations.AddField(
            model_name='asesorias',
            name='contabilidad',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asesorias',
            name='prevencionista',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asesorias',
            name='sanitizacion',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=9),
            preserve_default=False,
        ),
    ]