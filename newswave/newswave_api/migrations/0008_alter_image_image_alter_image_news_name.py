# Generated by Django 4.2.4 on 2023-08-17 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newswave_api', '0007_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='news_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newswave_api.news'),
        ),
    ]
