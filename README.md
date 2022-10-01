# Reitinhakusovellus

Sovellus on laadittu Helsingin yliopiston syksyn 2022 kurssille [Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit](https://tiralabra.github.io/2022_p1/).

## Dokumentaatio

* [Määrittelydokumentti](https://github.com/valtterikantanen/tiralabra/blob/master/dokumentaatio/maarittelydokumentti.md)
* [Testausdokumentti](https://github.com/valtterikantanen/tiralabra/blob/master/dokumentaatio/testausdokumentti.md)

### Viikkoraportit

* [Viikko 1](https://github.com/valtterikantanen/tiralabra/blob/master/dokumentaatio/viikkoraportit/viikkoraportti1.md)
* [Viikko 2](https://github.com/valtterikantanen/tiralabra/blob/master/dokumentaatio/viikkoraportit/viikkoraportti2.md)
* [Viikko 3](https://github.com/valtterikantanen/tiralabra/blob/master/dokumentaatio/viikkoraportit/viikkoraportti3.md)
* [Viikko 4](https://github.com/valtterikantanen/tiralabra/blob/master/dokumentaatio/viikkoraportit/viikkoraportti4.md)

## Asennus ja käyttö

### Alkutoimet

Varmista tarvittaessa, että tietokoneellesi on asennettu [Poetry](https://python-poetry.org/). Tämän voi tehdä komennolla `poetry --version`, jonka tulisi tulostaa asennettu versio. Jos Poetrya ei ole asennettu, esimerkiksi [Ohjelmistotekniikka-kurssin materiaalista](https://ohjelmistotekniikka-hy.github.io/python/viikko2#poetry-ja-riippuvuuksien-hallinta) voi katsoa ohjeet asennukseen.

Aloita lataamalla sovelluksen lähdekoodi [zip-tiedostona](https://github.com/valtterikantanen/tiralabra/archive/refs/heads/master.zip) tai kloonaa projekti komennolla

```bash
$ git clone https://github.com/valtterikantanen/tiralabra.git
```
Mene projektin juurihakemistoon ja asenna tarvittavat kirjastot komennolla
```
$ poetry install
```

### Käyttö

Ohjelman käynnistäminen
```
$ poetry run invoke start
```
Testien suorittaminen
```
$ poetry run invoke test
```
Testikattavuusraportin luominen
```
$ poetry run invoke coverage-report
```
Pylint-tarkistusten suorittaminen
```
$ poetry run invoke lint
```

## Huomautuksia

Ohjelman testaukseen käytetyt [kartat ja testireitit](https://github.com/valtterikantanen/tiralabra/blob/master/src/maps) on ladattu [Moving AI Labin](https://www.movingai.com/benchmarks/index.html) kotisivuilta. Kartat on lisensoitu [Open Data Commons Attribution License](https://opendatacommons.org/licenses/by/1-0/) -lisenssillä.