#tuodaan time -kirjasto jotta tulos voidaan jättää ruudulle
import time


#haetaan käyttäjän alkup. leveli
level = int(input('Käyttäjän leveli:'))
mlevel = int(input('Mainoksessa mainittu leveli:'))


#parsitaan leveli tämän funktion avulla
if level < mlevel:
    print("Ostoksen jälkeen saat levelin",mlevel)

else:
    flevel = mlevel + level
    print("Ostoksen jälkeen saat levelin",flevel)


#Jätetään tulos ruudulle hetkeksi
time.sleep(5)
