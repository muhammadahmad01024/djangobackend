# Generated by Django 3.1.1 on 2021-01-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('panelName', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('rowId', models.IntegerField()),
                ('commentText', models.CharField(max_length=2000)),
            ],
        ),
    ]
