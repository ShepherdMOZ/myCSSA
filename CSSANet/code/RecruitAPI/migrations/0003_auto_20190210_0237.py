# Generated by Django 2.1.5 on 2019-02-10 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecruitAPI', '0002_joblist_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='isReject',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='joblist',
            name='dueDate',
            field=models.DateTimeField(default=None, null=True, verbose_name='截止日期'),
        ),
    ]