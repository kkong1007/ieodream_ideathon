# Generated by Django 3.2.4 on 2021-08-13 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_postm_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postm',
            name='document',
        ),
        migrations.AddField(
            model_name='blogi',
            name='final',
            field=models.ImageField(blank=True, null=True, upload_to='blogI/'),
        ),
        migrations.AddField(
            model_name='blogm',
            name='final',
            field=models.ImageField(blank=True, null=True, upload_to='blogM/'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='final',
            field=models.ImageField(blank=True, null=True, upload_to='blogS/'),
        ),
    ]
