# Generated by Django 2.1.3 on 2018-12-21 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PublicSite', '0002_auto_20181205_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicAccessControl',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('uri', models.CharField(max_length=500)),
                ('is_accessible', models.BooleanField(default=False)),
            ],
        ),
    ]