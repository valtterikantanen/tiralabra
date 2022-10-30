# Toteutusdokumentti

## Ohjelman rakenne

Projektin rakenne on seuraava:
```
src
├── algorithms
│   ├── dijkstra.py
│   └── ida_star.py
├── index.py
├── maps
│   ├── Berlin_0_256.map
│   ├── Berlin_0_256.map.scen
│   ├── Map_20.map
│   ├── Map_5.map
│   └── perf_test_maps
│       ├── map1.map
│       ├── map2.map
│       ├── map3.map
│       └── map4.map
├── services
│   └── ui_logic.py
├── tests
│   ├── dijkstra_test.py
│   ├── heap_test.py
│   ├── ida_star_test.py
│   ├── ui_logic_test.py
│   └── performance_tests
│       ├── dijkstra_test_all_cases.py
│       └── main_perf_test.py
├── ui
│   └── ui.py
└── util
    ├── graph.py
    └── heap.py
```

Osien toiminta on pääasiassa seuraavanlainen:

* [`dijkstra.py`](https://github.com/valtterikantanen/tiralabra/blob/master/src/dijkstra.py) ja [`ida_star.py`](https://github.com/valtterikantanen/tiralabra/blob/master/src/ida_star.py) vastaavat Dijkstran algoritmin ja IDA\*-algoritmin toteutuksista
* [`graph.py`](https://github.com/valtterikantanen/tiralabra/blob/master/src/graph.py) vastaa tekstimuotoisten karttojen muuttamisesta verkoksi vieruslistaesitystä käyttäen
* [`heap.py`](https://github.com/valtterikantanen/tiralabra/blob/master/src/heap.py) vastaa Dijkstran algoritmissa tarvittavan binäärikeon toteutuksesta
* [`ui_logic.py`](https://github.com/valtterikantanen/tiralabra/blob/master/src/services/ui_logic.py) vastaa käyttöliittymälogiikasta
* [`index.py`](https://github.com/valtterikantanen/tiralabra/blob/master/src/index.py) käynnistää ohjelman toiminnan
* [`/maps/`](https://github.com/valtterikantanen/tiralabra/tree/master/src/maps) sisältää esimerkkikarttoja
* [`/tests/`](https://github.com/valtterikantanen/tiralabra/tree/master/src/tests) sisältää ohjelmalle laaditut testitiedostot (alikansio [`/performance_tests/`](https://github.com/valtterikantanen/tiralabra/tree/master/src/tests/performance_tests) sisältää suorituskykyä mittaavia testejä)
* [`/ui/ui.py`](https://github.com/valtterikantanen/tiralabra/tree/master/src/ui/ui.py) sisältää käyttöliittymäkoodin

## Yleistä ohjelman käytöstä
Asennuksen jälkeen ohjelma käynnistetään komennolla `poetry run invoke start`. Graafisessa käyttöliittymässä ilmoitetaan lähtö- ja maaliruutujen koordinaatit pilkulla erotettuna (esim. `0, 0`). Tämän jälkeen valitaan käytettävä algoritmi ja painetaan "Löydä lyhin reitti", jolloin ohjelma näyttää laskentaan käytetyn ajan ja löydetyn reitin pituuden. Ohjelma myös piirtää reitin karttaan. Alussa ruudut ovat joko valkoisia (vapaita) tai mustia (esteitä). Reitin löydyttyä lähtö- ja maaliruudut merkitään vihreällä, muut reittiin kuuluvat ruudut punaisella ja muut vieraillut ruudut keltaisella.

Yksityiskohtaisemmat ohjeet ovat [käyttöohjeessa](https://github.com/valtterikantanen/tiralabra/blob/master/dokumentaatio/kayttoohje.md).

## Tietorakenteet ja algoritmit

### Binäärikeko
Keko on toteutettu minimikekona, joka mahdollistaa pienimmän alkion löytymisen nopeasti. Kun kekoon lisätään tai siitä poistetaan alkio, palautetaan voimaan niin sanottu kekoehto. Kekoehdon mukaan minimikeossa solmun lapsien täytyy olla vähintään yhtä suuret kuin vanhempansa. Esimerkiksi solmulla, jonka arvo on 8, voi olla lapset arvoltaan 8 ja 10, mutta ei lapsia, joiden arvot ovat 7 ja 5.

Binäärikeko on toteutettu binääripuuna, ja pohjimmiltaan se on tallennettu tavallisena listana. Pienin alkio on aina indeksissä 1 (indeksi 0 on tyhjä). Yleisesti, jos alkio on indeksissä $k$, niin sen lapsien indeksit ovat $2k$ (vasen lapsi) ja $2k+1$ (oikea lapsi) ja vanhempi sijaitsee indeksissä $\lfloor k/2 \rfloor$.

Uusi alkio lisätään aluksi seuraavaan vapaana olevaan paikkaan. Tämän jälkeen alkiota nostetaan ylöspäin, kunnes kekoehto on jälleen voimassa. Vastaavasti kun pienin alkio poistetaan keon juuresta, siirretään aluksi keon viimeinen alkio uudeksi juureksi. Tämän jälkeen alkiota lasketaan alaspäin, kunnes kekoehto on jälleen voimassa.

Alkion lisäämisen ja poistamisen lisäksi keossa on metodi keon koon selvittämiselle sekä metodi, joka kertoo, onko keko tyhjä vai ei.

### Dijkstran algoritmi
Dijkstran algoritmi on toteutettu yhdessä funktiossa, joka saa parametreina käytettävän verkon vieruslistaesityksenä, lähtösolmun ja maalisolmun. Aluksi alustetaan kaksi listaa, joista toinen pitää kirjaa vierailluista solmuista ja toinen tietoa siitä, mistä solmusta mihinkin solmuun on päästy. Tätä tietoa tarvitaan polun muodostamisessa. Lisäksi luodaan keko, johon lisätään alussa vain lähtösolmu, ja sanakirja, jossa ylläpidetään tietoa etäisyyksistä.

While-silmukkaa toistetaan kunnes keko on tyhjä tai maalisolmu löydetään. Näin voidaan toimia, sillä algoritmi toimii niin, että kun maalisolmu löydetään, siihen ei voi löytyä enää lyhyempiä reittejä. Näin on siksi, että keosta poistetaan aina solmu, johon on lähtösolmusta lyhin etäisyys. Jos kauempaa kiertämällä voisi löytyä lyhyempi etäisyys, jossakin kohdassa olisi oltava negatiivinen solmun paino, mikä ei ole Dijkstran algoritmissa sallittua.

Joka kierroksella keosta poistetaan siis solmu, jonka naapurit käydään vuorotellen läpi. Mikäli nykyisen solmun kautta naapurisolmuun on aiempaa lyhyempi reitti, naapurisolmun etäisyyttä korjataan alaspäin. Lisäksi naapurisolmu lisätään kekoon, mikäli etäisyyttä on muutettu.

Lopuksi muodostetaan vielä lista reitin muodostavista solmuista. Funktio palauttaa reitin, tiedon vierailluista solmuista sekä etäisyyden maalisolmuun.

### IDA\*-algoritmi
IDA\*-algoritmin toiminta on jaettu kahteen funktioon: `ida_star`-pääfunktioon ja rekursiiviseen `_search`-funktioon. Pääfunktio saa parametreina käytettävän verkon vieruslistaesityksenä, lähtösolmun ja maalisolmun. Rekursiivisen funktion parametreina on käytettävä verkko, polun nykyinen pituus (g-arvo), hakuraja eli tutkittavien polkujen maksimipituus, etsittävä solmu sekä tutkittava polku.

Aluksi tarkistetaan, onko joko lähtö- tai maalisolmussa este. Jos on, funktiosta palataan välittömästi, koska mitään reittiä ei voi löytyä. Varsinaisen algoritmin toiminta alkaa lyhimmän mahdollisen reitin pituuden määrittämisellä, missä käytetään apuna `_estimate_shortest_path`-funktiota. Funktio laskee lyhimmän mahdollisen etäisyyden seuraavasti:
* Ensin liikutaan mahdollisimman paljon viistoon, kunnes ollaan samalla vaaka- tai pystyakselilla kuin maaliruutu (yhden siirtymän pituus on $\sqrt{2}$)
* Tämän jälkeen loppuosa matkasta on ainoastaan vaaka- tai pystysuuntaisia siirtymiä (yhden siirtymän pituus on 1)

Algoritmin kannalta on tärkeää, että heuristinen arvio on määritelty oikein (eli heuristiikka on luvallinen). Toisin sanoen arvio ei koskaan saa olla yläkanttiin, koska muuten lyhintä reittiä ei välttämättä löydetä.

Reitti alustetaan niin, että siihen asetetaan aloitussolmu. Tämän jälkeen rekursiivista funktiota kutsutaan uudelleen niin kauan, kunnes maalisolmu on löytynyt tai on todettu, ettei reittiä ylipäänsä voi löytyä. Muussa tapauksessa tutkittavien polkujen maksimipituutta kasvatetaan joka kierroksella. Uudeksi hakurajaksi tulee kaikista löydetyistä reiteistä lyhimmän pituus (joka on kuitenkin suurempi kuin edellisen kierroksen raja).

Rekursiivinen funktio toimii niin, että polun viimeisestä solmusta lähtien aletaan tarkastella mahdollisia reittiä. Uusi arvio aloitus- ja maalisolmun etäisyydestä (f-arvo) lasketaan lisäämällä polun nykyiseen pituuteen (g-arvo) heuristinen arvio nykyisen solmun ja maalisolmun välisestä etäisyydestä. Jos näin saatu arvo on suurempi, kuin kullakin hetkellä voimassa oleva raja, palautetaan f-arvo. Vastaavasti jos ollaan saavutettu maalisolmu, tiedetään, että ollaan löydetty lyhin reitti, joten tässäkin tapauksessa voidaan palata pääfunktioon.

Muussa tapauksessa aletaan selvittää, mikä olisi lyhimmän reitin pituus, joka on kuitenkin pidempi kuin tämänhetkinen raja ja johon päästään nykyisestä solmusta. Tämä tapahtuu käymällä nykyisen solmun naapurit läpi, ja tutkimalla rekursiivisesti syvyyshaulla ne solmut, jotka eivät tällä hetkellä kuulu reittiin. Kun vaihtoehdot on tutkittu, palautetaan lyhimmän löydetyn reitin pituus.

## Saavutetut aika- ja tilavaativuudet

### Keko
Binääripuun rakenne mahdollista pienimmän alkion löytymisen ajassa $O(1)$, koska pienin alkio on aina keon juuressa. Alkion poistaminen ja lisääminen tapahtuvat ajassa $O(\log n)$, missä $n$ on keon alkioiden määrä. Tällöin tasojen määrä keossa on $O(\log n)$, ja pahimmassa tapauksessa lisäyksen tai poiston yhteydessä alkio joudutaan siirtämään ylimmältä tasolta alimmalle tai toisin päin.

### Dijkstran algoritmi
Algoritmi käy läpi verkon solmut ja kaaret, mihin kuluu aikaa $O(|E| + |V|)$, missä $|E|$ on kaarten lukumäärä ja $|V|$ solmujen lukumäärä. Pahimmassa tapauksessa jokainen kaari joudutaan lisäämään vuorollaan kekoon, mihin kuluu aikaa $O(|E| \log |E|)$, sillä yksi lisäys vie aikaa $O(\log |E|)$. Vastaavasti pahimmassa tapauksessa reitin löytämiseksi joudutaan mahdollisesti poistamaan keosta jokainen alkio, mihin kuluu aikaa myös $O(|E| \log |E|)$. Tästä saadaan aikavaativuus $O(|E| + |V|) + O(|E| \log |E|) + O(|E| \log |E|) = O(|E| + |V|) + O(2 |E| \log 2 |E|) = O(|E| \log |E| + |V|)$.

Pahimmassa tapauksessa kekoon on talletettu samanaikaisesti kaikki kaaret. Toteutuksessa solmusta voi lähteä enintään kahdeksan kaarta, joten pahimman tapauksen tilavaativuudeksi saadaan $O(8 |V|) = O(|V|)$, missä $|V|$ on solmujen lukumäärä.

### IDA\*-algoritmi
Algoritmin aikavaativuus riippuu ongelmasta sekä siitä, kuinka hyvin heuristiikkafunktio toimii kyseiseen ongelmaan. Yleisesti ottaen pahimman tapauksen aikavaativuus on $O(b^d)$, missä $b$ on niin sanottu haarautumiskerroin (*branching factor*) ja $d$ lyhimpään reittiin kuuluvien solmujen määrä. Tässä projektissa haarautumiskerroin on yleisesti ottaen kahdeksan, koska jokaisesta solmusta lähtee enintään kahdeksan kaarta.

Näin ollen aikavaativuus on eksponentiaalinen polun pituuteen nähden. Mitä lähempänä heuristinen arvio on todellista lyhimmän reitin pituutta, sitä vähemmän laskentakierroksia tarvitsee tehdä. Esimerkiksi siinä tapauksessa, että heuristiikkafunktio antaa suoraan lyhimmän polun pituuden, riittää yksi kierros. Tästä syystä IDA\* on hyvin nopea silloin, kun lähtö- ja maalisolmun välillä ei ole lainkaan esteitä, koska tällöin toteutettu heuristiikka antaa suoraan lyhimmän polun pituuden. Haasteeksi nouseekin se, miten matkalla mahdolliset olevat esteet voisi huomioida heuristiikassa, jotta kaikista lyhimpiä reittiä ei tarvitsisi tutkia lainkaan.

Tilavaativuus on parempi kuin Dijkstran algoritmissa, sillä tallennettuna on ainoastaan kullakin hetkellä tutkittava polku. Näin ollen tilavaativuus on lineaarinen suhteessa lyhimmän reitin pituuteen eli $O(n)$, missä $n$ on lyhimpään reittiin kuuluvien solmujen määrä. Tämä kuitenkin johtaa siihen, että samoja solmuja joudutaan käymään läpi useaan kertaan.

## Suorituskykyvertailu

Tarkemmat tiedot käytetyistä testisyötteistä ja tuloksista ovat [testausdokumentissa](testausdokumentti.md).

Testeissä huomattiin, että mitä pienempi kartta ja mitä vähemmän esteitä, sitä nopeammin IDA\* löytää lyhimmän reitin. Esimerkiksi tyhjässä 10×10-kokoisessa kartassa ja 10 000 reitin sarjoilla IDA\* oli kaikissa tilanteissa hitaimmillaankin yli 5 kertaa Dijkstraa nopeampi.

Testeissä myös huomattiin, että Dijkstran algoritmi nopeutui esteiden määrän lisääntyessä. Tämä on ymmärrettävää, koska tällöin verkossa on vähemmän kaaria ja ne voidaan käydä nopeammin läpi.

Kartan koon ja esteiden määrän kasvaessa Dijkstran algoritmin suorituskyky pysy suhteellisen samana, kun taas IDA\*-algoritmissa hitaimmat tapaukset erottuvat hyvin selvästi. Esimerkiksi vain yksittäisiä esteitä sisältävässä 20×20-kokoisessa kartassa reitin löytäminen vei IDA\*-algoritmilta pahimmillaan yli 14 sekuntia, kun Dijkstran algoritmi selviytyi kaikista tapauksista alle 2,5 millisekunnissa.

Jos IDA\*-algoritmin heuristiikassa huomioitaisiin jollain tavalla esteiden määrä reitillä, saataisiin myös algoritmin suorituskykyä paremmaksi. Näyttää siltä, että jos kartan koosta tai esteiden määrästä ei ole lisätietoja, on Dijkstran algoritmi yleispätevämpi, vaikka se onkin mediaanitapauksessa hitaampi. 

## Parannusehdotuksia
Yksi selkeä parannus olisi IDA\*-algoritmiin liittyvän heuristiikkafunktion kehittäminen. Tällä hetkellä esimerkiksi esteiden määrää reitillä ei oteta lainkaan huomioon, vaan funktio palauttaa samoille alku- ja päätepisteille aina saman etäisyysarvion. Tämä hidastaa huomattavasti reittien läpikäymistä tilanteissa, joissa esteitä on runsaasti eli arvio ja todellinen lyhin reitti eroavat paljon toisistaan.

## Lähteet
Korf, Richard ym.: *Time complexity of iterative-deepening-A\**. Artificial Intelligence, 129 (1–2): 199–218. 2001. DOI: [10.1016/S0004-3702(01)00094-7](https://doi.org/10.1016/S0004-3702(01)00094-7).

Laaksonen, Antti: [_Tietorakenteet ja algoritmit_](https://raw.githubusercontent.com/hy-tira/tirakirja/master/tirakirja.pdf), s. 123–127.

Myllyoja, Henri: [_Binääri- ja Fibonacci-keot prioriteettijonon toteutukseen_](https://trepo.tuni.fi/bitstream/handle/123456789/25515/myllyoja.pdf?sequence=4&isAllowed=y). Kandidaatintyö. Tampereen teknillinen yliopisto, tieto- ja sähkötekniikan tiedekunta, 2018.