# Belajar private variable

class Hero:

    # class variable
    jumlah = 0
    __privateJumlah = 0 
    _protectedJumlah = 0

    def __init__(self, name, hp): # public
        self.name = name
        self.hp = hp

        # variable instance private __
        self.__private = "private"
        # variable instance protected _
        self._protected = "protected"

lina = Hero("lina", 100)

print(lina.__dict__)
lina._protected = "testing"

print(lina.__dict__)