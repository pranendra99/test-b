# buka dan baca file txt
file = open("text.txt", "r")

#urutkan kata berdasarkan abjad dari A-Z
def urut(file):
    #memecah kalimat menjadi kata
    w = file.read().split()

    #perulangan 
    for i in range(len(w)):
        #mengubah kata menjadi huruf kecil
        w[i] = w[i].lower()
    
    #mengurus kata
    file = sorted(w)
    print(file)

urut(file)


