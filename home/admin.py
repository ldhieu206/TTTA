from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class HocvienAdmin(admin.ModelAdmin):
    list_display = ['maHV','name','ngaySinh','phone']
    search_fields = ['maHV','name','phone']
admin.site.register(HocVien, HocvienAdmin)


class GiaovienAdmin(admin.ModelAdmin):
    list_display = ['maGV','tenGV','ngaySinh','sdt']
    search_fields = ['maGV','tenGV','sdt']
admin.site.register(GiaoVien, GiaovienAdmin)


class LophocAdmin(admin.ModelAdmin):
    list_display = ('maLop','tenLop','giaoVien_id','hocPhi_dot','traTheoKhoa','soLuongHocVien')
    search_fields = ['maLop','tenLop','hocPhi_ca','giaoVien_id','luongGV_ca','hocPhi_dot','luong_dot','traTheoKhoa']
admin.site.register(LopHoc, LophocAdmin)


class Hocvien_buoihocAdmin(admin.ModelAdmin):
    list_display = ['hocVien_id','lopHoc_id','diemDanhHV','ngay']
    search_fields = ['hocVien_id','lopHoc_id','diemDanhHV','ngay']
admin.site.register(HOCVIEN_buoihoc, Hocvien_buoihocAdmin)


class Giaovien_buoihocAdmin(admin.ModelAdmin):
    list_display = ['giaoVien_id','lopHoc_id','diemDanhGV','ngay']
    search_fields = ['giaoVien_id','lopHoc_id','diemDanhGV','ngay']
admin.site.register(GIAOVIEN_buoihoc, Giaovien_buoihocAdmin)


class PhuhuynhAdmin(admin.ModelAdmin):
    list_display = ['maPH','tenPH','sdt1','sdt2','email']
    search_fields = ['maPH','tenPH','sdt1','sdt2','email']
admin.site.register(PhuHuynh, PhuhuynhAdmin)


class Hocphi_HocvienAdmin(admin.ModelAdmin):
    list_display = ['hocVien_id','lopHoc_id','hocPhi','ngayDangKy']
    search_fields = ['hocVien_id','lopHoc_id','hocPhi','ngayDangKy']
admin.site.register(HocPhi_HocVien, Hocphi_HocvienAdmin)


class Dongtien_HocvienAdmin(admin.ModelAdmin):
    list_display = ['hocVien_id','soTienDong','ngay','ghiChu']
    search_fields = ['hocVien_id','soTienDong','ngay','ghiChu']
admin.site.register(DongTien_HocVien, Dongtien_HocvienAdmin)


class LuongGVAdmin(admin.ModelAdmin):
    list_display = ['giaoVien_id','ngay','soTienNhan','ghiChu']
    search_fields = ['giaoVien_id','ngay','soTienNhan','ghiChu']
admin.site.register(LuongGV, LuongGVAdmin)


class HocVien_LopHocAdmin(admin.ModelAdmin):
    list_display = ['hocVien_id','lopHoc_id']
    search_fields = ['hocVien_id','lopHoc_id']
admin.site.register(HocVien_LopHoc, HocVien_LopHocAdmin)


class KhoaHocAdmin(admin.ModelAdmin):
    list_display = ['maKH','tenKH','ghiChu']
    search_fields = ['maKH','tenKH','ghiChu']
admin.site.register(KhoaHoc, KhoaHocAdmin)


class KhoanKhacAdmin(admin.ModelAdmin):
    list_display = ['maKK','soTienChi','soTienThu']
    search_fields = ['maKK','soTienChi','soTienThu']
admin.site.register(KhoanKhac, KhoanKhacAdmin)


class Front_endAdmin(admin.ModelAdmin):
    list_display = ['slogan']
    search_fields = ['slogan']
admin.site.register(Front_end, Front_endAdmin)
