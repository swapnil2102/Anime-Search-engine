# Generated by Django 3.2 on 2021-05-09 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globe', '0003_auto_20210509_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='img',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
    ]
