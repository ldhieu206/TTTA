# Generated by Django 4.0.5 on 2022-07-04 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_remove_hocphi_hocvien_hocphi'),
    ]

    operations = [
        migrations.AddField(
            model_name='hocphi_hocvien',
            name='hocPhi',
            field=models.IntegerField(default=0),
        ),
    ]
