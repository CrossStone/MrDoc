# Generated by Django 2.1 on 2020-03-13 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_doc', '0011_auto_20200313_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_doc.ImageGroup', verbose_name='图片分组'),
        ),
    ]
