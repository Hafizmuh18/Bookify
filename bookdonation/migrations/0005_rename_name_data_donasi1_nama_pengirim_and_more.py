# Generated by Django 4.2.6 on 2023-10-25 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookdonation', '0004_rename_item_data_donasi1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data_donasi1',
            old_name='name',
            new_name='nama_pengirim',
        ),
        migrations.RenameField(
            model_name='data_donasi1',
            old_name='description',
            new_name='resi',
        ),
        migrations.RenameField(
            model_name='data_donasi1',
            old_name='amount',
            new_name='total_buku',
        ),
    ]
