# Testausdokumentti

## Yksikkötestaus
Yksikkötestit voidaan suorittaa helposti käyttämällä [Pytest-sovelluskehystä](https://docs.pytest.org/en/7.1.x/). Testitiedostot sijaitsevat hakemistossa [`src/tests/`](https://github.com/valtterikantanen/tiralabra/blob/master/src/tests/). Yksikkötestit voi suorittaa projektin juurihakemistossa komennolla
```bash
poetry run invoke test
```
ja testikattavuusraportin voi generoida komennolla
```bash
poetry run invoke coverage-report
```

Tähän mennessä testausta on tehty:
* [Heap](https://github.com/valtterikantanen/tiralabra/blob/master/src/heap.py/)-luokalle, joka toteuttaa Dijkstran algoritmissa vaadittavan minimikeon
* [dijkstra.py](https://github.com/valtterikantanen/tiralabra/blob/master/src/dijkstra.py/)-tiedostolle, joka sisältää toteutuksen Dijkstran algoritmille
* [ida_star.py](https://github.com/valtterikantanen/tiralabra/blob/master/src/ida_star.py/)-tiedostolle, joka sisältää toteutuksen IDA\*-algoritmille

### Testikattavuus

Sovelluksen testikattavuus näyttää tällä hetkellä tältä:

![](./kuvat/testikattavuus.png)

Sovelluksen testauksen haaraumakattavuus on näin ollen 99 %. Testikattavuuden ulkopuolelle on jätetty käyttöliittymäkoodin sisältävä hakemisto `src/ui/` ja testaukseen käytettävän koodin sisältävä hakemisto `src/tests/` sekä tiedostot `__init__.py` ja `index.py`.

### Dijkstran algoritmin toiminnallisuuden testaus
Dijkstran algoritmin testaus on toteutettu niin, että esimerkkikarttojen yhteydessä samalta sivustolta on ladattu [esimerkkiskenaarioita](https://github.com/valtterikantanen/tiralabra/blob/master/src/maps/Berlin_0_256.map.scen), joista ilmenee 930 eri pisteparin väliset etäisyydet. Testauksen yhteydessä näistä valitaan satunnaisesti viisitoista, ja ohjelman antamaa tulosta verrataan tiedettyyn etäisyyteen. Testi on asetettu menemään läpi, jos etäisyydet ovat kuuden desimaalin tarkkuudella samat.
