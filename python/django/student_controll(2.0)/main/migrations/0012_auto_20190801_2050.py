# Generated by Django 2.2.2 on 2019-08-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_departament_progress_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='group',
        ),
        migrations.AddField(
            model_name='teacher',
            name='group',
            field=models.ManyToManyField(blank=True, default=None, to='main.Groups'),
        ),
    ]
