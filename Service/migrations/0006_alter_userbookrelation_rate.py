# Generated by Django 3.2.5 on 2021-08-14 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0005_auto_20210814_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookrelation',
            name='rate',
            field=models.SmallIntegerField(choices=[(1, 'Not recommend'), (2, 'Boring'), (3, 'Fine'), (4, 'Good'), (5, 'Excellent')], null=True),
        ),
    ]