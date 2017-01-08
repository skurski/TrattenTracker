# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-08 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ttapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancelledTrainings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='dzień odwołanych zajęć')),
            ],
            options={
                'verbose_name': 'odwołany trening',
                'verbose_name_plural': 'Odwołane treningi',
            },
        ),
        migrations.AlterUniqueTogether(
            name='trainingmonth',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='trainingmonth',
            name='group',
        ),
        migrations.AlterModelOptions(
            name='attendance',
            options={'verbose_name': 'obecność', 'verbose_name_plural': 'Obecności'},
        ),
        migrations.AlterModelOptions(
            name='attendees',
            options={'verbose_name': 'uczestnik', 'verbose_name_plural': 'Uczestnicy'},
        ),
        migrations.AlterModelOptions(
            name='groups',
            options={'verbose_name': 'grupa', 'verbose_name_plural': 'Grupy'},
        ),
        migrations.AlterModelOptions(
            name='monthlybalance',
            options={'verbose_name': 'stan konta', 'verbose_name_plural': 'Bilans'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'płatność', 'verbose_name_plural': 'Płatności'},
        ),
        migrations.AddField(
            model_name='trainingschedule',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='od daty'),
        ),
        migrations.AddField(
            model_name='trainingschedule',
            name='stop_date',
            field=models.DateField(blank=True, null=True, verbose_name='do daty'),
        ),
        migrations.AlterField(
            model_name='trainingschedule',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to='ttapp.Groups', verbose_name='Grupa'),
        ),
        migrations.AlterUniqueTogether(
            name='trainingschedule',
            unique_together=set([('group', 'dow', 'begin_time', 'start_date')]),
        ),
        migrations.DeleteModel(
            name='TrainingMonth',
        ),
        migrations.AddField(
            model_name='cancelledtrainings',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cancelled', to='ttapp.TrainingSchedule', verbose_name='Trening'),
        ),
        migrations.AlterUniqueTogether(
            name='cancelledtrainings',
            unique_together=set([('schedule', 'date')]),
        ),
    ]