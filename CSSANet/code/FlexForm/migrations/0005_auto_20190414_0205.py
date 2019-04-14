# Generated by Django 2.2 on 2019-04-14 02:05

import FlexForm.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlexForm', '0004_auto_20190414_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexformdata',
            name='date_value',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='flexformdata',
            name='file_input',
            field=models.FileField(blank=True, default=None, null=True, upload_to=FlexForm.models._GetFormUploadsDir),
        ),
        migrations.AddField(
            model_name='flexformdata',
            name='time_value',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='flexformfield',
            name='field_type',
            field=models.CharField(choices=[('文本', 'text'), ('数字', 'digit'), ('文件', 'file'), ('日期', 'date'), ('时间', 'time')], max_length=10, verbose_name='字段类型'),
        ),
    ]
