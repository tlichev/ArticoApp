# Generated by Django 5.0.4 on 2024-04-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_articouser_managers_articouser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='articouser',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
