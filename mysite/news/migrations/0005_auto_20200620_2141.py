# Generated by Django 3.0.7 on 2020-06-20 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200610_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='news.Category', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
