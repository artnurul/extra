from select import select
from . import db


class DataBarang(db.Model):
    __tablename__ = 'tabel_data_barang'
    id_data_barang = db.Column(db.Integer, primary_key=True)
    nama_barang = db.Column(db.String(100))
    stok = db.Column(db.Integer)
    satuan = db.Column(db.String(100))
    harga_beli = db.Column(db.Integer)
    harga_jual = db.Column(db.Integer)
    diskon = db.Column(db.String(100))
    supplier = db.Column(db.Integer, db.ForeignKey('tabel_data_supplier.id_data_supplier'))
    kategori = db.Column(db.Integer, db.ForeignKey(
        'tabel_data_kategori.id_data_kategori'))
    total = db.Column(db.Integer)
    barcode = db.Column(db.String(100))

    def toJson(self):
        return {
            'id_data_barang': self.id_data_barang,
            'nama_barang': self.nama_barang,
            'kategori': self.kategori,
            'stok': self.stok,
            'satuan': self.satuan,
            'harga_beli': self.harga_beli,
            'harga_jual': self.harga_jual,
            'diskon': self.diskon,
            'supplier': self.supplier,
            'total': self.total,
            'barcode': self.barcode
        }


class DataSupplier(db.Model):
    __tablename__ = 'tabel_data_supplier'
    id_data_supplier = db.Column(db.Integer, primary_key=True)
    nama_supplier = db.Column(db.String(100))
    alamat_supplier = db.Column(db.String(100))
    contact_supplier = db.Column(db.String)
    keterangan_supplier = db.Column(db.String)

    def toJson(self):
        return {
            'id_data_supplier': self.id_data_supplier,
            'nama_supplier': self.nama_supplier,
            'alamat_supplier': self.alamat_supplier,
            'contact_supplier': self.contact_supplier,
            'keterangan_supplier': self.keterangan_supplier
        }


class DataPelanggan(db.Model):
    __tablename__ = 'tabel_data_pelanggan'
    id_data_pelanggan = db.Column(db.Integer, primary_key=True)
    nama_pelanggan = db.Column(db.String(100))
    alamat_pelanggan = db.Column(db.String(100))
    contact_pelanggan = db.Column(db.String)
    keterangan_pelanggan = db.Column(db.String)

    def toJson(self):
        return {
            'id_data_pelanggan': self.id_data_pelanggan,
            'nama_pelanggan': self.nama_pelanggan,
            'alamat_pelanggan': self.alamat_pelanggan,
            'contact_pelanggan': self.contact_pelanggan,
            'keterangan_pelanggan': self.keterangan_pelanggan
        }


class DataKategori(db.Model):
    __tablename__ = 'tabel_data_kategori'
    id_data_kategori = db.Column(db.Integer, primary_key=True)
    nama_kategori = db.Column(db.String(100))
    keterangan_kategori = db.Column(db.String)

    def toJson(self):
        return {
            'id_data_kategori': self.id_data_kategori,
            'nama_kategori': self.nama_kategori,
            'keterangan_kategori': self.keterangan_kategori
        }


class DataSatuan(db.Model):
    __tablename__ = 'tabel_data_satuan'
    id_data_satuan = db.Column(db.Integer, primary_key=True)
    nama_satuan = db.Column(db.String(100))
    keterangan_satuan = db.Column(db.String)

    def toJson(self):
        return {
            'id_data_satuan': self.id_data_satuan,
            'nama_satuan': self.nama_satuan,
            'keterangan_satuan': self.keterangan_satuan
        }


class DataOutlet(db.Model):
    __tablename__ = 'tabel_data_outlet'
    id_data_outlet = db.Column(db.Integer, primary_key=True)
    nama_outlet = db.Column(db.String(100))
    nama_branchmanager = db.Column(db.String(100))
    alamat_outlet = db.Column(db.String(100))
    contact_outlet = db.Column(db.String)

    def toJson(self):
        return {
            'id_data_outlet': self.id_data_outlet,
            'nama_outlet': self.nama_outlet,
            'nama_branchmanager': self.nama_branchmanager,
            'alamat_outlet': self.alamat_outlet,
            'contact_outlet': self.contact_outlet,

        }


class DataPenjualan(db.Model):
    __tablename__ = 'tabel_data_penjualan'
    id_data_penjualan = db.Column(db.Integer, primary_key=True)
    kode_transaksi = db.Column(db.Integer())
    tanggal_transaksi = db.Column(db.Integer())
    id_outlet = db.Column(db.Integer())
    id_barang = db.Column(db.Integer, db.ForeignKey(
        'tabel_data_barang.id_data_barang'))
    id_pelanggan = db.Column(db.Integer)
    qty = db.Column(db.Integer)
    potongan = db.Column(db.Integer)
    total_harga = db.Column(db.Integer)

    def toJson(self):
        return {
            'id_data_penjualan': self.id_data_penjualan,

            'kode_transaksi': self.kode_transaksi,
            'tanggal_transaksi': self.tanggal_transaksi,

            'id_outlet': self.id_outlet,
            'id_barang': self.id_barang,
            'id_pelanggan': self.id_pelanggan,
            'qty': self.qty,
            'potongan': self.potongan,
            'total_harga': self.total_harga,

        }


class DataUsers(db.Model):
    __tablename__ = 'tabel_data_users'
    id_data_users = db.Column(db.Integer, primary_key=True)
    nama_pengguna = db.Column(db.String())
    password = db.Column(db.String())
    hak_akses = db.Column(db.String())
    cabang = db.Column(db.Integer, db.ForeignKey(
        'tabel_data_outlet.id_data_outlet'))
    username = db.Column(db.String())

    def toJson(self):
        return {
            'id_data_users': self.id_data_users,
            'nama_pengguna': self.nama_pengguna,
            'password': self.password,
            'hak_akses': self.hak_akses,
            'cabang': self.cabang,
            'username': self.username,
        }


class DataReturn(db.Model):
    __tablename__ = 'tabel_data_return'
    id_data_return = db.Column(db.Integer, primary_key=True)
    nama_barang_return = db.Column(db.String())
    tanggal = db.Column(db.String())
    keterangan = db.Column(db.String())
   
    def toJson(self):
        return {
            'id_data_return': self.id_data_return,
            'nama_barang_return': self.nama_barang_return,
            'tanggal': self.tanggal,
            'keterangan': self.keterangan,
            
        }


class DataPengeluaranMarketing(db.Model):
    __tablename__ = 'tabel_data_pengeluaran_marketing'
    id_data_pengeluaran = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.String())
    kode = db.Column(db.Integer())
    pembayaran = db.Column(db.String())
    jumlah = db.Column(db.Integer())
    sumber_dana = db.Column(db.String())
    metode_bayar = db.Column(db.String())
    keterangan = db.Column(db.String())


    def toJson(self):
        return {
            'id_data_pengeluaran': self.id_data_pengeluaran,
            'tanggal': self.tanggal,
            'kode': self.kode,
            'pembayaran': self.pembayaran,
            'jumlah': self.jumlah,
            'sumber_dana': self.sumber_dana,
            
            'keterangan': self.keterangan,
            'metode_bayar': self.metode_bayar,

        }


class DataAlokasi(db.Model):
    __tablename__ = 'tabel_data_alokasi'
    id_data_alokasi = db.Column(db.Integer, primary_key=True)
    kode_alokasi = db.Column(db.String())
    jenis_alokasi = db.Column(db.String())
    keterangan = db.Column(db.String())
   
    def toJson(self):
        return {
            'id_data_alokasi': self.id_data_alokasi,
            'kode_alokasi': self.kode_alokasi,
            'jenis_alokasi': self.jenis_alokasi,
            'keterangan': self.hak_akketeranganses,
           
        }
