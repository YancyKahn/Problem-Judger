# Generated by Django 2.1.7 on 2019-02-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_category_abbr'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type_abbr',
            field=models.CharField(default='IDN', max_length=20),
        ),
        migrations.AlterField(
            model_name='category',
            name='abbr',
            field=models.CharField(max_length=20),
        ),
    ]
