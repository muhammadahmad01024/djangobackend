# Generated by Django 3.1.1 on 2021-01-21 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentsaaaaa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('panelName', models.CharField(max_length=200)),
                ('rowId', models.IntegerField()),
                ('commentText', models.CharField(max_length=2000)),
            ],
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
