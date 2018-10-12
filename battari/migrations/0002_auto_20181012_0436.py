# Generated by Django 2.1.1 on 2018-10-12 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battari', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('spotify_id', models.CharField(max_length=30)),
                ('comment', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserAction',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='useraction',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battari.User'),
        ),
        migrations.AddField(
            model_name='notification',
            name='receive_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battari.User'),
        ),
        migrations.AddField(
            model_name='map',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battari.User'),
        ),
    ]
