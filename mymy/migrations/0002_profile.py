# Generated by Django 2.1.7 on 2019-03-27 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tier', models.CharField(max_length=100)),
            ],
        ),
    ]
