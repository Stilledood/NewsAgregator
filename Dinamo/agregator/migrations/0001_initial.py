# Generated by Django 4.0.5 on 2022-06-14 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='news_images')),
                ('description', models.TextField()),
                ('publishing_site', models.CharField(max_length=128)),
                ('publishing_date', models.DateField()),
                ('link', models.URLField(max_length=256)),
                ('guid', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-publishing_date', 'title'],
                'get_latest_by': 'publishing_date',
            },
        ),
    ]