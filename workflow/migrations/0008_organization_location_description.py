# Generated by Django 2.2.10 on 2020-02-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0007_auto_20200227_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='location_description',
            field=models.TextField(blank=True, max_length=765, null=True, verbose_name='Location Description/Notes'),
        ),
    ]
