# Generated by Django 4.0.1 on 2022-02-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='Kurs Aciklamasi'),
        ),
    ]
