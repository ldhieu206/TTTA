from calendar import month
from cmath import e
import email
from gettext import ngettext
from inspect import trace
from re import L, M, U
import re
from sre_constants import RANGE
from tkinter import N
from xml.dom import UserDataHandler
from django.shortcuts import render

# Create your views here.
from mailer import Mailer
from django.shortcuts import render
import datetime
# Create your views here.
from unicodedata import name
from django.shortcuts import render
from django.http.response import *
from django.http import *
from django.shortcuts import redirect
from .models import *
import hashlib
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
 

# Create your views here.
@login_required
def indexAdmin(request):
    data = {
        'dsHocVien': HocVien.objects.all().count(),
        'dsGiaoVien': GiaoVien.objects.all().count(),
        'dsLopHoc': LopHoc.objects.all().count(),
        'dsKhoaHoc':KhoaHoc.objects.all().count(),
    }
    return render(request, 'home/admin/indexAdmin.html',data)
def index(request):

    return render(request, 'home/index.html')


def indexGV(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except KeyError:
        return redirect('/loginGV')
    data = {
        'giaoVien': giaoVien,
    }
    return render(request, 'home/giaoVien/indexGV.html',data)


def indexHV(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except KeyError:
        return redirect('/login')
    data = {
        'hocVien': hocVien,
    }
    return render(request, 'home/hocVien/indexHV.html',data)


def login(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
        return redirect('/indexHV')
    except:
        pass

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        from django.db.models import Q
        try:
            hocVien = HocVien.objects.get(Q(maHV=username,password=password) | Q(phone=username,password=password) | Q(email=username,password=password))
            request.session['hocVien'] = hocVien.maHV
            return redirect('/indexHV')
        except HocVien.DoesNotExist:
            return render(request, 'home/hocVien/login.html', {'result': 'incorrect', 'maHV': maHV})
    return render(request, 'home/hocVien/login.html', {'result': None})



def loginGV(request):
    try:
        maGV = request.session['giaoVien']
        return redirect('/indexGV')
    except KeyError:
        pass
    if request.method == 'POST':
        from django.db.models import Q
        username = request.POST['username']
        password = request.POST['password']
        try:
            giaoVien = GiaoVien.objects.get(Q(maGV=username) | Q(sdt=username) | Q(email=username),password=password)
            request.session['giaoVien'] = giaoVien.maGV
            return redirect('/indexGV')
        except GiaoVien.DoesNotExist:
            return render(request, 'home/giaoVien/loginGV.html', {'result': 'incorrect', 'maGV': maGV})
    return render(request, 'home/giaoVien/loginGV.html', {'result': None})


def logout(request):
    try:
        del request.session['hocVien']
    except KeyError:
        pass
    return redirect('/')


def logoutGV(request):
    try:
        del request.session['giaoVien']
    except KeyError:
        pass
    return redirect('/')



def account(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except KeyError:
        return redirect('/login')
    lopHocs = [x.lopHoc_id for x in HocVien_LopHoc.objects.filter(
        hocVien_id=hocVien.maHV)]
    phuHuynhs = PhuHuynh.objects.get(hocVien_id=maHV)
    hocPhis =  HocPhi_HocVien.objects.filter(hocVien_id= hocVien.maHV)
    data = {
        'hocVien': hocVien,
        'lopHocs': lopHocs,
        'phuHuynhs': phuHuynhs,
        'hocPhis': hocPhis,
    }
    return render(request, 'home/hocVien/account.html', data)




def accountGV(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except KeyError:
        return redirect('/loginGV')
    lopHocs = LopHoc.objects.filter(giaoVien_id=giaoVien.maGV)
    luongGVs = LuongGV.objects.filter(giaoVien_id=giaoVien.maGV)
    data = {
        'giaoVien': giaoVien,
        'lopHocs': lopHocs,
        'luongGVs': luongGVs
    }
    return render(request, 'home/giaoVien/accountGV.html', data)



def dsGiaoVien(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except KeyError:
        return redirect('/loginGV')
    Data = {'dsGiaoViens': GiaoVien.objects.all()}
    return render(request, 'home/giaoVien/dsGiaoVien.html', Data)


def dsHocVien(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except KeyError:
        return redirect('/loginGV')
    Data = {'dsHocViens': HocVien.objects.all()}
    return render(request, 'home/giaoVien/dsHocVien.html', Data)
@login_required
def dsHocVienAdmin(request):
    Data = {'dsHocViens': HocVien.objects.all().order_by('-create_at')}
    return render(request, 'home/admin/dsHocVien.html', Data)



def dsLopHocHV(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except KeyError:
        return redirect('/login')
    Data = {
        'dsLopHoc': LopHoc.objects.all().order_by('maLop'),
        'range7':list(range(7)),
        'range8':list(range(1,9)),
        'range56':list(range(56)),
        }
    if request.method == 'POST':
        maLop = request.POST['maLop']
        lopHoc = LopHoc.objects.get(maLop=maLop)
        dslh = {}
        for lh in lopHoc.lichHoc.split(','):
            dslh[int(lh)] = lopHoc.tenLop
        data = {
            'dslh':dslh,
            }
        print(dslh)
        return JsonResponse({
            'status': 'success',
            'data': data,
        })

    return render(request, 'home/hocVien/dsLopHocHV.html', Data)

def dsLopHoc(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except KeyError:
        return redirect('/loginGV')
    Data = {
        'dsLopHocs': LopHoc.objects.filter(giaoVien_id=giaoVien).order_by('maLop'),
        'range7':list(range(7)),
        'range8':list(range(1,9)),
        'range56':list(range(56)),
        }
    if request.method == 'POST':
        maLop = request.POST['maLop']
        lopHoc = LopHoc.objects.get(maLop=maLop)
        dslh = {}
        for lh in lopHoc.lichHoc.split(','):
            dslh[int(lh)] = lopHoc.tenLop
        data = {
            'dslh':dslh,
            }
        print(dslh)
        return JsonResponse({
            'status': 'success',
            'data': data,
        })
    return render(request, 'home/giaoVien/dsLopHoc.html', Data)


@login_required
def dsLopHocAdmin(request):
    data = {
        'dsLopHocs': LopHoc.objects.all().order_by('create_at'),
        'range7':list(range(7)),
        'range8':list(range(1,9)),
        'range56':list(range(56)),
    }
    if request.method == 'POST':
        maLop = request.POST['maLop']
        lopHoc = LopHoc.objects.get(maLop=maLop)
        dslh = {}
        for lh in lopHoc.lichHoc.split(','):
            dslh[int(lh)] = lopHoc.tenLop
        Data = {
            'dslh':dslh,
            }
        print(dslh.count())
        return JsonResponse({
            'status': 'success',
            'data': Data,
        })
    return render(request, 'home/admin/dsLopHoc.html',data)
@login_required
def dsGiaoVienAdmin(request):
    Data = {'dsGiaoViens': GiaoVien.objects.all().order_by('create_at')}
    return render(request, 'home/admin/dsGiaoVien.html', Data)

@login_required
def dsKhoaHoc(request):    
    Data = {'dsKhoaHocs': KhoaHoc.objects.all().order_by('create_at')}
    return render(request, 'home/admin/dsKhoaHoc.html', Data)

def dsHocVienLop(request,maLop):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except KeyError:
        return redirect('/loginGV')
    from datetime import datetime 
    data={
        'dsHocVien':HocVien_LopHoc.objects.filter(lopHoc_id=maLop),
        'dshv':[x.hocVien_id for x in HocVien_LopHoc.objects.filter(lopHoc_id=maLop)],
        'list_lophoc':LopHoc.objects.all(),
        'lopHoc':LopHoc.objects.get(maLop=maLop),
        'data': [
            1 if 
            HOCVIEN_buoihoc.objects.filter(
                lopHoc_id=maLop,
                hocVien_id=hv_lh.hocVien_id,
                ngay=datetime.now().date()
            ).exists() 
            else 0 
            for hv_lh in HocVien_LopHoc.objects.filter(lopHoc_id=maLop)
        ],
    }
    return render(request, 'home/giaoVien/dsHocVienLop.html', data)


def hienThiThongTinLopHoc(request, maLop):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except KeyError:
        return redirect('/login')
    Data = {'hienThiThongTinLopHocs': LopHoc.objects.filter(maLop=maLop)}
    return render(request, 'home/hocVien/hienThiThongTinLopHoc.html', Data)



def hienThiThongTinPhuHuynh(request, hocVien_id):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV = maGV)
    except KeyError:
        return redirect('/login')
    hocPhi = HocPhi_HocVien.objects.filter(hocVien_id=hocVien_id)
    phuHuynh = PhuHuynh.objects.filter(hocVien_id=hocVien_id)
    dsLopHoc = [x.lopHoc_id for x in HocVien_LopHoc.objects.filter(hocVien_id=hocVien_id)]
    dthv = DongTien_HocVien.objects.filter(hocVien_id=hocVien_id)
    dslh = {}
    for lopHoc in dsLopHoc:
        for lh in lopHoc.lichHoc.split(','):
            dslh[int(lh)] = lopHoc.maLop
    hp = 0
    for i in hocPhi:
        hp += i.hocPhi
    tongTienDong = 0
    for i in dthv:
        tongTienDong += i.soTienDong
    print(tongTienDong,hp)
    data = {
        'tongTienDong': tongTienDong,
        'hp': hp,
        'dthv':dthv,
        'hocPhi': hocPhi,
        'phuHuynh': phuHuynh,
        'dslh':dslh.items(),
        'range7':list(range(7)),
        'range8':list(range(1,9)),
        'range56':list(range(56)),
    }
    return render(request, 'home/giaoVien/hienThiThongTinPhuHuynh.html', data)

@login_required
def hienThiThongTinPhuHuynhAdmin(request, hocVien_id):    
    hocPhi = HocPhi_HocVien.objects.filter(hocVien_id=hocVien_id)
    phuHuynh = PhuHuynh.objects.filter(hocVien_id=hocVien_id)
    dsLopHoc = [x.lopHoc_id for x in HocVien_LopHoc.objects.filter(hocVien_id=hocVien_id)]
    dthv = DongTien_HocVien.objects.filter(hocVien_id=hocVien_id)
    dslh = {}
    for lopHoc in dsLopHoc:
        for lh in lopHoc.lichHoc.split(','):
            dslh[int(lh)] = lopHoc.maLop
    hp = 0
    for i in hocPhi:
        hp += i.hocPhi
    tongTienDong = 0
    for i in dthv:
        tongTienDong += i.soTienDong
    print(tongTienDong,hp)
    data = {
        'tongTienDong': tongTienDong,
        'hp': hp,
        'dthv':dthv,
        'hocPhi': hocPhi,
        'phuHuynh': phuHuynh,
        'dslh':dslh.items(),
        'range7':list(range(7)),
        'range8':list(range(1,9)),
        'range56':list(range(56)),
    }
    return render(request, 'home/admin/hienThiThongTinPhuHuynh.html', data)


# jsonresponse
from django.http import JsonResponse
def send_email(request):
    if request.method == 'POST':
        maHV = request.POST['maHV']
        tongTien = request.POST['tongTien']
        tongDaDong = request.POST['tongDaDong']
        hocVien = HocVien.objects.get(maHV=maHV)
        phuHuynh = PhuHuynh.objects.get(hocVien_id=maHV)

        receiver = phuHuynh.email
        sender = 'lehieu206201@gmail.com'
        password = 'usposcbumclsqebo'
        sender_name = 'ECenter'
        subject = 'Thông Báo Của ECenter'
        message = f"""
        <html>
            <head></head>
            <body style="font-size: 16px">
                <p>Học Viên: <b>{hocVien.name}</b>.</p>
                <p>Phụ Huynh: <b>{phuHuynh.tenPH}</b>.</p>
                <p>Học Phí: <b>{tongTien}</b>.</p>
                <p>Tổng tiễn đã đóng: <b>{tongDaDong}</b>.</p>
                <br>
                <p>Mọi thắc mắc vui lòng liên hệ: 0352998850<b>
            </body>
        </html>
        """

        mail = Mailer(email=sender, password=password)
        mail.settings(provider=mail.GMAIL)
        mail.send(sender_name=sender_name, receiver=receiver,
                subject=subject, message=message)
        return JsonResponse({
            "success": True,
            "message": "Email đã được gửi"
        })
        pass
    else:
        return JsonResponse({
            'success': False,
            'message': 'Method not allowed'
        })
def dangKyHoc(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except KeyError:
        pass
    dsLopHoc = [x.lopHoc_id for x in HocVien_LopHoc.objects.filter(hocVien_id=hocVien)]
    phuHuynh_id = PhuHuynh.objects.get(hocVien_id=maHV)
    if request.method == 'POST':
        lopHoc_id = request.POST['maLop']
        lopHoc_id = LopHoc.objects.get(maLop=lopHoc_id)
        hocVien_id = HocVien.objects.get(maHV= maHV)
        ngay = datetime.now()
        dsLH = LopHoc.objects.filter(maLop = lopHoc_id)
        print(dsLH,"############")
        for x in dsLH:
            for y in x.lichHoc.split(','):
                for lopHoc in dsLopHoc:
                    for lh in lopHoc.lichHoc.split(','):
                        if y == lh:
                            return JsonResponse({
                                "success": False,
                                "message": "Lịch học trùng với lịch học của lớp học khác"
                            })
        try:
            if HocVien_LopHoc.objects.get(hocVien_id=hocVien_id, lopHoc_id=lopHoc_id):
                return JsonResponse({
                    "success": False,
                    "message": "Đã đăng ký lớp này rồi."
                }) 
            
        except HocVien_LopHoc.DoesNotExist:
            if lopHoc_id.soLuongHocVien >= lopHoc_id.soLuongHocVienMax:
                return JsonResponse({
                    "success": False,
                    "message": "Lớp đã đầy."
                })
            
            HocVien_LopHoc.objects.create(hocVien_id=hocVien_id, lopHoc_id=lopHoc_id)
            if lopHoc_id.traTheoKhoa == True:
                HocPhi_HocVien.objects.create(hocVien_id=hocVien_id,lopHoc_id=lopHoc_id , ngayDangKy=ngay, hocPhi=lopHoc_id.hocPhi_dot)
            else:
                HocPhi_HocVien.objects.create(hocVien_id=hocVien_id,lopHoc_id=lopHoc_id , ngayDangKy=ngay, hocPhi=lopHoc_id.hocPhi_ca)
            lopHoc_id.soLuongHocVien += 1
            lopHoc_id.save()
            return JsonResponse({
                "success": True,
                "message": "Đăng ký thành công"
            })


def diemDanh(request):
    if request.method == 'POST':
        lopHoc_id = request.POST['lopHoc_id']
        lopHoc_id = LopHoc.objects.get(maLop=lopHoc_id)
        hocVien_id = request.POST['hocVien_id']
        hocVien_id = HocVien.objects.get(maHV=hocVien_id)
        hv = HocVien_LopHoc.objects.get(hocVien_id=hocVien_id, lopHoc_id=lopHoc_id)
        print(hv.count,"############")
        print(hocVien_id)
        ngay = datetime.now()

        try:
            if HOCVIEN_buoihoc.objects.get(hocVien_id=hocVien_id,ngay=ngay,lopHoc_id=lopHoc_id):
                return JsonResponse({
                    "success": False,
                    "message": "Đã điểm danh rồi.",
                })
            hvbh = HOCVIEN_buoihoc.objects.create( lopHoc_id=lopHoc_id,hocVien_id=hocVien_id,ngay= ngay, diemDanhHV=True)
            hvbh.count += 1
            hvbh.save()
            hv.count += 1
            hv.save()  
            return JsonResponse({
                "success": True,
                "message": "Điểm danh thành công"
            })
        except HOCVIEN_buoihoc.DoesNotExist:
            HOCVIEN_buoihoc.objects.create( lopHoc_id=lopHoc_id,hocVien_id=hocVien_id,ngay= ngay, diemDanhHV=True)
            hv.count += 1
            hv.save()
            return JsonResponse({
                "success": True,
                "message": "Điểm danh thành công"
            })
    return JsonResponse({
        "success": False,
        "message": "Điểm danh không thành công",
    })

import xlwt
def export_excel(request):
    if request.method == 'POST':
        lopHoc_id = request.POST['lopHoc_id']
        ngay = request.POST['ngay']
        hvbh = HOCVIEN_buoihoc.objects.filter(lopHoc_id = lopHoc_id,ngay = ngay)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=HocVienBuoiHoc' +\
            str(ngay) + '.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('HocVienBuoiHoc')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['Mã Lớp','Mã Học Viên','Điểm Danh']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle()
        rows = hvbh.values_list('lopHoc_id','hocVien_id','diemDanhHV')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        wb.save(response)
        return response


@login_required
def addLopHoc(request):
    data = {
        'dsLopHoc':LopHoc.objects.all(),
        'dsGiaoVien':GiaoVien.objects.all(),
        'range56':list(range(56)),
        'range7':list(range(7)),
        'range8':list(range(1,9)),
    }
    if request.method == 'POST':
        dslh = request.POST['dslh']
        maLop = request.POST['maLop']
        tenLop = request.POST['tenLop']
        giaoVien_id = request.POST['giaoVien_id']
        hocPhi_ca = request.POST['hocPhi_ca']
        ngayBatDau = request.POST['ngayBatDau']
        ngayKetThuc = request.POST['ngayKetThuc']
        traTheoKhoa = True if request.POST['traTheoKhoa'] == 'true' else False
        soLuongHocVienMax = request.POST['soLuongHocVienMax']
        hocPhi_dot = request.POST['hocPhi_dot']
        luongGV_ca = request.POST['luongGV_ca']
        gv = GiaoVien.objects.get(maGV=giaoVien_id)
        # dsLopHoc = LopHoc.objects.filter(giaoVien_id=giaoVien_id)
        dsLH = LopHoc.objects.filter(giaoVien_id=gv)

        try:

            lh = []
            for x in dslh.split(','):
                lh.append(int(x))
            for ds in dsLH:
                for d in ds.lichHoc.split(','):
                    if int(d) in lh:
                        return JsonResponse({
                            "success": False,
                            "message": "Giáo viên trùng lịch dạy!"
                        })
                        
            LopHoc.objects.get(maLop=maLop)
            return JsonResponse({
                "success": False,
                "message": "Lớp đã tồn tại"
            })
        except LopHoc.DoesNotExist:
            if ngayBatDau > ngayKetThuc:
                return JsonResponse({
                    "success": False,
                    "message": "Ngày bắt đầu phải trước ngày kết thúc"
                })
            
            LopHoc.objects.create(
                maLop=maLop,
                tenLop=tenLop,
                giaoVien_id=gv,
                hocPhi_ca=hocPhi_ca,
                ngayBatDau=ngayBatDau,
                ngayKetThuc=ngayKetThuc,
                traTheoKhoa=traTheoKhoa,
                soLuongHocVienMax=soLuongHocVienMax,
                hocPhi_dot=hocPhi_dot,
                luongGV_ca=luongGV_ca,
                lichHoc = str(dslh)
            )

            return JsonResponse({
                "success": True,
                "message": "Thêm lớp thành công"
            })
    return render(request, 'home/admin/addLopHoc.html',data)

@login_required
def addHocVien(request):
    if request.method == 'POST':
        maHV = request.POST['maHV']
        name = request.POST['name']
        gioiTinh = request.POST['gioiTinh']
        ngaySinh = request.POST['ngaySinh']
        phone = request.POST['phone']
        email = request.POST['email']
        diaChi = request.POST['diaChi']
        try:
            HocVien.objects.get(maHV=maHV)
            return JsonResponse({
                "success": False,
                "message": "Học viên đã tồn tại"
            })
        except HocVien.DoesNotExist:
            HocVien.objects.create(
                maHV=maHV,
                name=name,
                gioiTinh=gioiTinh,
                ngaySinh=ngaySinh,
                phone=phone,
                email=email,
                diaChi=diaChi
            )
            return JsonResponse({
                "success": True,
                "message": "Thêm học viên thành công"
            })
    return render(request, 'home/admin/addHocVien.html')
@login_required
def addPhuHuynh(request,maHV):
    data = {
        'maHV':maHV,
        'hocVien':HocVien.objects.get(maHV=maHV),
    }
    if request.method == 'POST':
        maPH = request.POST['maPH']
        tenPH = request.POST['tenPH']
        gioiTinh = request.POST['gioiTinh']
        ngaySinh = request.POST['ngaySinh']
        sdt1 = request.POST['sdt1']
        email = request.POST['email']
        soZalo = request.POST['soZalo']
        hv = HocVien.objects.get(maHV=maHV)
        try:
            PhuHuynh.objects.get(maPH=maPH)
            return JsonResponse({
                "errors": True,
                "message": "Phụ huynh đã tồn tại"
            })
        except PhuHuynh.DoesNotExist:
            PhuHuynh.objects.create(
                maPH=maPH,
                tenPH=tenPH,
                gioiTinh=gioiTinh,
                ngaySinh=ngaySinh,
                sdt1=sdt1,
                email=email,
                soZalo=soZalo,
                hocVien_id=hv
            )
            return JsonResponse({
                "success": True,
                "message": "Thêm phụ huynh thành công"
            })
        
    return render(request, 'home/admin/addPhuHuynh.html',data)
@login_required
def addGiaoVien(request):
    if request.method == 'POST':
        maGV = request.POST['maGV']
        tenGV = request.POST['tenGV']
        gioiTinh = request.POST['gioiTinh']
        ngaySinh = request.POST['ngaySinh']
        sdt = request.POST['sdt']
        email = request.POST['email']
        password = request.POST['password']
        luongNgay = request.POST['luongNgay']
        try:
            GiaoVien.objects.get(maGV=maGV)
            return JsonResponse({
                "success": False,
                "message": "Giáo viên đã tồn tại"
            })
        except GiaoVien.DoesNotExist:
            GiaoVien.objects.create(maGV=maGV, tenGV=tenGV, gioiTinh=gioiTinh, ngaySinh=ngaySinh, sdt=sdt, email=email, password=password, luongNgay=luongNgay)
            return JsonResponse({
                "success": True,
                "message": "Thêm giáo viên thành công",
            })
    return render(request, 'home/admin/addGiaoVien.html')


import json

def lichHoc(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except:
        return redirect('/login')
    dsLopHoc = [x.lopHoc_id for x in HocVien_LopHoc.objects.filter(hocVien_id=hocVien)]
    dslh = {}
    for lopHoc in dsLopHoc:
        for lh in lopHoc.lichHoc.split(','):
            dslh[int(lh)] = lopHoc.tenLop
    
    data = {
        'dsLopHoc': dsLopHoc,
        'dslh':dslh.items(),
        'range7':list(range(7)),
        'range8':list(range(1,9)),
        'range56':list(range(56)),
    }
    print(dslh.items() ,"#################")
    return render(request, 'home/hocVien/lichHoc.html',data)

def lichDay(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except:
        return redirect('/')
    # dsLopHoc = [x.maLop for x in LopHoc.objects.filter(giaoVien_id=maGV)]
    dsLopHoc = LopHoc.objects.filter(giaoVien_id=maGV)
    print(dsLopHoc)
    dslh = {}
    for lopHoc in dsLopHoc:
        print(lopHoc.lichHoc)
        for lh in lopHoc.lichHoc.split(','):
            dslh[int(lh)] = lopHoc.tenLop
    data = {
        'dsLopHoc': dsLopHoc,
        'dslh':dslh.items(),
        'range7':list(range(7)),
        'range8':list(range(1,9)),
        'range56':list(range(56)),
    }
    return render(request, 'home/giaoVien/lichDay.html',data)
@login_required
def thongKe(request):
    hocPhiHV = DongTien_HocVien.objects.all()
    luongGV = LuongGV.objects.all()
    z = HocVien.objects.all().count()
    chi = 0;
    thu= 0;
    thuNhap = 0;
    soTienHVConNo = 0;
    for i in luongGV:
        chi += i.soTienNhan
    for k in hocPhiHV:
        thu += k.soTienDong
    thuNhap = thu + soTienHVConNo - chi
    data = {
        'z':z,
        'range': list(range(1,z+1)),
        'hocPhiHV':hocPhiHV,
        'thu':thu,
        'chi':chi,
        'luongGV':luongGV,
        'soTienHVConNo':soTienHVConNo,
        'thuNhap':thuNhap,
    }
    return render(request, 'home/admin/thongKe.html',data)

def searchThongKe(request):
    data = {
        'hphv': DongTien_HocVien.objects.all(),
        'lgv': LuongGV.objects.all(),
    }
    if request.method == 'POST':
        bd = request.POST['bd']
        kt = request.POST['kt']
        print(bd,kt)
        if request.POST['type'] == 'hocPhiHV':
            data['hocPhiHV'] = DongTien_HocVien.objects.filter(ngay__range=[bd,kt])
        elif request.POST['type'] == 'luongGV':
            data['luongGV'] = LuongGV.objects.filter(ngay__range=(bd,kt))
        elif request.POST['type'] == 'tatCa':
            data['hocPhiHV'] = DongTien_HocVien.objects.filter(ngay__range=(bd,kt))
            data['luongGV'] = LuongGV.objects.filter(ngay__range=(bd,kt))

    return render(request, 'home/admin/searchThongKe.html',data)

import datetime as dt
from .resources import HocVienResource
from django.contrib import messages
from tablib import Dataset

def import_excel(request):              
    if request.method == 'POST' and request.FILES['myfile']:
        hocVien_resource = HocVienResource()
        dataset = Dataset()
        new_hocVien = request.FILES['myfile']

        if not new_hocVien.name.endswith('.xlsx'):
            messages.error(request, 'File không đúng định dạng')
            return redirect('home/admin/importexcel.html')
        imported_data = dataset.load(new_hocVien.read(),format='xlsx')
        for i in imported_data:
            value = HocVien(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4],
                i[5],
                i[6],
                i[7],
            )
            value.save()
    return render(request, 'home/admin/importexcel.html')
@login_required
def deleteHocVien(request):
    if request.method == 'POST':
        maHV = request.POST['maHV']
        print(maHV)
        HocVien.objects.get(maHV=maHV).delete()
        return JsonResponse({
            "success": True,
            "message": "Xóa học viên thành công",
        })

@login_required
def deleteGiaoVien(request):
    if request.method == 'POST':
        maGV = request.POST['maGV']
        print(maGV) 
        giaoVien = GiaoVien.objects.get(maGV=maGV)
        print(giaoVien)
        giaoVien.delete()
        return JsonResponse({
            "success": True,
            "message": "Xóa giáo viên thành công",
        })
@login_required
def deleteLopHoc(request):
    if request.method == 'POST':
        maLop = request.POST['maLop']
        print(maLop,"##############################")
        lopHoc = LopHoc.objects.get(maLop=maLop)
        lopHoc.delete()
        return JsonResponse({
            "success": True,
            "message": "Xóa lớp học thành công",
        })

@login_required
def editHocVien(request,maHV):
    data={
        'hocVien':HocVien.objects.get(maHV=maHV),
    }
    if request.method == 'POST':
        maHV = request.POST['maHV']
        hocVien = HocVien.objects.get(maHV=maHV)
        hocVien.name = request.POST['name']
        hocVien.ngaySinh = request.POST['ngaySinh']
        hocVien.gioiTinh = request.POST['gioiTinh']
        hocVien.diaChi = request.POST['diaChi']
        hocVien.email = request.POST['email']
        hocVien.phone = request.POST['phone']
        hocVien.password = request.POST['password']
        hocVien.save()
        return JsonResponse({
            "success": True,
            "message": "Sửa học viên thành công",
        })

    return render(request, 'home/admin/editHocVien.html',data)
@login_required
def editGiaoVien(request,maGV):
    data={
        'giaoVien':GiaoVien.objects.get(maGV=maGV),
    }
    if request.method == 'POST':
        maGV = request.POST['maGV']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
        giaoVien.tenGV = request.POST['tenGV']
        giaoVien.ngaySinh = request.POST['ngaySinh']
        giaoVien.gioiTinh = request.POST['gioiTinh']
        giaoVien.diaChi = request.POST['diaChi']
        giaoVien.email = request.POST['email']
        giaoVien.sdt = request.POST['sdt']
        giaoVien.password = request.POST['password']
        giaoVien.luongNgay = request.POST['luongNgay']
        giaoVien.save()
        return JsonResponse({
            "success": True,
            "message": "Sửa giáo viên thành công",
        })
    return render(request, 'home/admin/editGiaoVien.html',data)
@login_required
def editPhuHuynh(request,maPH):
    data={
        'phuHuynh':PhuHuynh.objects.get(maPH=maPH),
    }
    if request.method == 'POST':
        maPH = request.POST['maPH']
        phuHuynh = PhuHuynh.objects.get(maPH=maPH)
        phuHuynh.tenPH = request.POST['tenPH']
        phuHuynh.ngaySinh = request.POST['ngaySinh']
        phuHuynh.gioiTinh = request.POST['gioiTinh']
        phuHuynh.email = request.POST['email']
        phuHuynh.sdt1 = request.POST['sdt1']
        phuHuynh.soZalo = request.POST['soZalo']
        phuHuynh.save()
        return JsonResponse({
            "success": True,
            "message": "Sửa phụ huynh thành công",
        })
    return render(request, 'home/admin/editPhuHuynh.html',data)

@login_required
def editLopHoc(request,maLop):
    lopHoc = LopHoc.objects.get(maLop=maLop)
    dslh = {}
    for lh in lopHoc.lichHoc.split(','):
        dslh[int(lh)] = lopHoc.maLop

    print(dslh)
    data={
        # 'dsLopHoc' : [x.lopHoc_id for x in HocVien_LopHoc.objects.filter(hocVien_id=hocVien)],
        'lopHoc':lopHoc,
        'dsGiaoVien':GiaoVien.objects.all(),
        'range7':list(range(7)),
        'range8':list(range(1,9)),
        'range56':list(range(56)),
        'dslh': dslh.items(),
    }
    print(dslh.items() ,"#################")
    if request.method == 'POST':
        maLop = request.POST['maLop']
        lopHoc = LopHoc.objects.get(maLop=maLop)
        tenLop = request.POST['tenLop']
        giaoVien_id = request.POST['giaoVien_id']
        gv= GiaoVien.objects.get(maGV=giaoVien_id)
        dslh = request.POST['dslh']
        luongGV_ca = request.POST['luongGV_ca']
        hocPhi_ca = request.POST['hocPhi_ca']
        hocPhi_dot = request.POST['hocPhi_dot']
        ngayBatDau = request.POST['ngayBatDau']
        ngayKetThuc = request.POST['ngayKetThuc']
        soLuongHocVienMax = request.POST['soLuongHocVienMax']
        dsLH = LopHoc.objects.filter(giaoVien_id=gv) & LopHoc.objects.exclude(maLop=maLop)
        lopHoc= LopHoc.objects.get(maLop=maLop)
        try:
            lh = []
            for x in dslh.split(','):
                lh.append(int(x))
            for ds in dsLH:
                for d in ds.lichHoc.split(','):
                    if int(d) in lh:
                        return JsonResponse({
                            "success": False,
                            "message": "Giáo viên trùng lịch dạy!"
                        })
            lopHoc.maLop = maLop
            lopHoc.tenLop = tenLop
            lopHoc.giaoVien_id = gv
            lopHoc.lichHoc = str(dslh)
            lopHoc.luongGV_ca = luongGV_ca
            lopHoc.hocPhi_ca = hocPhi_ca
            lopHoc.hocPhi_dot = hocPhi_dot
            lopHoc.ngayBatDau = ngayBatDau
            lopHoc.ngayKetThuc = ngayKetThuc
            lopHoc.soLuongHocVienMax = soLuongHocVienMax
            lopHoc.save()
            return JsonResponse({
                "success": True,
                "message": "Sửa lớp học thành công",
            })
        except:
            return JsonResponse({
                "success": False,
                "message": "Sửa lớp học thất bại",
            })
    return render(request, 'home/admin/editLopHoc.html',data)



from django.contrib.auth.models import User
@login_required
def addAdmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            return JsonResponse({
                "success": True,
                "message": "Thêm admin thành công",
            })
        except:
            if User.username == username:
                return JsonResponse({
                    "success": False,
                    "message": "Tên đăng nhập đã tồn tại",
                })

    return render(request, 'home/admin/addAdmin.html')

@login_required
def dsAdmin(request):
    data={
        'dsAdmin':User.objects.all(),
    }
    return render(request, 'home/admin/dsAdmin.html',data)
@login_required
def deleteAdmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = User.objects.get(username=username)
        user.delete()
        return JsonResponse({
            "success": True,
            "message": "Xóa admin thành công",
        })
@login_required
def lopHocGV(request,maGV):
    dsLopHoc = LopHoc.objects.filter(giaoVien_id=maGV)
    print(dsLopHoc)
    dslh = {}
    for lopHoc in dsLopHoc:
        print(lopHoc.lichHoc)
        for lh in lopHoc.lichHoc.split(','):
            dslh[int(lh)] = lopHoc.tenLop
    data={
        'dsLopHoc':LopHoc.objects.filter(giaoVien_id=maGV),
        'dslh':dslh.items(),
        'range7':list(range(7)),
        'range8':list(range(1,9)),
        'range56':list(range(56)),
    }
    return render(request, 'home/admin/lopHocGV.html',data)
@login_required
def hocVienLopAdmin(request,maLop):

    from datetime import datetime 
    data={
        'dsHocVien':HocVien_LopHoc.objects.filter(lopHoc_id=maLop),
        'dshv':[x.hocVien_id for x in HocVien_LopHoc.objects.filter(lopHoc_id=maLop)],
        'list_lophoc':LopHoc.objects.all(),
        'lopHoc':LopHoc.objects.get(maLop=maLop),
        'data': [
            1 if 
            HOCVIEN_buoihoc.objects.filter(
                lopHoc_id=maLop,
                hocVien_id=hv_lh.hocVien_id,
                ngay=datetime.now().date()
            ).exists() 
            else 0 
            for hv_lh in HocVien_LopHoc.objects.filter(lopHoc_id=maLop)
        ],
    }
    return render(request, 'home/admin/hocVienLop.html',data)

@login_required
def deleteKhoaHoc(request):
    if request.method == 'POST':
        maKH = request.POST['maKH']
        khoaHoc = KhoaHoc.objects.get(maKH=maKH)
        khoaHoc.delete()
        return JsonResponse({
            "success": True,
            "message": "Xóa khóa học thành công",
        })

from django.core.files.storage import FileSystemStorage
@login_required
def addKhoaHoc(request):
    if request.method == 'POST':
        maKH = request.POST['maKH']
        tenKH = request.POST['tenKH']
        moTa = request.POST['moTa']
        img = request.FILES['img']
        ghiChu = request.POST['ghiChu']
        print(maKH,"################")
        try:
            KhoaHoc.objects.get(maKH=maKH)
            return JsonResponse({
                "success": False,
                "message": "Mã khóa học đã tồn tại",
            })
        except:
            KhoaHoc.objects.create(maKH=maKH,tenKH=tenKH,moTa=moTa,ghiChu=ghiChu,img = img)
            return JsonResponse({
                "success": True,
                "message": "Thêm khóa học thành công",
            })
    return render(request, 'home/admin/addKhoaHoc.html')
@login_required
def editKhoaHoc(request,maKH):
    data={
        'khoaHoc':KhoaHoc.objects.get(maKH=maKH),
        'dsKhoaHoc':KhoaHoc.objects.all(),
    }
    if request.method == 'POST':
        maKH = request.POST['maKH']
        khoaHoc = KhoaHoc.objects.get(maKH=maKH)
        khoaHoc.tenKH = request.POST['tenKH']
        khoaHoc.img = request.FILES['img']
        khoaHoc.ghiChu = request.POST['ghiChu']
        khoaHoc.moTa = request.POST['moTa']
        khoaHoc.save()
        return JsonResponse({
            "success": True,
            "message": "Sửa khóa học thành công",
        })
    return render(request, 'home/admin/editKhoaHoc.html',data)

def editHV(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except:
        return redirect('/')
    data={
        'hocVien':hocVien,
    }
    if request.method == 'POST':
        hocVien.name = request.POST['name']
        hocVien.ngaySinh = request.POST['ngaySinh']
        hocVien.gioiTinh = request.POST['gioiTinh']
        hocVien.diaChi = request.POST['diaChi']
        hocVien.email = request.POST['email']
        hocVien.phone = request.POST['phone']
        hocVien.password = request.POST['password']
        hocVien.save()
        return JsonResponse({
            "success": True,
            "message": "Sửa thông tin thành công",
        })
    return render(request, 'home/hocVien/editHV.html',data)
@login_required
def editGV(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except:
        return redirect('/')
    data={
        'giaoVien':giaoVien,
    }
    if request.method == 'POST':
        giaoVien.tenGV = request.POST['tenGV']
        giaoVien.ngaySinh = request.POST['ngaySinh']
        giaoVien.gioiTinh = request.POST['gioiTinh']
        giaoVien.email = request.POST['email']
        giaoVien.sdt = request.POST['sdt']
        giaoVien.password = request.POST['password']
        giaoVien.save()
        return JsonResponse({
            "success": True,
            "message": "Sửa thông tin thành công",
        })
    return render(request, 'home/giaoVien/editGV.html',data)
@login_required
def searchHV(request):
    data = {
        'dsHocVien':HocVien.objects.all(),
    }
    if request.method == 'POST':
        search = request.POST['search']
        data['dsHocVien'] = HocVien.objects.filter(name__icontains=search) | HocVien.objects.filter(maHV__icontains=search) | HocVien.objects.filter(email__icontains=search) | HocVien.objects.filter(phone__icontains=search)
    return render(request, 'home/admin/searchHV.html',data)
@login_required
def searchGV(request):
    data = {
        'dsGiaoVien':GiaoVien.objects.all(),
    }
    if request.method == 'POST':
        search = request.POST['search']
        data['dsGiaoVien'] = GiaoVien.objects.filter(tenGV__icontains=search) | GiaoVien.objects.filter(maGV__icontains=search) | GiaoVien.objects.filter(email__icontains=search) | GiaoVien.objects.filter(sdt__icontains=search)
    return render(request, 'home/admin/searchGV.html',data)

def DDHVtheoNgay(request):
    if request.method == 'POST':
        ngay = request.POST['ngay']
        lopHoc_id = request.POST['lopHoc_id']
        dsDDHV = HOCVIEN_buoihoc.objects.filter(ngay=ngay,lopHoc_id=lopHoc_id)
        data = {
            'dsHV':[hocVien.to_json() for hocVien in HocVien_LopHoc.objects.filter(lopHoc_id=lopHoc_id)],
            'hvbh':[hvbh.to_json() for hvbh in HOCVIEN_buoihoc.objects.filter(lopHoc_id=lopHoc_id,ngay=ngay)],
            'list_lophoc':[lopHoc.to_json() for lopHoc in LopHoc.objects.all()], 
            'dsDDHV':[ddhv.to_json() for ddhv in dsDDHV],
        }
        return JsonResponse({
            "success": True,
            "message": "Thành công",
            "data": data,
        })
@login_required
def addHVLH(request,lopHoc_id):
    lopHoc = LopHoc.objects.get(maLop=lopHoc_id)
    data = {
        'lopHoc':lopHoc,
        'dsHocVien':HocVien.objects.all(),
    }
    if request.method == 'POST':
        hocVien_id = request.POST['hocVien_id']
        hocPhiGiam = request.POST['hocPhiGiam']
        hv = HocVien.objects.get(maHV=hocVien_id)
        data={
            'lopHoc':[lopHoc.to_json() for lopHoc in LopHoc.objects.all()],
            'list_lophoc':LopHoc.objects.all(),
        }
        try:
            HocVien_LopHoc.objects.get(hocVien_id=hv,lopHoc_id=lopHoc)
            return JsonResponse({
                "success": False,
                "message": "Học viên đã đăng ký buổi học này",
            })
        except:
            HocVien_LopHoc.objects.create(hocVien_id=hv,lopHoc_id=lopHoc,hocPhiGiam = hocPhiGiam)
            return JsonResponse({
                "success": True,
                "message": "Đăng ký thành công",
            })
    return render(request, 'home/admin/addHVLH.html',data)

def xemLichHocAdmin(request):
    if request.method == 'POST':
        maLop = request.POST['maLop']
        print(maLop,"##################")
        lopHoc = LopHoc.objects.get(maLop=maLop)
        dslh2 = {}
        for lh in lopHoc.lichHoc.split(','):
            dslh2[int(lh)] = lopHoc.tenLop
        print(dslh2,"##################")
        print(len(list(dict.values(dslh2))),"##################")
        data = {
            'dslh2':dslh2,
        }
        return JsonResponse({
            "success": True,
            "message": "Thành công",
            "data": data,
        })

@login_required
def thongKeLopHoc(request):
    data = {
        'dsLopHoc':LopHoc.objects.all(),
    }
    return render(request, 'home/admin/thongKeLopHoc.html',data)

def tklh(request):
    data = {
        'dsLopHoc':LopHoc.objects.all(),
    }
    if request.method == 'POST':
        from datetime import datetime
        maLop = request.POST['maLop']
        lopHoc = LopHoc.objects.get(maLop=maLop)
        data['hvLH'] = HocVien_LopHoc.objects.filter(lopHoc_id=lopHoc)
        data['hvbh'] = HOCVIEN_buoihoc.objects.filter(lopHoc_id=lopHoc)
        dslh = {}
        print(lopHoc.ngayBatDau,"##################")
        print(date.today(),"##################")
        for lh in lopHoc.lichHoc.split(','):
            dslh[int(lh)] = lopHoc.tenLop
        sobuoi = len(dslh)
        sbDaDay = int(len(dslh) * (date.today() - lopHoc.ngayBatDau).days/7)
        sbCanDay = int(len(dslh) * (lopHoc.ngayKetThuc - lopHoc.ngayBatDau).days/7)
        data['sobuoi'] = sobuoi
        data['sbDaDay'] = sbDaDay
        data['sbCanDay'] = sbCanDay
    return render(request, 'home/admin/tklh.html',data)

@login_required
def locHV(request):
    data = {
        'dsHocVien':[hocVien.to_json() for hocVien in HocVien.objects.all()],
    }
    if request.method == 'POST':
        search = request.POST['search']
        from django.db.models import Q


        ds = HocVien.objects.filter(
            Q(name__icontains=search) 
            | Q(maHV__icontains=search)
            | Q(email__icontains=search)
            | Q(phone__icontains=search)
        )

        print(ds)

        data = {
            'dsHocVien': [hocVien.to_json() for hocVien in ds],
        }
    return JsonResponse({
        "success": True,
        "message": "Thành công",
        "data": data,
    })

def thongTinHocPhi(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except:
        return redirect('/login')
    lophoc = HocVien_LopHoc.objects.filter(hocVien_id=hocVien)
    hphv = HocPhi_HocVien.objects.filter(hocVien_id=hocVien)
    dongTien = DongTien_HocVien.objects.filter(hocVien_id=hocVien)
    tongTien = 0
    for h in hphv:
        tongTien += h.hocPhi
    dong = 0
    for d in dongTien:
        dong += d.soTienDong 

    no = 0
    no = dong - tongTien
    data = {
        'hocVien':hocVien,
        'lophoc':lophoc,
        'hphv':hphv,
        'dongTien':dongTien,
        "tongTien":tongTien,
        "dong":dong,
        "no":no
    }
    return render(request, 'home/hocVien/hocPhi.html',data)

def dongTien(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except:
        return JsonResponse({
            "success": False,
            "message": "Bạn chưa đăng nhập",
        })
    if request.method == 'POST':
        soTienDong = request.POST['soTienDong']
        ngay = datetime.now()
        try:
            DongTien_HocVien.objects.get(hocVien_id=hocVien,soTienDong=soTienDong)
            return JsonResponse({
                "success": False,
                "message": "Học viên đã đóng tiền",
            })
        except:
            DongTien_HocVien.objects.create(hocVien_id=hocVien,soTienDong=soTienDong,ngay=ngay)
            return JsonResponse({
                "success": True,
                "message": "Đóng tiền thành công",
            })


@login_required
def thanhToanLuong(request):
    if request.method == "POST":
        giaoVien_id = request.POST['giaoVien_id']
        giaoVien = GiaoVien.objects.get(maGV=giaoVien_id)
        ngay = datetime.now()
        soTienNhan = request.POST['soTienNhan']
        ghiChu = request.POST['ghiChu']
        try:
            LuongGV.objects.get(giaoVien_id=giaoVien,soTienNhan=soTienNhan,ngay=ngay,ghiChu=ghiChu)
            return JsonResponse({
                "success": False,
                "message": "Giao viên đã nhận tiền",
            })
        except:
            LuongGV.objects.create(giaoVien_id=giaoVien,soTienNhan=soTienNhan,ngay=ngay,ghiChu=ghiChu)
            return JsonResponse({
                "success": True,
                "message": "Nhận tiền thành công",
            })

def error_404(request, exception=None):
    # return render(request, 'error_404.html')
    return JsonResponse({
        'success': False, 
        'message': 'Page not found',
        'error': '404'
    })


def error_500(request):
    # return render(request, 'error_500.html')
    return JsonResponse({
        'success': False,
        'message': 'Internal server error',
        'error': '500'
    })

# 404 Page Not Found
