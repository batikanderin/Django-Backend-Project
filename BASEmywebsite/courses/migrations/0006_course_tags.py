# Generated by Django 4.0.1 on 2022-02-04 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_tags_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='courses.tags'),
        ),
    ]
