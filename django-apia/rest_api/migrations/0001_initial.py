# Generated by Django 4.1.1 on 2022-10-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Krosovka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('size', models.IntegerField(default=40)),
                ('color', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=40)),
            ],
        ),
    ]
