# Generated by Django 4.2.3 on 2023-07-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('frontend', 'f'), ('backend', 'b')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'd'), ('PUBLISHED', 'p')], max_length=10),
        ),
    ]