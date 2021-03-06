# Generated by Django 3.2.3 on 2021-06-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='desc',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='humd',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='lon',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='precip',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='soilt',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='temp',
            field=models.FloatField(null=True),
        ),
    ]
