# Generated by Django 4.0.5 on 2022-07-05 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_hocphi_hocvien_lophoc_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giaovien_buoihoc',
            name='caHoc_id',
        ),
        migrations.RemoveField(
            model_name='giaovien_buoihoc',
            name='traLuong',
        ),
    ]