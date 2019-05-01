# Generated by Django 2.2 on 2019-04-30 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoCompetition', '0003_auto_20190420_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='categoryType',
            field=models.CharField(choices=[('Nature', '风景'), ('Culture', '人文')], default='风景', max_length=30, null=True, verbose_name='题材类型'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='deviceType',
            field=models.CharField(choices=[('MobilePhone', '手机'), ('Camera', '相机')], default='手机', max_length=30, null=True, verbose_name='设备类型'),
        ),
    ]
