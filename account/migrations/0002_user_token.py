# Generated by Django 4.0.4 on 2022-04-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
    ]