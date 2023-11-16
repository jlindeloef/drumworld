# Generated by Django 3.2.23 on 2023-11-16 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='drums', on_delete=django.db.models.deletion.PROTECT, to='blog.category'),
        ),
    ]