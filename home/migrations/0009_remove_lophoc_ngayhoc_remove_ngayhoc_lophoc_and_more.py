# Generated by Django 4.0.5 on 2022-06-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_ngayhoc_lophoc_alter_lophoc_ngayhoc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lophoc',
            name='ngayHoc',
        ),
        migrations.RemoveField(
            model_name='ngayhoc',
            name='lopHoc',
        ),
        migrations.AddField(
            model_name='lophoc',
            name='lichHoc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]