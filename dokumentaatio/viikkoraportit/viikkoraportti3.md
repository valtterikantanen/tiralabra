# Viikkoraportti 3

Kuluneella viikolla loin ensimmäisen version ohjelman toiminnan visualisoinnista. Ohjelma osaa nyt näyttää graafisesti käytetyn kartan sekä löydetyn reitin. Toteutukseen on käytetty Pygame-kirjastoa.

Lisäksi laadin oman toteutukseni binäärikeolle ja luovuin standardikirjaston `heapq`-moduulin käytöstä. Omaa kekototeutustani käyttämällä 930 testitapauksen suorittaminen kesti 240 sekuntia, kun valmiilla toteutuksella aikaa kului 72 sekuntia. Näin ollen oma toteutukseni oli yli kolme kertaa standardikirjastoa hitaampi. En keksinyt, mikä [omassa versiossani](https://github.com/valtterikantanen/tiralabra/blob/master/src/heap.py) olisi toiminut tarpeettoman hitaasti, mutta huomasin, että [`heapq`-moduuli](https://github.com/python/cpython/blob/db39050396a104c73d0da473a2f00a62f9dfdfaa/Lib/heapq.py#L581) käyttää oletuksena C-kielistä toteutusta. Näin ollen uskon, että tämä pitkälti selittää tehokkuuserot, koska tunnetusti C on paljon tehokkaampi ohjelmointikieli kuin Python.

Onneksi ohjelman käytön kannalta olennaista ei ole 930 testitapauksen suorittaminen mahdollisimman nopeasti. Yhden reitin etsinnässä ajat olivat noin 0,4 sekuntia ja 0,3 sekuntia valmiin toteutuksen hyväksi, mitä en pidä vielä merkittävänä huononnuksena.

Tällä viikolla laadin myös tähän mennessä kirjoitetulle koodille kattavat testit ja tein ensimmäisen version testausdokumentista.

Seuraavana askeleena on IDA\*-algoritmin toteutuksen aloittaminen. Koska kyseessä on minulle täysin tuntematon algoritmi, perehdyn ensin itse algoritmiin tarkemmin, minkä jälkeen alan laatia ensimmäistä versiota algoritmista.

Kuluneella viikolla käytin työhön aikaa yhdeksän tuntia.