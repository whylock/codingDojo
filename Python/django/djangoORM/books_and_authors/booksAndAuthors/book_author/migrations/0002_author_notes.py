# Generated by Django 2.2.4 on 2020-08-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='notes'),
            preserve_default=False,
        ),
    ]
