# Generated by Django 4.2.3 on 2023-07-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('project_resume', models.CharField(max_length=256)),
                ('utl', models.CharField(choices=[('PT', 'Python'), ('CSS', 'CSS'), ('JS', 'Java Script'), ('DK', 'Docker'), ('DJ', 'Django'), ('JSON', 'JSON'), ('HT ', 'HTML'), ('TK ', 'TKInter'), ('SQ', 'SQlite'), ('API', 'API'), ('WS', 'Web Scraping'), ('GT', 'Git'), ('GH', 'GitHub')], max_length=4)),
                ('utl1', models.CharField(blank=True, choices=[('PT', 'Python'), ('CSS', 'CSS'), ('JS', 'Java Script'), ('DK', 'Docker'), ('DJ', 'Django'), ('JSON', 'JSON'), ('HT ', 'HTML'), ('TK ', 'TKInter'), ('SQ', 'SQlite'), ('API', 'API'), ('WS', 'Web Scraping'), ('GT', 'Git'), ('GH', 'GitHub')], max_length=4)),
                ('utl2', models.CharField(blank=True, choices=[('PT', 'Python'), ('CSS', 'CSS'), ('JS', 'Java Script'), ('DK', 'Docker'), ('DJ', 'Django'), ('JSON', 'JSON'), ('HT ', 'HTML'), ('TK ', 'TKInter'), ('SQ', 'SQlite'), ('API', 'API'), ('WS', 'Web Scraping'), ('GT', 'Git'), ('GH', 'GitHub')], max_length=4)),
                ('utl3', models.CharField(blank=True, choices=[('PT', 'Python'), ('CSS', 'CSS'), ('JS', 'Java Script'), ('DK', 'Docker'), ('DJ', 'Django'), ('JSON', 'JSON'), ('HT ', 'HTML'), ('TK ', 'TKInter'), ('SQ', 'SQlite'), ('API', 'API'), ('WS', 'Web Scraping'), ('GT', 'Git'), ('GH', 'GitHub')], max_length=4)),
                ('utl4', models.CharField(blank=True, choices=[('PT', 'Python'), ('CSS', 'CSS'), ('JS', 'Java Script'), ('DK', 'Docker'), ('DJ', 'Django'), ('JSON', 'JSON'), ('HT ', 'HTML'), ('TK ', 'TKInter'), ('SQ', 'SQlite'), ('API', 'API'), ('WS', 'Web Scraping'), ('GT', 'Git'), ('GH', 'GitHub')], max_length=4)),
                ('utl5', models.CharField(blank=True, choices=[('PT', 'Python'), ('CSS', 'CSS'), ('JS', 'Java Script'), ('DK', 'Docker'), ('DJ', 'Django'), ('JSON', 'JSON'), ('HT ', 'HTML'), ('TK ', 'TKInter'), ('SQ', 'SQlite'), ('API', 'API'), ('WS', 'Web Scraping'), ('GT', 'Git'), ('GH', 'GitHub')], max_length=4)),
                ('utl6', models.CharField(blank=True, choices=[('PT', 'Python'), ('CSS', 'CSS'), ('JS', 'Java Script'), ('DK', 'Docker'), ('DJ', 'Django'), ('JSON', 'JSON'), ('HT ', 'HTML'), ('TK ', 'TKInter'), ('SQ', 'SQlite'), ('API', 'API'), ('WS', 'Web Scraping'), ('GT', 'Git'), ('GH', 'GitHub')], max_length=4)),
                ('utl7', models.CharField(blank=True, choices=[('PT', 'Python'), ('CSS', 'CSS'), ('JS', 'Java Script'), ('DK', 'Docker'), ('DJ', 'Django'), ('JSON', 'JSON'), ('HT ', 'HTML'), ('TK ', 'TKInter'), ('SQ', 'SQlite'), ('API', 'API'), ('WS', 'Web Scraping'), ('GT', 'Git'), ('GH', 'GitHub')], max_length=4)),
                ('project_start_date', models.DateField()),
                ('project_status', models.CharField(choices=[('K', 'Kuriamas'), ('U', 'Užbaigtas')], max_length=1)),
                ('c_remarks', models.CharField(default='-', max_length=256, verbose_name='Pastabos')),
                ('c_created_at', models.DateTimeField(auto_now_add=True)),
                ('c_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
