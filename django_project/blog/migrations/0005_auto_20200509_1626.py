# Generated by Django 3.0.4 on 2020-05-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200509_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='blog/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(default='Default.mp4', upload_to=''),
        ),
    ]
