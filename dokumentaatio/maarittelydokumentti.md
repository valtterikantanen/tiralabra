# Määrittelydokumentti

Harjoitustyön aiheena on reitinhaku. Tarkoituksena on kehittää sovellus, joka löytää nopeimman tai lyhimmän reitin kahden pisteen välillä. Reitinhaussa hyödynnetään kahta algoritmia: Dijkstran algoritmia ja IDA\*-algoritmia. Sovellus vertaa näiden algoritmien antamia tuloksia ja tehokkuutta. Algoritmit on valittu siksi, että ne ovat yleisiä reitinhaussa käytettyjä algoritmeja.

Sovellus laaditaan täysin Python-ohjelmointikielellä. Ainakin Dijkstran algoritmissa vaadittava prioriteettijono toteutetaan itse kekorakennetta hyödyntäen.

Syötteenä ohjelma saa kartan sekä alku- ja loppupisteen, joiden välinen reitti halutaan optimoida. Pisteet voi valita myös graafisen käyttöliittymän avulla. Lisäksi algoritmien toimintaa visualisoidaan graafisesti.

Ohjelmassa pyritään Dijkstran algoritmin aikavaativuuteen $O(|E| + |V| \log|V|)$, missä $|V|$ on verkon solmujen lukumäärä ja $|E|$ kaarten lukumäärä. IDA\*-algoritmi on A\*-algoritmin versio, joka pyrkii käyttämään minimaalisen määrän muistia haun aikana. Algoritmi perustuu rajoitettuun syvyyshakuun ja heuristiikkaan, jolla arvioidaan matkaa maalisolmuun. IDA\*-algoritmi ei tarvitse monimutkaisia tietorakenteita ja käyttää vähän muistia, joten se käy solmuja läpi erittäin nopeasti.

## Kurssiin liittyviä seikkoja

Projektin dokumentaatio (mukaan lukien docstring-kommentit) laaditaan suomeksi. Luokkien, funktioiden, muuttujien ym. nimeäminen tehdään yleisen käytännön mukaisesti englanniksi.

Harjoitustyön laatijan opinto-ohjelma on tietojenkäsittelytieteen kandiohjelma. En osaa Pythonin lisäksi muita kieliä tarpeeksi, jotta voisin vertaisarvioida muilla kielillä laadittuja projekteja.

## Lähteet

Torikka, Oskari: [_A*-algoritmi ja siihen pohjautuvat muistirajoitetut heuristiset reitinhakualgoritmit_](https://erepo.uef.fi/bitstream/handle/123456789/14693/urn_nbn_fi_uef-20150206.pdf?sequence=1&isAllowed=y)

Laaksonen, Antti: [_Tietorakenteet ja algoritmit_](https://raw.githubusercontent.com/hy-tira/tirakirja/master/tirakirja.pdf)

Kord, Richard ym.: [_Time complexity of iterative-deepening-A∗_](https://www.sciencedirect.com/science/article/pii/S0004370201000947/pdf?md5=6685f651efae7e0f243de5d7d4522aba&pid=1-s2.0-S0004370201000947-main.pdf)

[_Iterative deepening A*_](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
