from itertools import count
import json
from sys import maxsize
from tkinter.tix import MAX
from venv import create
from django.db import models
from datetime import date, datetime
# Create your models here.
from django.db import models

from django.contrib.auth.decorators import login_required

# Create your models here.

class HocVien(models.Model):
    maHV = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50)
    ngaySinh = models.DateField(null=True,blank=True)
    gioiTinh = models.CharField(max_length=50, choices=[(
        'Nam', 'Nam'), ('Nữ', 'Nữ'), ('Khác', 'Khác')], default='Nam')
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    diaChi = models.CharField(max_length=255)
    password = models.CharField(max_length=50,default='1')
    ghiChu = models.TextField(blank=True, null=True)
    duPhong2 = models.CharField(max_length=50,null=True, blank=True)
    duPhong3 = models.CharField(max_length=50,null=True, blank=True)
    duPhong4 = models.CharField(max_length=50,null=True, blank=True)
    create_at = models.DateField(null=True, blank=True,default=datetime.now())


    def __str__(self):
        return self.maHV

    def to_json(self):
        return {
            'maHV': self.maHV,
            'name': self.name,
            'ngaySinh': self.ngaySinh,
            'gioiTinh': self.gioiTinh,
            'phone': self.phone,
            'email': self.email,
            'diaChi': self.diaChi,
            'password': self.password,
            'ghiChu': self.ghiChu,
            'duPhong2': self.duPhong2,
            'duPhong3': self.duPhong3,
            'duPhong4': self.duPhong4,
        }


class GiaoVien(models.Model):
    maGV = models.CharField(max_length=50,primary_key=True)
    tenGV = models.CharField(max_length=50)
    gioiTinh = models.CharField(max_length=50,choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('Khác', 'Khác')], default='Nam')
    ngaySinh = models.DateField()
    sdt = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50,null=True,default='1')
    luongNgay = models.IntegerField()
    duPhong2 = models.CharField(max_length=50,null=True,blank=True)
    duPhong3 = models.CharField(max_length=50,null=True, blank=True)
    duPhong4 = models.CharField(max_length=50,null=True, blank=True)
    quyen = models.CharField(max_length=50,null=True, blank=True)
    create_at = models.DateTimeField(default=datetime.now(),null=True, blank=True)

    def __str__(self):
        return self.maGV

class LopHoc(models.Model):
    maLop = models.CharField(max_length=50,primary_key=True)
    tenLop = models.CharField(max_length=50)
    # ngayHoc = models.ManyToManyField('NgayHoc',blank=True,null=True)
    # caHoc_id = models.ManyToManyField('CaHoc',blank=True,null=True)
    lichHoc = models.CharField(max_length=255, blank=True, null=True)
    hocPhi_ca = models.IntegerField(default=0)
    giaoVien_id = models.ForeignKey(GiaoVien, on_delete=models.SET_NULL, null=True)
    luongGV_ca = models.IntegerField()
    hocPhi_dot = models.IntegerField(default=0)
    luong_dot = models.IntegerField(default=0)
    traTheoKhoa = models.BooleanField(default=False)
    ngayBatDau = models.DateField(null=True,blank=True)
    ngayKetThuc = models.DateField(null=True,blank=True)
    soLuongHocVien = models.IntegerField(null=True,default=0)
    soLuongHocVienMax = models.IntegerField(null=True)
    duPhong1 = models.CharField(max_length=50,null=True,blank=True)
    duPhong2 = models.CharField(max_length=50,null=True, blank=True)
    create_at = models.DateField(null=True, blank=True, default=datetime.now())

    def __str__(self):
        return str(self.maLop)

    def to_json(self):
        return {
            'maLop': self.maLop,
            'tenLop': self.tenLop,
        }

class CaHoc(models.Model):
    gioBatDau = models.TimeField()
    gioKetThuc = models.TimeField()
    ca = models.CharField(max_length=2)
    ghiChu = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ca

class HOCVIEN_buoihoc(models.Model):
    hocVien_id = models.ForeignKey(HocVien, on_delete=models.SET_NULL, null=True)
    lopHoc_id = models.ForeignKey(LopHoc, on_delete=models.SET_NULL, null=True)
    diemDanhHV = models.BooleanField(default=False)
    ngay = models.DateField(blank=True,null=True)
    count = models.IntegerField(default=0,null=True,blank=True)
    ghiChu = models.TextField(blank=True)

    def __str__(self):
        return str(self.hocVien_id)

    def to_json(self):
        return {
            'hocVien_id': self.hocVien_id.maHV,
            'lopHoc_id': self.lopHoc_id.maLop,
            'diemDanhHV': self.diemDanhHV,
            'ngay': self.ngay,
            'ghiChu': self.ghiChu
        }

class HocVien_LopHoc(models.Model):
    lopHoc_id = models.ForeignKey(LopHoc, on_delete=models.CASCADE, null=True)
    hocVien_id = models.ForeignKey(HocVien, on_delete=models.CASCADE, null=True)
    hocPhiGiam = models.IntegerField(null=True,default=0,blank=True)
    count = models.IntegerField(default=0,null=True,blank=True)
    ghiChu = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.hocVien_id)

    def to_json(self):
        return {
            'hocVien_id': self.hocVien_id.maHV,
            'lopHoc_id': self.lopHoc_id.maLop,
            'hocPhiGiam': self.hocPhiGiam,
            'ghiChu': self.ghiChu
        }

class GIAOVIEN_buoihoc(models.Model):
    giaoVien_id = models.ForeignKey(GiaoVien, on_delete=models.SET_NULL, null=True)
    lopHoc_id = models.ForeignKey(LopHoc, on_delete=models.SET_NULL, null=True)
    diemDanhGV = models.BooleanField()
    ngay = models.DateField()
    ghiChu = models.TextField(blank=True)

    def __str__(self):
        return str(self.giaoVien_id)
    


class PhuHuynh(models.Model):
    maPH = models.CharField(max_length=50,primary_key=True)
    hocVien_id = models.ForeignKey(HocVien, on_delete=models.CASCADE, null=True)
    tenPH = models.CharField(max_length=50)
    gioiTinh = models.CharField(max_length=50,choices=[('nam', 'Nam'), ('nu', 'Nữ'), ('khac', 'Khác')], default='khac')
    ngaySinh = models.DateField(null=True, blank=True)
    sdt1 = models.CharField(max_length=50)
    sdt2 = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    soZalo = models.CharField(max_length=50)
    duPhong2 = models.CharField(max_length=50,blank=True) 
    duPhong3 = models.CharField(max_length=50,blank=True)
    duPhong4 = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.maPH


class HocPhi_HocVien(models.Model):
    hocVien_id = models.ForeignKey(HocVien, on_delete=models.SET_NULL, null=True)
    lopHoc_id = models.ForeignKey(LopHoc, on_delete=models.SET_NULL, null=True)
    hocPhi = models.IntegerField(default=0)
    ngayDangKy = models.DateField()
    ghiChu = models.TextField(blank=True)

    def __str__(self):
        return str(self.hocVien_id)

class DongTien_HocVien(models.Model):
    hocVien_id = models.ForeignKey(HocVien, on_delete=models.SET_NULL, null=True)
    ngay = models.DateField()
    soTienDong = models.IntegerField()
    ghiChu = models.TextField(blank=True)

    def __str__(self):
        return str(self.hocVien_id)

class LuongGV(models.Model):
    giaoVien_id = models.ForeignKey(GiaoVien, on_delete=models.SET_NULL, null=True)
    ngay = models.DateField()
    soTienNhan = models.IntegerField()
    ghiChu = models.TextField(blank=True)

    def __str__(self):
        return str(self.giaoVien_id)
class KhoaHoc(models.Model):
    maKH = models.CharField(max_length=50,primary_key=True)
    tenKH = models.CharField(max_length=50)
    moTa = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    ghiChu = models.TextField(blank=True)
    create_at = models.DateTimeField(default=datetime.now(), null=True, blank=True)

    def __str__(self):
        return self.maKH
class KhoanKhac(models.Model):
    maKK = models.CharField(max_length=50,primary_key=True)
    soTienChi = models.IntegerField()
    ngay = models.DateField()
    noiDungChi = models.CharField(max_length=255)
    soTienThu = models.IntegerField()
    noiDungThu = models.CharField(max_length=255)

    def __str__(self):
        return self.maKK

class Front_end(models.Model):
    slogan = models.CharField(max_length=255)
    slider = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    logo = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.slogan


class NgayHoc(models.Model):
    ngay = models.CharField(max_length=255,choices=[('Thứ 2', 'Thứ 2'),('Thứ 3', 'Thứ 3'),('Thứ4', 'Thứ 4'),('Thứ 5', 'Thứ 5'),('Thứ 6', 'Thứ 6'),('Thứ 7', 'Thứ 7'),('Chủ Nhật','Chủ Nhật')], default='Chủ Nhật')
    def __str__(self):
        return self.ngay


import re
 
from django.conf import settings
from django.contrib.auth.decorators import login_required
 
 
class RequireLoginMiddleware(object):
    """
    Middleware component that wraps the login_required decorator around
    matching URL patterns. To use, add the class to MIDDLEWARE_CLASSES and
    define LOGIN_REQUIRED_URLS and LOGIN_REQUIRED_URLS_EXCEPTIONS in your
    settings.py. For example:
    ------
    LOGIN_REQUIRED_URLS = (
        r'/topsecret/(.*)$',
    )
    LOGIN_REQUIRED_URLS_EXCEPTIONS = (
        r'/topsecret/login(.*)$',
        r'/topsecret/logout(.*)$',
    )
    ------
    LOGIN_REQUIRED_URLS is where you define URL patterns; each pattern must
    be a valid regex.
 
    LOGIN_REQUIRED_URLS_EXCEPTIONS is, conversely, where you explicitly
    define any exceptions (like login and logout URLs).
    """
    def __init__(self):
        self.required = tuple(re.compile(url) for url in settings.LOGIN_REQUIRED_URLS)
        self.exceptions = tuple(re.compile(url) for url in settings.LOGIN_REQUIRED_URLS_EXCEPTIONS)
 
    def process_view(self, request, view_func, view_args, view_kwargs):
        # No need to process URLs if user already logged in
        if request.user.is_authenticated():
            return None
 
        # An exception match should immediately return None
        for url in self.exceptions:
            if url.match(request.path):
                return None
 
        # Requests matching a restricted URL pattern are returned
        # wrapped with the login_required decorator
        for url in self.required:
            if url.match(request.path):
                return login_required(view_func)(request, *view_args, **view_kwargs)
 
        # Explicitly return None for all non-matching requests
        return None