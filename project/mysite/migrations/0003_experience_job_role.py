# Generated by Django 2.2.1 on 2019-05-02 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_remove_experience_job_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='job_role',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
