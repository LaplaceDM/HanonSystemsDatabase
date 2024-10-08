# Generated by Django 4.2.15 on 2024-08-28 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='darchannel',
            name='channel_number',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fluid',
            name='manufacturer',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lab',
            name='lab_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_family',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='variant',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='program',
            name='program_name',
            field=models.CharField(default='', max_length=50, verbose_name='Program'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='test_description',
            field=models.TextField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='test_type_id',
            field=models.ForeignKey(db_column='test_type_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='database.testtype', verbose_name='Test Type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testmap',
            name='test_map_name',
            field=models.CharField(default='', max_length=100, verbose_name='Test Map Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testmap',
            name='tr',
            field=models.CharField(default='', max_length=14, verbose_name='TR'),
            preserve_default=False,
        ),
    ]
