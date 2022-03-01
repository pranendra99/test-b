# open and read file txt
file = open("text.txt", "r")

# pencarian berdasarkan kata dengan menampilkan hasil berupa berapa kali ditemukan dalam text file.
# dictionary untuk menampung hasil pencarian
d = dict()

# perulangan untuk mencari kata dalam text file
for line in file:
    # memecah kalimat menjadi kata dan menghilangkan spasi
    line = line.strip()
    
    # mengecilkan kata
    line = line.lower()

    # memecah kalimat menjadi kata
    words = line.split()

    # perulangan untuk mencari kata dalam text file
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1


# menampilkan hasil pencarian
for key in list(d.keys()):
    print("{} : {}".format(key, d[key]))



