# Generated by Django 4.2.10 on 2025-03-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0006_auto_20250306_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='complaintimage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
