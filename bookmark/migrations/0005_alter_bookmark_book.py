# Generated by Django 4.2.6 on 2023-10-28 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booklibrary', '0002_alter_userbook_book'),
        ('bookmark', '0004_remove_bookmark_author_remove_bookmark_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booklibrary.userbook'),
        ),
    ]
