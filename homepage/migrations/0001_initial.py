# Generated by Django 2.0 on 2019-01-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Regno', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
