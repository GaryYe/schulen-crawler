# schulen-crawler

A simple crawler that retrieves Austrian schools. 

## Usage

Simply install the modules in `requirements.txt` by using pip. 

Then start crawling the data by issuing the following command:

```
$ scrapy runspider schulen.py -o schulen.json
```

In total it will be around 1.1MB of school data. `head schulen.json` gives the
following output:

```
[
{"name": "Abendgymnasium - BG/BRG f\u00fcr Berufst\u00e4tige\t", "address": " Spittelwiese 14, 4020 Linz", "email": "s401116@eduhi.at", "homepage": "http://www.abendgym.at"},
{"name": "Akademie f\u00fcr den medizinisch-technischen Laboratoriumsdienst am Allgemeinen \u00f6ffentlichen Krankenhaus\t", "address": " Krankenhausstra\u00dfe 9, 4020 Linz", "email": null, "homepage": null},
{"name": "Akademie f\u00fcr den medizinisch-technischen Laboratoriumsdienst am a.\u00f6. Krankenhaus Wr. Neustadt\t", "address": " Corvinusring 20, 2700 Wiener Neustadt", "email": "mta@kh-wrn.ac.at", "homepage": null},
{"name": "Akademie f\u00fcr den logop\u00e4disch-phoniatrisch-audiologischen Dienst d. Landes Stmk. am LKH-Universit\u00e4tsk\t", "address": " Auenbruggerplatz 26, 8036 Graz", "email": null, "homepage": null},
{"name": "Akademie f\u00fcr den logop\u00e4disch-phoniatrisch-audiologischen Dienst am Ausbildungszentrum West\t", "address": " Innrain 98, 6020 Innsbruck", "email": null, "homepage": null},
{"name": "Akademie f\u00fcr den logop\u00e4disch-phoniatrisch-audiologischen Dienst am Allgemeinen \u00f6ffentlichen Krankenh\t", "address": " Krankenhausstra\u00dfe 9, 4020 Linz", "email": null, "homepage": null},
{"name": "Akademie f\u00fcr den log.-phon.-audiolog. Dienst - Berufsf\u00f6rderungsinstitut O\u00d6.\t", "address": " Peter-Roseggerstra\u00dfe 26, 4910 Ried i. Innkreis", "email": "logopaed.acad@bfi-ooe.at", "homepage": "http://www.bfi-ooe.at"},
{"name": "Akademie f\u00fcr den ergotherapeutischen Dienst an der Landesnervenklinik Sigmund Freud - Graz\t", "address": " Wagner-Jauregg-Platz 8, 8053 Graz", "email": null, "homepage": null},
{"name": "Akademie f\u00fcr den ergotherapeutischen Dienst an der Christian Doppler-Klinik Salzburg\t", "address": " Ignaz-Harrer-Stra\u00dfe 79, 5020 Salzburg", "email": "e.streitwieser@lks.at", "homepage": null},
```

