# Generated by Django 4.0.5 on 2022-07-02 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_hocvien_lophoc_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hocphi_hocvien',
            name='phuHuynh_id',
        ),
    ]
