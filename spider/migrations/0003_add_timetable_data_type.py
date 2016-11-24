# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-26 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0002_add_orc_data_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawleddata',
            name='data_type',
            field=models.CharField(choices=[(b'medians', b'Medians'), (b'orc_department_courses', b'ORC Department Courses'), (b'course_timetable', b'Course Timetable')], max_length=32),
        ),
    ]
