The [Truth WithIn STatistics 2018](https://twist2018.ch) hackathon was one of the first events of its kind that provided a childcare facility as part of the event. Together with the childcare team from the University of Zürich that supported the event ([kihz.uzh.ch](https://www.kihz.uzh.ch/)), we investigated the question of whether event organizers or even parents in general had access to open data about childcare providers in Switzerland, and decided to make open data. The result is a [Data Package](https://frictionlessdata.io/field-guide/) which can be used to analyze, visualize, and crowdsource more information about childcare providers in Switzerland or worldwide.

<blockquote class="twitter-tweet" data-lang="fr"><p lang="en" dir="ltr">Heard of the TWIST Hackdays💻? It&#39;s a diversity-friendly Hackathon in Zurich, 25-26 August. Parents are also welcome to participate - there is even the possibility of full childcare service during the event👶 Carefree &amp; Happy Hacking! <a href="https://twitter.com/hashtag/hackdays?src=hash&amp;ref_src=twsrc%5Etfw">#hackdays</a> <a href="https://twitter.com/hashtag/TWIST2018?src=hash&amp;ref_src=twsrc%5Etfw">#TWIST2018</a></p>&mdash; Django Girls Zürich (@DjangoGirlsZH) <a href="https://twitter.com/DjangoGirlsZH/status/1027451529266188293?ref_src=twsrc%5Etfw">9 août 2018</a></blockquote>

![](https://pbs.twimg.com/media/DlbWJIVWwAE_IZT.jpg:large)
&mdash; TWIST2018 (@TWIST2018) <a href="https://twitter.com/TWIST2018/status/1033248634417172481">25 août 2018</a>

# Data

Note that there are sources of statistical Open Government Data about childcare, for example searching the [Opendata.swiss portal](https://opendata.swiss/de/dataset?q=kinderbetreuung) we found a detailed list of day care centers in the City of Zürich on the basis of key figures according to school groups since 2014. Key figures in this dataset include the number of childcare places, the number of children of pre-school age and the care rate per school group. See [data.stadt-zurich.ch](https://data.stadt-zuerich.ch/dataset/sd_zv_kitas_schulkreis)

The best starting point for researching detailed information about childcare centers is [KibeSuisse](https://www.kibesuisse.ch/verband/ueber-kibesuisse/kibesuisse-stellt-sich-vor/), the Swiss Childcare Association, which calls itself a competence center for family and school-accompanying childcare:

> "Kibesuisse fördert den qualitativen und quantitativen Ausbau familien- und schulergänzender Kinderbetreuungsangebote." *(Kibesuisse promotes the qualitative and quantitative expansion of family and school supplementary childcare services.)*

Note that there a number of interesting [research publications](https://www.kibesuisse.ch/publikationen/) on their homepage, where criteria for admission in the network and evaluation can be found. However, we could not find any open data on their website `:(` But lucky for us, they have a nice member database! `:)`. See the next section for details of how we opened this data, or the [research](#Research) section for more links.

# Preparation

On the member search web application maintained publicly by Kibesuisse we were able to see care centers on a map, do a search, filter by canton, and get basic contact information (city and URL) which we transformed into a spreadsheet. By scraping the web page source it is also possible to get a copy of the `JSON`-formatted detailed locations list that generates the map. See [kibesuisse.ch](https://www.kibesuisse.ch/verband/mitglieder/mitglieder-suchen/?tx_iskibesuissemitglieder_suche[action]=search&tx_iskibesuissemitglieder_suche[controller]=Mitglieder&tx_iskibesuissemitglieder_suche[canton]=ZG)

We propose the following basic schema for this Data Package:

- **Land/Kanton/Ort** - localisation information, which we will expand with georeferences via `data/locations-only.csv`
- **URL** - original web address obtained from the database
- **Kibesuisse** - 'Ja' if this childcare is part of the Kibesuisse network
- **QualiKita** - 'Ja' if this childcare is part of the QualiKita network
- **Qualis** - 'Ja' if this childcare is part of the Qualis network
- **Purzelbaum** - 'Ja' if this childcare is part of the Purzelbaum network
- **Fourchette Verte** - 'Ja' if this childcare is certified by Fourchette Verte
- **Pädagogisches Konzept** - a link, if available, to the explanation of the childcare concept
- **Tarife** - a link, if available, to the cost structure
- **Ernährungsprinzip** - a link, if available, to the dietary concept
- **Altersgruppe** - what age groups the centre caters to
- **Anzähl Plätze** - statistic of number of places available
- **Zeitfenster** - whether they work on demand or on weekends
- **Mindestbetreuung** - if there is a minimum number of days per week requirement
- **Mehrsprachigkeit** - if they have multilingual carers (come to the [Hackdays](https://hack.opendata.ch/event/22)!)
- **Subventionen** - whether reduced-cost places are available.

Feedback and suggestions are welcome on this schema.

# Research

Note that this database does not have to be constrained only to network members or certified providers, but includes columns for (last known) participation in such schemes. We also researched the 'market need' for such a dataset, and came across [care4kids.ch](https://www.care4kids.ch/fuer-familien/animation-fur-einen-anlass/), which for example specifically provides [event services](https://www.care4kids.ch/fuer-familien/animation-fur-einen-anlass/). It is, however, a closed platform which cannot be directly searched - we do not want to argue with their reasons, but we do wish to provide a more open alternative.

In addition to Kibesuisse, there are other associations and certification providers, for example: [Qualikita](https://www.quali-kita.ch/de/fuer-eltern/zertifizierte-kitas/), [Purzelbaum](https://www.radix.ch/Gesunde-Schulen/Bewegung-und-Ernaehrung/Purzelbaum-Schweiz/Purzelbaum-KiTa/Pf3sM/?sesURLcheck=true) and - not only for childcare providers but for any institution that provides meals - [Fourchette Verte](http://www.fourchetteverte.ch/). They list their members in a similar way. We went through every child care provider in the Canton of Zug (because this is the location of our [next Hackdays](http://hack.opendata.ch/event/21#top) - and where we are planning to use this data to make recommendations), checked and corrected links, enhanced the original data with additional information, and brainstormed ideas for other data that would be useful to know. This is detailed in the schema below, and the result is published in this Data Package.

Another source for research publications about childcare providers in Switzerland is [netzwerk kinderbetreuung](http://www.netzwerk-kinderbetreuung.ch/de/dossiers/27/).

For an example of public discussion about childcare costs and quality, see this recent [Zentralplus article](https://www.zentralplus.ch/de/news/wirtschaft/5536600/Eigene-Kitas-bei-Zuger-Unternehmen-Fehlanzeige.htm).

## Special thanks

![Logo](https://www.kihz.uzh.ch/dam/jcr:ffffffff-fad9-f04f-0000-000078c87d1e/kihz.jpg)

*Vielen dank zu **Stefanie** und **Andrea** von kihz.uhz.ch für das spannende Zusammenarbeit `:D` Für die nächste Hackdays freuen Sie sich [auf unseres Kontakt](https://www.kihz.uzh.ch/de/kitas.html)!*

# License

According to the [Impressum page](https://www.kibesuisse.ch/footerlinks-rechts/impressum/) of KibeSuisse, the text and images on kibesuisse.ch are copyright, and not to be used without express written permission. Our republication of the data for demonstration purposes is under the principles of [Fair Use](https://de.wikipedia.org/wiki/Fair_Use), and is done without intention to commercial intent.

The licensing terms of this dataset have not yet been established. If you intend to use these data in a public or commercial product, check with each of the data sources for any specific restrictions.

This Data Package is made available by its maintainers under the [Public Domain Dedication and License v1.0](http://www.opendatacommons.org/licenses/pddl/1.0/), a copy of the full text of which is in [LICENSE.md](LICENSE.md).
