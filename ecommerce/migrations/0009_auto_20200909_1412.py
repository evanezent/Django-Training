# Generated by Django 3.1 on 2020-09-09 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_auto_20200908_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img_url',
            field=models.FileField(null=True, upload_to='user'),
        ),
    ]