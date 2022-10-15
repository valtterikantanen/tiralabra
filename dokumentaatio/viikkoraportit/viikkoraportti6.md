# Viikkoraportti 6

Tällä viikolla laajensin testejä erityisesti IDA\*-algoritmin osalta. Muokkasin myös suorituskykytestit Pytest-sovelluskehystä hyödyntäviksi, eli tuloksia ei enää kirjoiteta erilliseen tiedostoon. Lisäksi paransin koodin dokumentointia lisäämällä docstring-kommentointia ja kirjoitin toisen vertaisarvioinnin.

Kuluneella viikolla ongelmia aiheutti se, etten ole varma, toimiiko IDA\*-algoritmi oikein silloin kun maalisolmu on esteen ympäröimä, eli siihen ei ole polkua kaikista tyhjistä solmuista. Testit antavat oikean tuloksen, jos aloitussolmu on esteen ympäröimä. En tiedä kestääkö toiseen suuntaan kaikkien vaihtoehtojen tutkiminen vain pitkään, vai jääkö ohjelma pyörimään ikuisesti silmukkaan.

Edellä mainittua ongelmaa lukuun ottamatta algoritmit tuntuvat toimivan oikein ja omat vaaditut tietorakenteet on toteutettu. Tässä vaiheessa jäljellä onkin enää dokumentaation viimeistely ja suorituskykyvertailu algoritmien välillä. Jo tässä vaiheessa näyttää selvältä, että Dijkstran algoritmi löytää lyhimmän reitin lähes aina nopeammin kuin IDA\*, erityisesti jos verkko on laaja tai esteitä on paljon.

Kuluneella viikolla käytin työhön aikaa yksitoista tuntia.