# Generated by Django 4.0.5 on 2022-06-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_ngaylophoc_lophoc_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ngayhoc',
            name='lopHoc',
        ),
        migrations.AlterField(
            model_name='lophoc',
            name='ngayHoc',
            field=models.ManyToManyField(blank=True, null=True, related_name='lopHoc', to='home.ngayhoc'),
        ),
    ]
