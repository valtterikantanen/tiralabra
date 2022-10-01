# Viikkoraportti 4

Kuluneella viikolla loin ensimmäisen toteutuksen IDA\*-algoritmista ja paransin sovelluksen käyttöliittymän toiminnallisuuksia.

Olin aiemmin toteuttanut käyttöliittymän Pygame-kirjastolla, mutta siirryin tällä viikolla käyttämään [TkInter](https://docs.python.org/3/library/tkinter.html)-kirjastoa. Nyt sovellusta pystyy käyttämään täysin graafisen käyttöliittymän avulla. Käyttöliittymä esittää käytettävän kartan ja löydetyn reitin, kuten myös algoritmin käyttämän ajan ja reitin pituuden. TkInter vaikuttaa myös toimivan paljon tehokkaammin kartan piirtämisessä kuin Pygame, minkä lisäksi esimerkiksi koordinaattien valinta toimii mielestäni paremmin tekstikenttien avulla.

En ollut onneksi ehtinyt vielä käyttää liikaa aikaa Pygamen ääressä. Opin joka tapauksessa sen, että jatkossa mietin paremmin suurimpia valintoja, jotka vaikuttavat ohjelman käyttöön ja toteutukseen, jotta turhalta työltä vältyttäisiin. Opin myös, että IDA\*-algoritmin toiminta hidastuu todella paljon, kun kartan koko kasvaa ja esteiden määrä lisääntyy. Yleisesti ottaen Dijkstra vaikuttaa siis paremmalta valinnalta, mikäli kartan koosta tai sen sisällöstä ei ole tarkempaa tietoa.

Tällä viikolla aloitin myös toteutusdokumentin kirjoittamisen.

En ehtinyt vielä laatia yksikkötestejä IDA\*-algoritmille, joten seuraavana askeleena on testauskattavuuden parantaminen. Algoritmi on kuitenkin tähän mennessä löytänyt aina saman pituisen reitin kuin Dijkstran algoritmi, joten toteutus on todennäköisesti oikea.

Kuluneella viikolla käytin työhön aikaa kolmetoista tuntia.