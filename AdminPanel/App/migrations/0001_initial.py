# Generated by Django 4.2.6 on 2023-10-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('user_pass', models.CharField(max_length=12)),
                ('remember_me', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='sendAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alertTime', models.DateField(auto_created=True)),
                ('alertMsg', models.CharField(max_length=100)),
                ('alertType', models.CharField(max_length=100)),
            ],
        ),
    ]