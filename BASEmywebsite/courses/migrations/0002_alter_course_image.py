# Generated by Django 4.0.1 on 2022-02-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='courses/6306470.jpg', upload_to='courses/%Y/%m/%d/'),
        ),
    ]
