# Generated by Django 2.1.5 on 2019-03-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mineral', '0002_auto_20190315_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineral',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='cleavage',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_habit',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_symmetry',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_system',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='diaphaneity',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='formula',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='group',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='image_caption',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='image_filename',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='luster',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='mohs_scale_hardness',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='optical_properties',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='refractive_index',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='specific_gravity',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='streak',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='strunz_classification',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='unit_cell',
            field=models.TextField(),
        ),
    ]
