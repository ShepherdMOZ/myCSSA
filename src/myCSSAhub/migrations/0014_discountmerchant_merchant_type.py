# Generated by Django 2.1.7 on 2019-03-06 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCSSAhub', '0013_auto_20190306_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountmerchant',
            name='merchant_type',
            field=models.CharField(choices=[('折扣商家', '折扣商家'), ('赞助商家', '赞助商家')], max_length=10, null=True),
        ),
    ]
