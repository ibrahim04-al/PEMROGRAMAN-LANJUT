class bapak(object):
    def __init__(self, nama, tinggi, berat):
        self.nama = nama
        self.tinggi = tinggi
        self.berat = berat

    def Tinggi(self):
        print("tinggi kurus")

    def Alis(self):
        print("alis tebal")

class anak(bapak):
    def Malas(self):
        print("malas makan")

    def Alis_baseclass(self):
        return super(anak, self).Alis()

    def putra(self):
        print("Putra sulung")
        

    
b = bapak("Abd.Azis", 176, 68)
print("Nama:", b.nama)
print("Tinggi:", b.tinggi, "cm")
print("Berat:", b.berat, "kg")
b.Tinggi()
b.Alis()

a = anak("Al Ibrahim", 180, 52)
print()
print("Nama:", a.nama)
print("Tinggi:", a.tinggi, "cm")
print("Berat:", a.berat, "kg")
a.Tinggi()
a.Malas()
a.Alis_baseclass()
a.putra()
