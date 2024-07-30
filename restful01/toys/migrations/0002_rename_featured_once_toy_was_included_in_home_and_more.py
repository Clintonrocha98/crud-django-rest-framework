# Generated by Django 5.0.7 on 2024-07-30 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toy',
            old_name='featured_once',
            new_name='was_included_in_home',
        ),
        migrations.AlterField(
            model_name='toy',
            name='description',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]
