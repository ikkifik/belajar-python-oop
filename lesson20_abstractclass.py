# Belajar Abstract class -> Blueprint dari class(tidak bisa menjadi object sebelum menjadi class)
# abc = abstract base class

from abc import ABC,abstractmethod

class Button(ABC):

    @abstractmethod #decorator -> memaksa inherit class untuk mengimplementasikannya
    def click(self):
        pass

class PushButton(Button):
    
    def click(self):
        print("Push Button Click")


# tombol = Button()
tombol1 = PushButton()

tombol1.click()


