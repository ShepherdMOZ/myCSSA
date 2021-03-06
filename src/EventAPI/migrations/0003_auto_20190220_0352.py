# Generated by Django 2.1.7 on 2019-02-20 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventAPI', '0002_attendevent_attendeduserid'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='hasMaxAttendent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='isFree',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='event',
            name='mainVisual',
            field=models.ImageField(default=None, null=True, upload_to='uploads/usrImage/'),
        ),
        migrations.AddField(
            model_name='event',
            name='maxAttendent',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
