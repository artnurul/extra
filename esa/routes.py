
import os
from . import create_app, db
from .models import DataBarang, DataOutlet, DataPenjualan, DataReturn, DataSatuan, DataSupplier, DataPelanggan, DataKategori, DataUsers, DataPengeluaranMarketing
from flask import jsonify, redirect, render_template, request, url_for

import hashlib


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.route("/")
def main():
    return render_template('dashboard/index.html')


#def present all_data_database
@app.route("/data-barang", methods=["GET"])
def semuaBarang():
    dataBarang = db.session.query(DataBarang, DataSupplier, DataKategori).join(DataBarang).filter(DataBarang.kategori==DataKategori.id_data_kategori).all()
    print(dataBarang)
    dataSupplier = DataSupplier.query.all()
    namaBarang = DataBarang.query.all()
    dataKategori = DataKategori.query.all()

    return render_template('data/data_barang.html', data=dataBarang, dataSupplier=dataSupplier, dataKategori=dataKategori, namaBarang=namaBarang)


# fungsi untuk menambahkan data barang
@app.route("/tambah-data-barang", methods=["POST"])
def tambahDataBarang():
    namaBarang = request.form['nama_barang']
    kategori = request.form['kategori']
    barcode = request.form['barcode']
    stok = request.form['stok']
    satuan = request.form['satuan']
    hargaBeli = request.form['harga_beli']
    hargaJual = request.form['harga_jual']
    supplier = request.form['supplier']
    total = request.form['total']
    diskon = request.form['diskon']

    barangdekatbawah = DataBarang(nama_barang=namaBarang, kategori=kategori, barcode=barcode, stok=stok,
                                  satuan=satuan, harga_beli=hargaBeli, harga_jual=hargaJual, supplier=supplier, total=total, diskon=diskon,)

    db.session.add(barangdekatbawah)
    db.session.commit()

    return redirect(url_for('semuaBarang'))

#delete data barang
@app.route("/delete-data-barang/<id>", methods=["GET"])
def deleteDataBarang(id):
    barang = DataBarang.query.filter_by(id_data_barang=id).first()

    db.session.delete(barang)
    db.session.commit()

    return redirect(url_for('semuaBarang'))


#edit data barang
@app.route("/edit-data-barang/<id>", methods=["GET"])
def editDataBarang(id):
    barang = DataBarang.query.filter_by(id_data_barang=id).first()
    dataSupplier = DataSupplier.query.all()
    dataKategori = DataKategori.query.all()

    return render_template('data/edit_data_barang.html', data=barang, dataSupplier=dataSupplier, dataKategori=dataKategori)


#update barang
@app.route("/update-data-barang", methods=["POST"])
def updateDataBarang():
    id = request.form['id_data_barang']
    namaBarang = request.form['nama_barang']
    kategori = request.form['kategori']
    barcode = request.form['barcode']
    stok = request.form['stok']
    satuan = request.form['satuan']
    hargaBeli = request.form['harga_beli']
    hargaJual = request.form['harga_jual']
    supplier = request.form['supplier']
    total = request.form['total']
    diskon = request.form['diskon']

    barang = DataBarang.query.filter_by(id_data_barang=id).first()

    barang.nama_barang = namaBarang
    barang.kategori = kategori
    barang.barcode = barcode
    barang.stok = stok
    barang.satuan = satuan
    barang.harga_beli = hargaBeli
    barang.harga_jual = hargaJual
    barang.supplier = supplier
    barang.total = total
    barang.diskon = diskon

    db.session.add(barang)
    db.session.commit()

    return redirect(url_for('semuaBarang'))








@app.route("/")
def mainSupplier():
    return render_template('dashboard/index.html')


@app.route("/data-supplier", methods=["GET"])
def semuaSupplier():
    dataSupplier = DataSupplier.query.all()
    return render_template('data/data_supplier.html', data=dataSupplier)


@app.route("/tambah-data-supplier", methods=["POST"])
def tambahDataSupplier():
    namaSupplier = request.form['nama_supplier']
    alamatSupplier = request.form['alamat_supplier']
    contactSupplier = request.form['contact_supplier']
    keteranganSupplier = request.form['keterangan_supplier']

    supplier = DataSupplier(nama_supplier=namaSupplier,
                            alamat_supplier=alamatSupplier, contact_supplier=contactSupplier, keterangan_supplier=keteranganSupplier,)

    db.session.add(supplier)
    db.session.commit()

    return redirect(url_for('semuaSupplier'))


@app.route("/delete-data-supplier/<id>", methods=["GET"])
def deleteDataSupplier(id):
    supplier = DataSupplier.query.filter_by(id_data_supplier=id).first()

    db.session.delete(supplier)
    db.session.commit()

    return redirect(url_for('semuaSupplier'))


#edit data supplier
@app.route("/edit-data-supplier/<id>", methods=["GET"])
def editDataSupplier(id):
    supplier = DataSupplier.query.filter_by(id_data_supplier=id).first()
    return render_template('data/edit_data_supplier.html', data=supplier)


#update supplier
@app.route("/update-data-supplier", methods=["POST"])
def updateDatasupplier():
    id = request.form['id']
    namaSupplier = request.form['nama_supplier']
    alamatSupplier = request.form['alamat_supplier']
    contactSupplier = request.form['contact_supplier']
    keteranganSupplier = request.form['keterangan_supplier']

    supplier = DataSupplier.query.filter_by(
        id_data_supplier=id).first()

    supplier.nama_supplier = namaSupplier
    supplier.alamat_supplier = alamatSupplier
    supplier.contact_supplier = contactSupplier
    supplier.keterangan_supplier = keteranganSupplier

    db.session.add(supplier)
    db.session.commit()

    return redirect(url_for('semuaSupplier'))























@app.route("/")
def mainPelanggan():
    return render_template('dashboard/index.html')


@app.route("/data-pelanggan", methods=["GET"])
def semuaPelanggan():
    dataPelanggan = DataPelanggan.query.all()
    return render_template('data/data_pelanggan.html', data=dataPelanggan)


@app.route("/tambah-data-pelanggan", methods=["POST"])
def tambahDataPelanggan():
    namaPelanggan = request.form['nama_pelanggan']
    alamatPelanggan = request.form['alamat_pelanggan']
    contactPelanggan = request.form['contact_pelanggan']
    keteranganPelanggan = request.form['keterangan_pelanggan']

    pelanggan = DataPelanggan(nama_pelanggan=namaPelanggan,
                              alamat_pelanggan=alamatPelanggan, contact_pelanggan=contactPelanggan, keterangan_pelanggan=keteranganPelanggan,)

    db.session.add(pelanggan)
    db.session.commit()

    return redirect(url_for('semuaPelanggan'))




@app.route("/delete-data-pelanggan/<id>", methods=["GET"])
def deleteDataPelanggan(id):
    pelanggan = DataPelanggan.query.filter_by(
        id_data_pelanggan=id).first()

    db.session.delete(pelanggan)
    db.session.commit()

    return redirect(url_for('semuaPelanggan'))


#edit data pelanggan
@app.route("/edit-data-pelanggan/<id>", methods=["GET"])
def editDataPelanggan(id):
    pelanggan = DataPelanggan.query.filter_by(id_data_pelanggan=id).first()
    return render_template('data/edit_data_pelanggan.html', data=pelanggan)


#update supplier
@app.route("/update-data-pelanggan", methods=["POST"])
def updateDataPelanggan():
    id = request.form['id']
    namaPelanggan = request.form['nama_pelanggan']
    alamatPelanggan = request.form['alamat_pelanggan']
    contactPelanggan = request.form['contact_pelanggan']
    keteranganPelanggan = request.form['keterangan_pelanggan']

    pelanggan = DataPelanggan.query.filter_by(
        id_data_pelanggan=id).first()

    pelanggan.nama_pelanggan = namaPelanggan
    pelanggan.alamat_pelanggan = alamatPelanggan
    pelanggan.contact_pelanggan = contactPelanggan
    pelanggan.keterangan_pelanggan = keteranganPelanggan

    db.session.add(pelanggan)
    db.session.commit()

    return redirect(url_for('semuaPelanggan'))
























@app.route("/")
def mainKategori():
    return render_template('dashboard/index.html')


@app.route("/data-kategori", methods=["GET"])
def semuaKategori():
    dataKategori = DataKategori.query.all()
    return render_template('data/data_kategori.html', data=dataKategori)


@app.route("/tambah-data-kategori", methods=["POST"])
def tambahDataKategori():
    namaKategori = request.form['nama_kategori']
    keteranganKategori = request.form['keterangan_kategori']

    kategori = DataKategori(nama_kategori=namaKategori,
                            keterangan_kategori=keteranganKategori,)

    db.session.add(kategori)
    db.session.commit()

    return redirect(url_for('semuaKategori'))


@app.route("/delete-data-kategori/<id>", methods=["GET"])
def deleteDataKategori(id):
    kategori = DataKategori.query.filter_by(id_data_kategori=id).first()

    db.session.delete(kategori)
    db.session.commit()

    return redirect(url_for('semuaKategori'))


#edit data pelanggan
@app.route("/edit-data-kategori/<id>", methods=["GET"])
def editDataKategori(id):
    kategori = DataKategori.query.filter_by(id_data_kategori=id).first()
    return render_template('data/edit_data_kategori.html', data=kategori)


#update supplier
@app.route("/update-data-kategori", methods=["POST"])
def updateDataKategori():
    id = request.form['id']
    namaKategori = request.form['nama_kategori']
    keteranganKategori = request.form['keterangan_kategori']

    kategori = DataKategori.query.filter_by(
        id_data_kategori=id).first()

    kategori.nama_kategori = namaKategori
    kategori.keterangan_kategori = keteranganKategori

    db.session.add(kategori)
    db.session.commit()

    return redirect(url_for('semuaKategori'))















@app.route("/")
def mainSatuan():
    return render_template('dashboard/index.html')


@app.route("/data-satuan", methods=["GET"])
def semuaSatuan():
    dataSatuan = DataSatuan.query.all()
    return render_template('data/data_satuan.html', data=dataSatuan)


@app.route("/tambah-data-satuan", methods=["POST"])
def tambahDatasatuan():
    namasatuan = request.form['nama_satuan']
    keteranganSatuan = request.form['keterangan_satuan']

    satuan = DataSatuan(nama_satuan=namasatuan,
                      keterangan_satuan=keteranganSatuan,)

    db.session.add(satuan)
    db.session.commit()

    return redirect(url_for('semuaSatuan'))


@app.route("/delete-data-satuan/<id>", methods=["GET"])
def deleteDataSatuan(id):
    satuan = DataSatuan.query.filter_by(id_data_satuan=id).first()

    db.session.delete(satuan)
    db.session.commit()

    return redirect(url_for('semuaSatuan'))


#edit data pelanggan
@app.route("/edit-data-satuan/<id>", methods=["GET"])
def editDataSatuan(id):
    satuan = DataSatuan.query.filter_by(id_data_satuan=id).first()
    return render_template('data/edit_data_satuan.html', data=satuan)


#update supplier
@app.route("/update-data-satuan", methods=["POST"])
def updateDataSatuan():
    id = request.form['id']
    namaSatuan = request.form['nama_satuan']
    keteranganSatuan = request.form['keterangan_satuan']

    satuan = DataSatuan.query.filter_by(
        id_data_satuan=id).first()

    satuan.nama_satuan = namaSatuan
    satuan.keterangan_satuan = keteranganSatuan

    db.session.add(satuan)
    db.session.commit()

    return redirect(url_for('semuaSatuan'))











@app.route("/data-outlet", methods=["GET"])
def semuaOutlet():
    dataOutlet = DataOutlet.query.all()
    return render_template('data/data_outlet.html', data=dataOutlet)


@app.route("/tambah-data-outlet", methods=["POST"])
def tambahDataOutlet():
    namaOutlet = request.form['nama_outlet']
    namaBranchmanager = request.form['nama_branchmanager']
    alamatOutlet = request.form['alamat_outlet']
    contactOutlet = request.form['contact_outlet']
    
    outlet = DataOutlet(nama_outlet=namaOutlet,
                            nama_branchmanager=namaBranchmanager, alamat_outlet=alamatOutlet, contact_outlet=contactOutlet,)

    db.session.add(outlet)
    db.session.commit()

    return redirect(url_for('semuaOutlet'))


@app.route("/delete-data-outlet/<id>", methods=["GET"])
def deleteDataOutlet(id):
    outlet = DataOutlet.query.filter_by(id_data_outlet=id).first()

    db.session.delete(outlet)
    db.session.commit()

    return redirect(url_for('semuaOutlet'))


#edit data supplier
@app.route("/edit-data-outlet/<id>", methods=["GET"])
def editDataOutlet(id):
    outlet = DataOutlet.query.filter_by(id_data_outlet=id).first()
    return render_template('data/edit_data_outlet.html', data=outlet)


#update supplier
@app.route("/update-data-outlet", methods=["POST"])
def updateDataOutlet():
    id = request.form['id']
    namaOutlet = request.form['nama_outlet']
    namaBranchmanager = request.form['nama_branchmanager']
    alamatOutlet = request.form['alamat_outlet']
    contactOutlet = request.form['contact_outlet']

    outlet = DataOutlet.query.filter_by(
        id_data_outlet=id).first()

    outlet.nama_outlet = namaOutlet
    outlet.nama_branchmanager = namaBranchmanager
    outlet.alamat_outlet = alamatOutlet
    outlet.contact_outlet = contactOutlet

    db.session.add(outlet)
    db.session.commit()

    return redirect(url_for('semuaOutlet'))













@app.route("/")
def mainPenjualan():
    return render_template('dashboard/index.html')


@app.route("/data-penjualan", methods=["GET"])
def semuaPenjualan():
    dataPen = db.session.query(
        DataPenjualan, DataBarang).join(DataPenjualan).all()
    idOutlet = DataOutlet.query.all()
    idBarang = DataBarang.query.all()
    idPelanggan = DataPelanggan.query.all()
    return render_template('data/data_penjualan.html', datacu=dataPen, data=idOutlet, dataku=idBarang, idinPelanggan=idPelanggan)


@app.route("/tambah-data-penjualan", methods=["POST"])
def tambahDataPenjualan():
    kodeTransaksi = request.form['kode_transaksi']
    tanggalTransaksi = request.form['tanggal_transaksi']
    idOutlet = request.form['id_outlet']
    idBarang = request.form['id_barang']
    idPelanggan = request.form['id_pelanggan']
    qty = request.form['qty']
    potongan = request.form['potongan']
    totalHarga = request.form['total_harga']

    penjualannya = DataPenjualan(kode_transaksi=kodeTransaksi,
                              tanggal_transaksi=tanggalTransaksi, id_outlet=idOutlet, id_barang=idBarang, id_pelanggan=idPelanggan, qty=qty, potongan=potongan, total_harga=totalHarga)

    db.session.add(penjualannya)
    db.session.commit()

    return redirect(url_for('semuaPenjualan'))


@app.route("/delete-data-penjualan/<id>", methods=["GET"])
def deleteDataPenjualan(id):
    penjualanku = DataPenjualan.query.filter_by(id_data_penjualan=id).first()

    db.session.delete(penjualanku)
    db.session.commit()

    return redirect(url_for('semuaPenjualan'))


#edit data supplier
@app.route("/edit-data-penjualan/<id>", methods=["GET"])
def editDataPenjualan(id):
    penjualan = DataPenjualan.query.filter_by(id_data_penjualan=id).first()
    barang = DataBarang.query.all()
    outlet = DataOutlet.query.all()
    pelanggan = DataPelanggan.query.all()
    return render_template('data/edit_data_penjualan.html', dataci=penjualan, idBarang=barang, idrOutlet=outlet, idePelanggan=pelanggan)


#update supplier
@app.route("/update-data-penjualan", methods=["POST"])
def updateDataPenjualan():
    id = request.form['id']
    kodeTransaksi = request.form['kode_transaksi']
    tanggalTransaksi = request.form['tanggal_transaksi']
    idOutlet = request.form['id_outlet']
    idBarang = request.form['id_barang']
    idPelanggan = request.form['id_pelanggan']
    qty = request.form['qty']
    potongan = request.form['potongan']
    totalHarga = request.form['total_harga']
    
    penjualanmu = DataPenjualan.query.filter_by(
        id_data_penjualan=id).first()

    penjualanmu.kode_transaksi = kodeTransaksi
    penjualanmu.tanggal_transaksi = tanggalTransaksi
    penjualanmu.id_outlet = idOutlet
    penjualanmu.id_barang = idBarang
    penjualanmu.id_pelanggan = idPelanggan
    penjualanmu.qty = qty
    penjualanmu.potongan = potongan
    penjualanmu.total_harga = totalHarga

    db.session.add(penjualanmu)
    db.session.commit()

    return redirect(url_for('semuaPenjualan'))


@app.route("/data-users", methods=["GET"])
def semuaUsers():
    dataUsers = db.session.query(
        DataUsers, DataOutlet).join(DataUsers).all()
    cabang = DataOutlet.query.all()
    barang = DataOutlet.query.all()
    return render_template('data/data_users.html', isiData=dataUsers, dataUsers=cabang, idBarang=barang)

@app.route("/tambah-data-users", methods=["POST"])
def tambahDataUsersm():
    namaPengguna = request.form['nama_pengguna']
    password = request.form['password']
    hakAkses = request.form['hak_akses']
    cabang = request.form['cabang']
    username = request.form['username']

    users = DataUsers(nama_pengguna=namaPengguna,
                        password=encrypt_string(password), hak_akses=hakAkses, cabang=cabang, username=username,)
    db.session.add(users)
    db.session.commit()
    return redirect(url_for('semuaUsers'))

@app.route("/delete-data-users/<id>", methods=["GET"])
def deleteDataUsersm(id):
    users = DataUsers.query.filter_by(id_data_users=id).first()
    db.session.delete(users)
    db.session.commit()
    return redirect(url_for('semuaUsers'))

@app.route("/edit-data-users/<id>", methods=["GET"])
def editDataUsersm(id):
    users = DataUsers.query.filter_by(id_data_users=id).first()
    cabang = DataOutlet.query.all()
    return render_template('data/edit_data_users.html', data=users, dataOutlet=cabang)

@app.route("/update-data-gusers", methods=["POST"])
def updateDataUsersm():
    id = request.form['id']
    namaPengguna = request.form['nama_pengguna']
    password = request.form['password']
    hakAkses = request.form['hak_akses']
    cabang = request.form['cabang']

    users = DataUsers.query.filter_by(
        id_data_users=id).first()

    users.nama_pengguna = namaPengguna
    users.password = password
    users.hak_akses = hakAkses
    users.cabang = cabang

    db.session.add(users)
    db.session.commit()

    return redirect(url_for('semuaUsers'))









@app.route("/data-return", methods=["GET"])
def semuaReturn():
    data = DataReturn.query.all()

    return render_template('data/data_return.html', data=data)


@app.route("/tambah-data-return", methods=["POST"])
def tambahDataReturnm():
    namaBarangReturn = request.form['nama_barang_return']
    tanggal = request.form['tanggal']
    keterangan = request.form['keterangan']
    
    data = DataReturn(nama_barang_return=namaBarangReturn,
                         tanggal=tanggal, keterangan=keterangan,)
    db.session.add(data)
    db.session.commit()
    return redirect(url_for('semuaReturn'))


@app.route("/delete-data-return/<id>", methods=["GET"])
def deleteDataReturn(id):
    data = DataReturn.query.filter_by(id_data_return=id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('semuaReturn'))


@app.route("/edit-data-return/<id>", methods=["GET"])
def editDataReturn(id):
    data = DataReturn.query.filter_by(id_data_return=id).first()
    
    return render_template('data/edit_data_return.html', data=data)


@app.route("/update-data-return", methods=["POST"])
def updateDataReturn():
    id = request.form['id']
    namaBarangReturn = request.form['nama_barang_return']
    tanggal = request.form['tanggal']
    keterangan = request.form['keterangan']
    
    data = DataReturn.query.filter_by(
        id_data_return=id).first()

    data.nama_barang_return = namaBarangReturn
    data.tanggal = tanggal
    data.keterangan = keterangan

    db.session.add(data)
    db.session.commit()

    return redirect(url_for('semuaReturn'))







@app.route("/data-pengeluaran-marketing", methods=["GET"])
def semuaPelumar():
    datamu = DataPengeluaranMarketing.query.all()

    return render_template('data/data_pengeluaran_marketing.html', databor=datamu)


@app.route("/tambah-data-pengeluaran-marketing", methods=["POST"])
def tambahDataPengeluaranMarketing():
    tanggal = request.form['tanggal']
    kode = request.form['kode']
    jumlah = request.form['jumlah']
    sumberDana = request.form['sumber_dana']
    keterangan = request.form['keterangan']
    metodeBayar = request.form['metode_bayar']

    herData = DataPengeluaranMarketing(tanggal=tanggal, kode=kode,
                                       jumlah=jumlah, sumber_dana=sumberDana, keterangan=keterangan, metode_bayar=metodeBayar,)
    db.session.add(herData)
    db.session.commit()
    return redirect(url_for('semuaPelumar'))


@app.route("/delete-data-pengeluaran-marketing/<id>", methods=["GET"])
def deleteDataPengeluaranMarketing(id):
    theirData = DataPengeluaranMarketing.query.filter_by(
        id_data_pengeluaran=id).first()
    db.session.delete(theirData)
    db.session.commit()
    return redirect(url_for('semuaPelumar'))


@app.route("/edit-data-pengeluaran-marketing/<id>", methods=["GET"])
def editDataPengeluaranMarketing(id):
    datamu = DataPengeluaranMarketing.query.filter_by(
        id_data_pengeluaran=id).first()

    return render_template('data/data_pengeluaran_marketing.html', datamek=datamu)


@app.route("/update-data-pengeluaran-marketing", methods=["POST"])
def updateDataPengeluaranMarketing():
    id = request.form['id']

    tanggal = request.form['tanggal']
    kode = request.form['kode']
    pembayaran = request.form['pembayaran']
    jumlah = request.form['jumlah']
    sumberDana = request.form['sumber_dana']
    keterangan = request.form['keterangan']
    metodeBayar = request.form['metode_bayar']
    ourData = DataPengeluaranMarketing.query.filter_by(
        id_data_pengeluaran=id).first()

    ourData.tanggal = tanggal
    ourData.kode = kode
    ourData.pembayaran = pembayaran
    ourData.jumlah = jumlah
    ourData.sumber_dana = sumberDana
    ourData.keterangan = keterangan
    ourData.metode_bayar = metodeBayar
    
    

    db.session.add(ourData)
    db.session.commit()

    return redirect(url_for('semuaPelumar'))








@app.route("/")
def mainAlokasi():
    return render_template('dashboard/index.html')


@app.route("/data-alokasi", methods=["GET"])
def semuaAlokasi():
    dataAlokasi = DataPelanggan.query.all()
    return render_template('data/data_alokasi.html', data=dataAlokasi)


@app.route("/tambah-data-alokasi", methods=["POST"])
def tambahDataAlokasi():
    kodeAlokasi = request.form['kode_alokasi']
    jenisAlokasi = request.form['jenis_alokasi']
    keterangan = request.form['keterangan']
   
    alokasi = DataAlokasi(kode_alokasi=kodeAlokasi,
                              jenis_alokasi=jenisAlokasi, keterangan=keterangan,)

    db.session.add(alokasi)
    db.session.commit()

    return redirect(url_for('semuaAlokasi'))














    
