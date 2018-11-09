# Generated by Django 2.1.1 on 2018-11-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battari', '0005_auto_20181107_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='firebase_token',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='spotify_id',
            field=models.TextField(),
        ),
    ]