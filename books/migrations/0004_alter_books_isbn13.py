# Generated by Django 4.2.5 on 2023-10-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_books_isbn10'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='isbn13',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
