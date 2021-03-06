# Generated by Django 2.1.3 on 2018-11-27 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20181127_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='evi_case',
            name='summary',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='evidence',
            name='summary',
            field=models.TextField(help_text='Enter brief description of evidence', max_length=1000, null=True),
        ),
    ]
