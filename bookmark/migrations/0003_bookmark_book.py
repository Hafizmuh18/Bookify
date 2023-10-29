# Generated by Django 4.2.6 on 2023-10-28 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_books_isbn10'),
        ('bookmark', '0002_remove_bookmark_book_bookmark_author_bookmark_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.books'),
        ),
    ]
