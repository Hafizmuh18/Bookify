# Generated by Django 4.2.6 on 2023-10-29 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_merge_20231029_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('member', 'Member'), ('moderator', 'Moderator')], default='member', max_length=10),
        ),
    ]