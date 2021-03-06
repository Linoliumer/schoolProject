# Generated by Django 3.0.5 on 2020-04-27 02:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('name_person', models.CharField(max_length=30)),
                ('theme_question', models.CharField(max_length=100)),
                ('full_text', models.TextField(max_length=2000)),
                ('created_time_quest', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
