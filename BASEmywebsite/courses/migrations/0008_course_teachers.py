# Generated by Django 4.0.1 on 2022-02-07 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('courses', '0007_remove_course_tags_course_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher'),
        ),
    ]