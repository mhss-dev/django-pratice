# Generated by Django 5.0.3 on 2024-04-30 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cours', models.CharField(max_length=60)),
                ('formateur', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('heures', models.IntegerField()),
            ],
        ),
    ]