# Generated by Django 2.2.10 on 2020-04-24 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0011_merge_20200312_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalindicator',
            name='target_frequency',
            field=models.IntegerField(blank=True, choices=[(1, 'Life of Program only'), (3, 'Every Year'), (4, 'Every Six Months'), (5, 'Every Four Months'), (6, 'Every Three Months'), (7, 'Every Month'), (8, 'Every Week'), (9, 'Every Two Weeks')], help_text=' ', null=True, verbose_name='Target frequency'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='target_frequency',
            field=models.IntegerField(blank=True, choices=[(1, 'Life of Program only'), (3, 'Every Year'), (4, 'Every Six Months'), (5, 'Every Four Months'), (6, 'Every Three Months'), (7, 'Every Month'), (8, 'Every Week'), (9, 'Every Two Weeks')], help_text=' ', null=True, verbose_name='Target frequency'),
        ),
    ]
