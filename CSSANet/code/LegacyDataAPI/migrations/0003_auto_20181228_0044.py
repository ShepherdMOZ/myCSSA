# Generated by Django 2.1.3 on 2018-12-28 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LegacyDataAPI', '0002_auto_20181228_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legacyusers',
            name='originate',
            field=models.CharField(max_length=50, null=True, verbose_name='籍贯'),
        ),
        migrations.AlterField(
            model_name='legacyusers',
            name='telNumber',
            field=models.CharField(max_length=15, null=True, verbose_name='联系电话'),
        ),
    ]
