# Generated by Django 3.2.7 on 2023-02-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_person_db_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='processed_video',
            field=models.FileField(default='Na', upload_to='processed_video'),
        ),
    ]
