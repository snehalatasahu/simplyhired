# Generated by Django 3.1.7 on 2021-04-02 04:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20210402_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='apply_by',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]