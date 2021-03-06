# Generated by Django 2.2.1 on 2019-05-09 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthAPI', '0017_auto_20190430_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cssacommitteprofile',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserAuthAPI.UserProfile'),
        ),
        migrations.AlterField(
            model_name='useracademic',
            name='userProfile',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='UserAuthAPI.UserProfile'),
        ),
    ]
