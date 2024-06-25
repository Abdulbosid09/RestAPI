# Generated by Django 4.2.7 on 2024-06-24 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=80)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]