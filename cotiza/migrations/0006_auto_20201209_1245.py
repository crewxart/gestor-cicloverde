# Generated by Django 3.1.4 on 2020-12-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotiza', '0005_trabajadores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asesorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_asesoria', models.CharField(max_length=100)),
                ('monto', models.DecimalField(decimal_places=1, max_digits=6)),
                ('mes', models.CharField(max_length=50)),
                ('total', models.DecimalField(decimal_places=1, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='GastosAdministrativos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gastos_comunes', models.DecimalField(decimal_places=1, max_digits=8)),
                ('insumos_aseo', models.DecimalField(decimal_places=1, max_digits=8)),
                ('insumos_oficina', models.DecimalField(decimal_places=1, max_digits=8)),
                ('mantencion_banco', models.DecimalField(decimal_places=1, max_digits=8)),
                ('TI', models.DecimalField(decimal_places=1, max_digits=8)),
                ('arriendo', models.DecimalField(decimal_places=1, max_digits=8)),
                ('patentes', models.DecimalField(decimal_places=1, max_digits=8)),
                ('encomiendas', models.DecimalField(decimal_places=1, max_digits=8)),
                ('ropa_trabajadores', models.DecimalField(decimal_places=1, max_digits=8)),
                ('permisos_circulacion', models.DecimalField(decimal_places=1, max_digits=8)),
                ('generales', models.DecimalField(decimal_places=1, max_digits=8)),
                ('mes', models.CharField(max_length=50)),
                ('total', models.DecimalField(decimal_places=1, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='GastosProduccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electricidad', models.DecimalField(decimal_places=1, max_digits=8)),
                ('gas_grua', models.DecimalField(decimal_places=1, max_digits=8)),
                ('petroleo', models.DecimalField(decimal_places=1, max_digits=8)),
                ('cordel', models.DecimalField(decimal_places=1, max_digits=8)),
                ('insumos_epp', models.DecimalField(decimal_places=1, max_digits=8)),
                ('mantencion_maquinaria', models.DecimalField(decimal_places=1, max_digits=8)),
                ('insumos_planta', models.DecimalField(decimal_places=1, max_digits=8)),
                ('mes', models.CharField(max_length=50)),
                ('total', models.DecimalField(decimal_places=1, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='GastosTotales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=50)),
                ('sueldos', models.DecimalField(decimal_places=1, max_digits=8)),
                ('total_asesorias', models.DecimalField(decimal_places=1, max_digits=8)),
                ('total_administrativos', models.DecimalField(decimal_places=1, max_digits=8)),
                ('total_produccion', models.DecimalField(decimal_places=1, max_digits=8)),
                ('costo_operativo_dia', models.DecimalField(decimal_places=1, max_digits=8)),
                ('costo_operativo_hora', models.DecimalField(decimal_places=1, max_digits=8)),
                ('costo_operativo_mes', models.DecimalField(decimal_places=1, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Petroleo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=50)),
                ('valor_actual', models.DecimalField(decimal_places=1, max_digits=8)),
                ('valor_anterior', models.DecimalField(decimal_places=1, max_digits=8)),
            ],
        ),
        migrations.AlterField(
            model_name='clientes',
            name='celular',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.IntegerField(blank=True),
        ),
    ]
