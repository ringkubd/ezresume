# Generated by Django 2.1.1 on 2018-10-13 05:05

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0003_auto_20181013_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='achievements',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
