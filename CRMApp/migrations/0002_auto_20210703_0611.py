# Generated by Django 3.2.4 on 2021-07-03 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRMApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='frompincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='otherValue',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='topincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='taxableAmount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
    ]