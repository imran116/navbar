# Generated by Django 4.2.2 on 2023-06-26 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_menuitem_html_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=59)),
                ('contact', models.IntegerField()),
                ('country', models.CharField(max_length=59)),
            ],
        ),
    ]
