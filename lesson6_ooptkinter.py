# Belajar Tkinter
import tkinter

main_window = tkinter.Tk() # tiap class diberi huruf kapital

label1 = tkinter.Label(main_window, text = "label1")
label2 = tkinter.Label(main_window, text = "label2")

tombol1 = tkinter.Button(main_window, text = "Tombol1")
tombol2 = tkinter.Button(main_window, text = "Tombol2")

# method positioning
label1.pack() # huruf kecil semua -> method/function
label2.pack()
tombol1.pack()
tombol2.pack()

# method menampilkan GUI
main_window.mainloop()