# Generated by Django 4.0.1 on 2023-11-10 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('name', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
                ('phneno', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('exp', models.CharField(max_length=256)),
            ],
        ),
    ]