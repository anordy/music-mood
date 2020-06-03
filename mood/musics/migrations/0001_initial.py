# Generated by Django 3.0.6 on 2020-05-29 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('user_id', models.IntegerField(default=0)),
                ('cover', models.ImageField(upload_to='covers')),
                ('album_file', models.FileField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time', models.DateTimeField(verbose_name='date published')),
                ('artists_id', models.IntegerField(default=0)),
                ('album_id', models.IntegerField(default=0)),
                ('genre', models.CharField(max_length=50)),
                ('song_file', models.FileField(default='', upload_to='')),
            ],
        ),
    ]
