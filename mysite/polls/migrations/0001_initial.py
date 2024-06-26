# Generated by Django 5.0.4 on 2024-04-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Done_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='To_do_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_do_text', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('deadline', models.DateTimeField(verbose_name='deadline')),
            ],
        ),
    ]
