# Generated by Django 3.1.2 on 2020-11-11 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='file/', verbose_name='ファイル')),
            ],
            options={
                'db_table': 'documentlist',
            },
        ),
        migrations.CreateModel(
            name='PhotoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photo/', verbose_name='フォト')),
            ],
            options={
                'db_table': 'photolist',
            },
        ),
    ]