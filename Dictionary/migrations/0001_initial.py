# Generated by Django 5.1 on 2024-10-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name': 'Dictionary',
                'verbose_name_plural': 'Dictionary',
            },
        ),
    ]
