# Toteutusdokumentti

## Ohjelman rakenne

Projektin rakenne on seuraava:
```
src
├── dijkstra.py
├── graph.py
├── heap.py
├── ida_star.py
├── index.py
├── maps
│   ├── Berlin_0_256.map
│   ├── Berlin_0_256.map.scen
│   └── Map_20.map
├── tests
│   ├── dijkstra_test_all_cases.py
│   ├── dijkstra_test.py
│   ├── heap_test.py
└── ui
    └── ui.py
```

Osien toiminta on pääasiassa seuraavanlainen:

* [`dijkstra.py`](https://github.com/valtterikantanen/tiralabra/blob/master/src/dijkstra.py) ja [`ida_star.py`](https://github.com/valtterikantanen/tiralabra/blob/master/src/ida_star.py) vastaavat Dijkstran algoritmin ja IDA\*-algoritmin toteutuksista
* [`graph.py`](https://github.com/valtterikantanen/tiralabra/blob/master/src/graph.py) vastaa tekstimuotoisten karttojen muuttamisesta verkoksi vieruslistaesitystä käyttäen
* [`heap.py`](https://github.com/valtterikantanen/tiralabra/blob/master/src/heap.py) vastaa Dijkstran algoritmissa tarvittavan binäärikeon toteutuksesta
* [`index.py`](https://github.com/valtterikantanen/tiralabra/blob/master/src/index.py) käynnistää ohjelman toiminnan
* [`/maps`](https://github.com/valtterikantanen/tiralabra/tree/master/src/maps) sisältää esimerkkikarttoja
* [`/tests`](https://github.com/valtterikantanen/tiralabra/tree/master/src/tests) sisältää ohjelmalle laaditut testitiedostot
* [`/ui/ui.py`](https://github.com/valtterikantanen/tiralabra/tree/master/src/ui/ui.py) sisältää käyttöliittymäkoodin

## Yleistä ohjelman käytöstä
Asennuksen jälkeen ohjelma käynnistetään komennolla `poetry run invoke start`. Graafisessa käyttöliittymässä ilmoitetaan lähtö- ja maaliruutujen koordinaatit pilkulla erotettuna (esim. `0,0`). Tämän jälkeen valitaan käytettävä algoritmi ja painetaan "Löydä lyhin reitti", jolloin ohjelma näyttää laskentaan käytetyn ajan ja löydetyn reitin pituuden. Ohjelma myös piirtää reitin karttaan. Alussa ruudut ovat joko valkoisia (vapaita) tai mustia (esteitä). Reitin löydyttyä lähtö- ja maaliruudut merkitään vihreällä, muut reittiin kuuluvat ruudut punaisella ja muut vieraillut ruudut keltaisella.

## Tietorakenteet ja algoritmit

### Dijkstran algoritmi
Dijkstran algoritmi on toteutettu yhdessä funktiossa, joka saa parametrinaan käytettävän verkon vieruslistaesityksenä, lähtösolmun ja maalisolmun. Aluksi alustetaan kaksi listaa, joista toinen pitää kirjaa vierailluista solmuista ja toinen tietoa siitä, mistä solmusta mihinkin solmuun on päästy. Tätä tietoa tarvitaan polun muodostamisessa. Lisäksi luodaan keko, johon lisätään alussa vain lähtösolmu, ja sanakirja, jossa ylläpidetään tietoa etäisyyksistä.

While-silmukkaa toistetaan kunnes keko on tyhjä tai maalisolmu löydetään. Näin voidaan toimia, sillä algoritmi toimii niin, että kun maalisolmu löydetään, siihen ei voi löytyä enää lyhyempiä reittejä. Näin on siksi, että keosta poistetaan aina solmu, johon on lähtösolmusta lyhin etäisyys. Jos kauempaa kiertämällä voisi löytyä lyhyempi etäisyys, jossakin kohdassa olisi oltava negatiivinen solmun paino, mikä ei ole Dijkstran algoritmissa sallittua.

Joka kierroksella keosta poistetaan siis solmu, jonka naapurit käydään vuorotellen läpi. Mikäli nykyisen solmun kautta naapurisolmuun on aiempaa lyhyempi reitti, naapurisolmun etäisyyttä korjataan alaspäin. Lisäksi naapurisolmu lisätään kekoon, mikäli etäisyyttä on muutettu.

Lopuksi muodostetaan vielä lista reitin muodostavista solmuista. Funktio palauttaa reitin, tiedon vierailluista solmuista sekä etäisyyden maalisolmuun.

### IDA\*-algoritmi

### Binäärikeko

## Aika- ja tilavaativuudet

## Suorituskykyvertailu
Dijkstran algoritmin toimintaa on testattu 930 eri syöttellä 256×256-kokoisessa kartassa. Kaikissa tapauksissa ohjelma löysi oikean lyhimmän reitin. Testaus tehtiin [esimerkkiskenaarioiden](https://github.com/valtterikantanen/tiralabra/blob/master/src/maps/Berlin_0_256.map.scen) avulla. 930 eri testitapauksen ajo kesti 240 sekuntia eli yhdessä tapauksessa kului aikaa  keskimäärin 0,258 sekuntia.

## Lähteet
Laaksonen, Antti: [_Tietorakenteet ja algoritmit_](https://raw.githubusercontent.com/hy-tira/tirakirja/master/tirakirja.pdf), s. 123–127.