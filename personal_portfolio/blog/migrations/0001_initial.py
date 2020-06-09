# Generated by Django 3.0.7 on 2020-06-09 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('blog_date', models.DateField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
