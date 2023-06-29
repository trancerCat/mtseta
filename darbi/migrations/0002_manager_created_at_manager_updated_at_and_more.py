# Generated by Django 4.1.7 on 2023-04-04 16:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('darbi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manager',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='advance_payment',
            field=models.IntegerField(verbose_name='Avansa summa'),
        ),
        migrations.AlterField(
            model_name='project',
            name='advance_payment_date',
            field=models.DateField(verbose_name='Avansa datums'),
        ),
        migrations.AlterField(
            model_name='project',
            name='automation',
            field=models.IntegerField(verbose_name='Aut.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Pabeigts'),
        ),
        migrations.AlterField(
            model_name='project',
            name='completion_date',
            field=models.DateField(verbose_name='Pabeigšanas datums'),
        ),
        migrations.AlterField(
            model_name='project',
            name='concrete_column',
            field=models.IntegerField(verbose_name='Betona stabi'),
        ),
        migrations.AlterField(
            model_name='project',
            name='concrete_foundation',
            field=models.IntegerField(verbose_name='Betona cokoli'),
        ),
        migrations.AlterField(
            model_name='project',
            name='concrete_slab',
            field=models.IntegerField(verbose_name='Betona pasētas'),
        ),
        migrations.AlterField(
            model_name='project',
            name='delivery_date',
            field=models.DateField(verbose_name='Nodošanas datums'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=250, verbose_name='Objekta apraksts'),
        ),
        migrations.AlterField(
            model_name='project',
            name='forged_window',
            field=models.IntegerField(verbose_name='Kaltie posmi'),
        ),
        migrations.AlterField(
            model_name='project',
            name='large_gate',
            field=models.IntegerField(verbose_name='Lielie vārti'),
        ),
        migrations.AlterField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='darbi.manager', verbose_name='Menedžeris'),
        ),
        migrations.AlterField(
            model_name='project',
            name='mesh_in_roll',
            field=models.IntegerField(verbose_name='Siets ruļļos'),
        ),
        migrations.AlterField(
            model_name='project',
            name='metal_column',
            field=models.IntegerField(verbose_name='Metāla stabi'),
        ),
        migrations.AlterField(
            model_name='project',
            name='panel_3d2d',
            field=models.IntegerField(verbose_name='Paneļi 3D/2D'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sliding_gate',
            field=models.IntegerField(verbose_name='Bīdāmie vārti'),
        ),
        migrations.AlterField(
            model_name='project',
            name='small_gate',
            field=models.IntegerField(verbose_name='Mazie vārti'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Adrese'),
        ),
        migrations.AlterField(
            model_name='project',
            name='wooden_frame',
            field=models.IntegerField(verbose_name='Koka posmi'),
        ),
    ]