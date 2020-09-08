# Generated by Django 3.1 on 2020-09-08 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_cart_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='category',
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.user'),
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.category')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product')),
            ],
        ),
    ]
