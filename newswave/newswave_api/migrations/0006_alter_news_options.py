# Generated by Django 4.2.4 on 2023-08-17 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newswave_api', '0005_alter_news_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
    ]
