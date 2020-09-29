# Belajar magic method -> method yang sudah memiliki keyword(sudah tersedia di python)
# ditandai dengan "__" double underscore

class Mangga:

    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah
    
    def __repr__(self): #dipakai saat debugging
        return f"Debug: Mangga {self.nama} dengan jumlah {self.jumlah}"

    def __str__(self): #dipakai ketika program telah jadi
        return f"Mangga {self.nama} dengan jumlah {self.jumlah}"

    def __add__(self, objek): #penjumlahan
        return self.jumlah + objek.jumlah

    @property
    def __dict__(self): #override method __dict__
        return "Objek ini memiliki nama dan jumlah"

belanja1 = Mangga("Arumanis", 10)
belanja2 = Mangga("Mana lagi", 5)
print(repr(belanja1))
print(belanja2)

print(belanja1 + belanja2)

print(belanja1.__dict__) #mengeluarkan dictionary