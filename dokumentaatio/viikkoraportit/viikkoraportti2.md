# Viikkoraportti 2

Tällä viikolla palautin mieleeni Dijkstran algoritmin toimintaa ja laadin algoritmista ensimmäisen version. Käytin vielä tässä vaiheessa Pythonin standardikirjaston `heapq`-moduulia algoritmin tarvitsevan keon muodostamiseen ja ylläpitoon, koska halusin ensin varmistua siitä, että algoritmi toimii muilta osin oikein.

Tällä hetkellä ohjelma osaa muuttaa .map-muotoisen kartan rivit ensin listoiksi ja sen jälkeen laatia vieruslistat jokaiselle ruudulle (eli verkon solmulle). Myös Dijkstran algoritmi on toteutettu kokonaan lukuun ottamatta itse toteutettua binäärikekoa, joka oli edellytyksenä Dijkstran algoritmin käyttämiselle.

Latasin [Moving AI Labin](https://www.movingai.com/benchmarks/grids.html) kotisivuilta 256×256-kokoisen .map-muotoisen kartan ja katsoin, antaako algoritmi samoja tuloksia kuin kartan yhteydessä listatut esimerkkireitit. Alussa joidenkin reittien pituuksissa oli pieniä epätarkkuuksia. Ymmärsin varsin pian, etten ollut huomioinut sitä, että reitti ei voi kulkea esimerkiksi yläviistoon oikealle, jos ylhäällä tai oikealla on este. Tämän korjauksen jälkeen tulokset olivat käytännössä samoja. Suurin ero tuloksissa oli noin $7{,}4 \cdot 10^{-8}$, mitä voidaan pitää pyöristysvirheenä tai eri $\sqrt{2}$:n arvojen käytöstä johtuvana.

Seuraavalla viikolla aion ottaa selvää, miten reitinhaun visualisointi kannattaa toteuttaa. Tällä hetkellä mielessäni on lähinnä Pygame-kirjaston käyttö. Uskon, että visualisointi tulee viemään minulta enemmän aikaa kuin itse algoritmien toteutus. Mikäli aikaa jää, aloitan binäärikeon toteuttamisen tai alan tutkia IDA\*-algoritmia tarkemmin.

Tällä viikolla käytin työhön aikaa yksitoista tuntia.