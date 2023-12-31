# Generated by Django 4.1.7 on 2023-04-03 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('concrete_column', models.IntegerField()),
                ('concrete_foundation', models.IntegerField()),
                ('concrete_slab', models.IntegerField()),
                ('wooden_frame', models.IntegerField()),
                ('metal_column', models.IntegerField()),
                ('forged_window', models.IntegerField()),
                ('panel_3d2d', models.IntegerField()),
                ('mesh_in_roll', models.IntegerField()),
                ('sliding_gate', models.IntegerField()),
                ('small_gate', models.IntegerField()),
                ('large_gate', models.IntegerField()),
                ('automation', models.IntegerField()),
                ('description', models.CharField(max_length=250)),
                ('advance_payment', models.IntegerField()),
                ('advance_payment_date', models.DateField()),
                ('delivery_date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
                ('completion_date', models.DateField()),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='darbi.manager')),
            ],
        ),
    ]
