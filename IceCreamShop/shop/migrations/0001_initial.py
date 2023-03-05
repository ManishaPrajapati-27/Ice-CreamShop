# Generated by Django 4.1.7 on 2023-02-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('email', models.CharField(max_length=125)),
                ('phone', models.CharField(max_length=125)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
