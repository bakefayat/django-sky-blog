# Generated by Django 4.0.2 on 2022-03-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_alter_module_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='display',
            field=models.BooleanField(default=True, verbose_name='نمایش'),
        ),
    ]
