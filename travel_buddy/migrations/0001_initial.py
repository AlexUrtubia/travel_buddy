# Generated by Django 3.2.7 on 2021-09-27 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('plan', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('joined', models.ManyToManyField(related_name='join', to='login.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travels', to='login.user')),
            ],
        ),
    ]
