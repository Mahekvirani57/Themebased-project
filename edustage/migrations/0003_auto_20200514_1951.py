# Generated by Django 3.0.6 on 2020-05-14 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edustage', '0002_destination_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('field_name', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='destination',
            name='offer',
        ),
        migrations.AddField(
            model_name='destination',
            name='ref',
            field=models.CharField(default='tutorial', max_length=100),
        ),
    ]