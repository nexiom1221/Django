# Generated by Django 3.2.6 on 2021-08-28 18:19

from django.db import migrations, models
import django.db.models.deletion
import photo.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='한줄작성')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='TITLE')),
                ('description', models.TextField(blank=True, verbose_name='Photo 설명')),
                ('image', photo.fields.ThumbnailImageField(upload_to='photo/%Y/%m')),
                ('upload_dt', models.DateTimeField(auto_now_add=True, verbose_name='업로드 날짜')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.album')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]