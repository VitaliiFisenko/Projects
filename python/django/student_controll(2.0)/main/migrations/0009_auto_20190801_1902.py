# Generated by Django 2.2.2 on 2019-08-01 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190801_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='subject',
            field=models.ManyToManyField(blank=True, null=True, to='main.Subjects'),
        ),
        migrations.AlterField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(blank=True, null=True, to='main.Subjects'),
        ),
    ]
