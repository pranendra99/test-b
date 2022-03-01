
# ubah kata "adalah" menjadi "ialah"
caritext = "adalah"

ubahtext = "ialah"

# buka dan baca file txt kemudian tampilkan hasilnya berupa line textnya
with open("text.txt", "r") as file:
    for line in file:
        if caritext in line:
            line = line.replace(caritext, ubahtext)
            print(line)
