# Generated by Django 5.0.4 on 2024-04-14 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('short_description', models.TextField()),
                ('long_description', models.TextField()),
                ('product_photo', models.URLField()),
                ('likes', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, max_length=20, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
