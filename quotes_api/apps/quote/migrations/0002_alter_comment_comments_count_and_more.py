# Generated by Django 4.0.3 on 2022-03-19 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comments_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='downs_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='ups_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quote',
            name='comments_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quote',
            name='downs_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quote',
            name='ups_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]