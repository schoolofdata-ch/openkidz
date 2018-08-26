The [Truth WithIn STatistics 2018](https://twist2018.ch) hackathon was one of the first events of its kind that provided childcare during and as part of the event. Together with the carers from the University of Zürich ([kihz.uzh.ch](https://www.kihz.uzh.ch/)), during quiet hours, we investigated the question of whether event organizers or even parents in general had access to high quality data about childcare providers in Switzerland. We designed and published a [Data Package](https://frictionlessdata.io/field-guide/) which can be used to analyze, visualize, and crowdsource - ideally as part of an easy-to-use application - more information about childcare providers in Switzerland or worldwide.

---

> Heard of the TWIST Hackdays💻? It&#39;s a diversity-friendly Hackathon in Zurich, 25-26 August. Parents are also welcome to participate - there is even the possibility of full childcare service during the event👶 Carefree &amp; Happy Hacking! <a href="https://twitter.com/hashtag/hackdays?src=hash&amp;ref_src=twsrc%5Etfw">#hackdays</a> <a href="https://twitter.com/hashtag/TWIST2018?src=hash&amp;ref_src=twsrc%5Etfw">#TWIST2018</a>
> &mdash; Django Girls Zürich <a href="https://twitter.com/DjangoGirlsZH/status/1027451529266188293?ref_src=twsrc%5Etfw">9 août 2018</a>

![](https://pbs.twimg.com/media/DlbWJIVWwAE_IZT.jpg:large)
> &mdash; Being excellent to children at TWIST2018 <a href="https://twitter.com/TWIST2018/status/1033248634417172481">25 août 2018</a>

# Data

There are existing sources of statistical Open Government Data about childcare. By searching the [opendata.swiss portal](https://opendata.swiss/de/dataset?q=kinderbetreuung) we found a detailed list of day care centers in the City of Zürich sorted by school groups since 2014. Key figures in this dataset include the number of childcare places, the number of children of pre-school age, and the care rate per school group. See [data.stadt-zurich.ch](https://data.stadt-zuerich.ch/dataset/sd_zv_kitas_schulkreis)

The best starting point for researching detailed information about childcare centers is [KibeSuisse](https://www.kibesuisse.ch/verband/ueber-kibesuisse/kibesuisse-stellt-sich-vor/), the Swiss Childcare Association, which calls itself a competence center for family and school-accompanying childcare:

> "Kibesuisse fördert den qualitativen und quantitativen Ausbau familien- und schulergänzender Kinderbetreuungsangebote." *(Kibesuisse promotes the qualitative and quantitative expansion of family and school supplementary childcare services.)*

Note that there a number of interesting [research publications](https://www.kibesuisse.ch/publikationen/) on their homepage, where also the criteria for admission in the network and evaluation can be found. However, we could not find any open data on their website `:(` Lucky for us, they have a nicely designed web-accessible member database! `:)`. See the next section for details of how we created a new dataset on this basis, or the [research](#Research) section for further links.

# Preparation

On the member search web application maintained publicly by Kibesuisse we were able to see care centers on a map, do a search, filter by canton, and get basic contact information (city and URL) which we transformed into a spreadsheet. By scraping the web page source it is also possible to get a copy of the `JSON`-formatted detailed locations list that generates the map. See [kibesuisse.ch](https://www.kibesuisse.ch/verband/mitglieder/mitglieder-suchen/?tx_iskibesuissemitglieder_suche[action]=search&tx_iskibesuissemitglieder_suche[controller]=Mitglieder&tx_iskibesuissemitglieder_suche[canton]=ZG)

We opened the link to every child care provider in the Canton of Zug (because this is the location of our [next Hackdays](http://hack.opendata.ch/event/21#top) - and where we are planning to use this data to make recommendations), checked and corrected links, enhanced the original data with additional information, such as validation of membership in networks besides KibeSuisse, and brainstormed ideas for other data fields that would be useful to have.

We propose the following initial schema for this Data Package:

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

Feedback and further suggestions are [welcome](https://github.com/schoolofdata-ch/openkidz/issues).

# Research

Note that this database does not have to be constrained only to network members or certified providers, but includes columns for (last known) participation in such schemes. With expert consultation, we did basic research for the 'market need' for such a dataset, and came across [care4kids.ch](https://www.care4kids.ch/fuer-familien/animation-fur-einen-anlass/), which specifically provides [event services](https://www.care4kids.ch/fuer-familien/animation-fur-einen-anlass/). This is, however, a closed platform which cannot be directly searched - we do not want to argue with their reasons, but we do wish to provide more open alternatives.

In addition to KibeSuisse, there are other associations and certification providers in Switzerland, for example: [Qualikita](https://www.quali-kita.ch/de/fuer-eltern/zertifizierte-kitas/), [Purzelbaum](https://www.radix.ch/Gesunde-Schulen/Bewegung-und-Ernaehrung/Purzelbaum-Schweiz/Purzelbaum-KiTa/Pf3sM/?sesURLcheck=true) and - not only for childcare providers but for any institution that provides meals - [Fourchette Verte](http://www.fourchetteverte.ch/). Sometimes they list their members in a similar way to KibeSuisse, and we would like to support multiple networks in this dataset.

One of the partners of KibeSuisse, [Kitaclub AG](https://kitaclub.ch/), is a commercial portal that allows childcare centers to advertise themselves on a database which lists (at time of writing) 2996 kitas, day-families and play-groups in Switzerland, with 734 having detailed profiles. On a regional level, they have 153 entries for Zug (compare this with only 35 being listed on KibeSuisse). Besides the location shown on a map, location and contact details are not provided without a log in, and we saw no evidence of more advanced metadata shared.

An interesting source for research publications about childcare providers in Switzerland is [netzwerk kinderbetreuung](http://www.netzwerk-kinderbetreuung.ch/de/dossiers/27/). For an example of public discussion about childcare costs and quality, see this recent [Zentralplus article](https://www.zentralplus.ch/de/news/wirtschaft/5536600/Eigene-Kitas-bei-Zuger-Unternehmen-Fehlanzeige.htm).

Outside of Switzerland there are good examples of Open Data sources of this kind. The [Government of Alberta, Canada](https://open.alberta.ca/opendata/childcareinformation) provides child care information for programs which are licensed or approved by the Ministry, including location data, capacity, accreditation status, inspection dates, and details of any non-compliance issues and remedies. This creates transparency and ostensibly improves the level of childcare in the province. On the [New York City open data portal](https://data.cityofnewyork.us/widgets/3nxf-gbay) there is likewise detailed geodata on childcare centers.

The Ofsted department of the U.K. government goes to great lengths to share data and the tools to understand it in their [Statistics section](https://www.gov.uk/government/organisations/ofsted/about/statistics#data-view). The up-to-date [Childcare providers and inspections](https://www.gov.uk/government/statistics/childcare-providers-and-inspections-as-at-31-march-2018) dataset has a rich, well annotated schema, including:

- main findings in HTML, Word and PDF
- summary tables and charts in Excel format
- individual provider-level and inspection-level data in ODS format
- methodology and quality report in PDF format
- pre-release access list in PDF format

While we recognize the commitment to statistical excellence and raw data sharing shown by this agency, the raw data is not provided in simpler formats like CSV, and as far as we can tell, not yet well known in the open data community. Please contact us if you know of any projects or third-party analyses made with this or similar data source.

# Acknowledgments

![Logo](https://www.kihz.uzh.ch/dam/jcr:ffffffff-fad9-f04f-0000-000078c87d1e/kihz.jpg)

**Many thanks to Stefanie and Andrea from kihz.uhz.ch for the support and collaboration! They will be glad [to hear from you](https://www.kihz.uzh.ch/de/kitas.html) if you're organizing an event in Zürich.**

Further contributors to the project include [Gonzalo Casas](http://github.com/gonzalocasas), [Oleg Lavrovsky](http://github.com/loleg) and Anna Lamprou.

# License

According to the [Impressum page](https://www.kibesuisse.ch/footerlinks-rechts/impressum/) of KibeSuisse, the text and images on kibesuisse.ch are under copyright restriction, and not to be used without express written permission. Our republication of the data obtained legally from the public website and for demonstration purposes, is done under the principles of [Fair Use](https://de.wikipedia.org/wiki/Fair_Use) without malicious or commercial intentions.

If you intend to use any data mentioned here in a public or commercial product, please check with each of the data sources for any specific restrictions.

This Data Package is made available by its maintainers under the [Public Domain Dedication and License v1.0](http://www.opendatacommons.org/licenses/pddl/1.0/), a copy of the full text of which is in [LICENSE.md](LICENSE.md).
