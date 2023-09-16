---
alias:
tag: CodeNotebook
---

from [Jirka Mayer, prof. from MFF UK](https://github.com/Jirka-Mayer/NPRG030-062/blob/master/prg/zapoctaky.md)

# Zápočťáky

- chci od každého téma do konce listopadu
    - tzn. chci aby mi každý poslal (resp. jsme se dohodli na) *specifikaci zápočtového programu*
    - specifikací se rozumí stručný popis toho, co by váš program měl dělat
    - specifikace je to, co rozhodne, jestli jste napsali program, který se po vás chtěl, nebo ne
    - specifikace by měla obsahovat radši méně věcí. Lepší nakonec dodat víc než bylo slíbeno, než nedodat něco co mělo být dodáno.
    - Např.: "Implementuji hru carcassonne v prostředí pygame. Hra bude pro dva a více živých hráčů, tzn. nebude obsahovat umělou inteligenci. Detailní pravidla hry jsou na adrese -url-."
    - Např.: "Implementuji first-person-shooter controller jako skript pro herní engine Unity. Kontroler by měl umožňovat pohyb po libolné sadě colliderů z 3D fyzikálního systému Unity, měl by umožnit skákání a narážení hlavou do stropu. Měl by spolehlivě detekovat stání na zemi (tzn. při chůzi zkopce nebude tvrdit, že se znáší). Hráč by neměl být schopen zatočit ve vzduchu."
- dva lidé nesmí mít to samé (kdo dřív přijde...)
- neměla by to být knihovna, ale program. Lze udělat knihovnu a pak ji použít v ukázkové aplikaci
- radši méně kódu, ale hezky strukturovaného a čitelného
    - tzn. není třeba databáze s dvaceti datovými typy. Stačí dva typy, ale mít pěknou strukturu kódu pro monžné rozšíření
- program by měl být rozumně odlazený (abych při vyzkoušení nenarazil na bugy, ale rozhodně bych neměl být jako uživatel schopný program shodit, když nedělám nic úchylného)
- dokumentace (https://ksvi.mff.cuni.cz/~kryl/dokumentace.htm)
    - uživatelská = vysvětlete někomu kdo není programátor, jak se váš program používá
        - Např.: Program čte vstup ze souboru `input.csv` a ten má takový a takový formát. Program má 3 argumenty na příkazové řádce a ty ovlivňují následující... V případě chyby program vygeneruje soubor `error.log`...
        - Např.: Kliknutím a tažením RMB můžete posouvat kameru po světě, kolečkem přibližujete. Dvojklik zobrazí detail komponenty...
        - Např.: Server běží v prostředí node.js, takže pro jeho spuštění budete muset mít nainstalovaný node. Spuštění z příkazové řádky provedete příkazem: ...
    - vývojová = vysvětlete mně (nebo vašemu spolužákovi) hlavní strukturu a koncepty vašeho programu, aby ho pochopil do takové míry, že bude schopný program rozšířit, případně bude vedět kde v kódu hledat, kdyby měl opravovat nějakou chybu (tady se vám bude rozhodně ušetří práci to, že budete mít přehledný kód)
        - Např.: Program dělá diskrétní simulaci světa, svět je mřížka buňěk, buňky jsou ty a ty. Program žije ve třídě `Program` a používá třídy `World`, `SimulationPolicy` a `EvolutionRecorder` jako hlavní komponenty celé aplikace. ...
- osobní předvedení programu (není povinné, ale doporučuji - nebudeme muset řešit všechno přes email)


## Co by se dalo dělat?

Od Martina Mareše: http://mj.ucw.cz/vyuka/zap/

Osobně doporučuji něco, o čem se budete učit později na MFF. Zabijete tím dvě mouchy jednou ranou a ušetříte si tak práci s učením v budoucnu. I když se jedná o něco, co teď neumíte - můžete se to naučit a proto já schválím, jestli je složitost programu adekvátní, nebo jste si naložili příliž.

Průvodce labyrintem algoritmů: http://pruvodce.ucw.cz/

- grafy
    - hledání nejkratší cesty: dijkstra, A*
    - hledání maximálního toku v tokové síti
    - hledání cyklů
    - hledání komponent souvislosti
- text
    - Aho-Corrasick
    - Knuth-Morris-Pratt
    - regulární výrazy
    - překladače, kompilátory, interpretery, pretty-printery, lintery, transpilery
    - zpracování přirozeného jazyka
        - překladač
        - určování pádu, sklnování slov
        - generování textu pohle šablony (překladové systémy pro softwarové vývojáře)
            - `"There were :bug_count: #bug(s) in your program."`
- geometrické problémy
    - triangulace polygonů
    - binární operace na tělesech
    - zpracování obrazu / volumetrických dat (minecraft?)
- kombinatorické hry (šachy, piškvorky, ...)
    - prohledávání stavového prostoru
    - prořezávání
    - heuristky
- automaty a gramatiky
    - konečné deterministické automaty vs. regulární výrazy vs. nedeterministické
    - simulace turingova stroje
    - compiler pro turingův stroj (assembler -> turing)
    - busy beaver
- hardwarové věci
    - simulace hradel
    - simulace jednoduchých starých procesorů nebo podmnožin procesorů (např. MIPS)
    - vlastní překladač pro nějaký jednoduchý jazyk
- databáze
    - zkusit si implementovat key-value store (jako Redis) s indexem přes klíče pomocí B-stromu nebo hashování
    - vlastní malá databáze, která si hlídá konzistenci cizích klíčů
    - in-memory databáze pro snadné testování aplikace
- matematika
    - symbolická úprava matematických výrazů (symbolická kalkulačka)
    - SAT
    - lineární optimalizace (simplexová metoda)
    - počítání s maticemi
    - numerická matematika
        - kořeny polynomů
        - integrace diferenciálních rovnic
        - dekompozice matic (LU rozklad)
        - fitování funkcí
- fyzika
    - simulace el. obvodů
    - simulace proudění kapalin, plynů
    - simulace sluneční soustavy (newtonovská gravitace)
    - rigid-body physics 2D, 3D
- grafika
    - konvoluční filtry
    - napsání vlastní 3D grafické pipeline nad CPU (vertex shader, fragment shader)
    - ray-tracing
    - automatický kontrast a jas obrázku
    - podepisování obrázků (detekce černé kopie souboru)
    - vyhledávání obrázků podle barev
    - tesselace povrchu podle displacement mapy
    - syntetické generování textur (perlin noise -> dřevo / mramor / ...)
- problémy v reálném světě (nejde řešit pěkně, je třeba použít neuristiky)
    - jízdní řády
    - obchodní cestující
    - batoh
    - loupežníci
    - optimální rozvržení školního rozvrhu
- cloud
    - vlastní message broker (rabbitMQ, Apache Kafka)
    - vlastní orchestrace kontejnerů pro docker
    - vlastní nástroj pro deployment (nahrávání přes FTP / SSH, ...)
    - nástroj pro prohlížení databáze (jako phpmyadmin, ale appka)
    - nástroj pro testování REST api, GraphQL api
    - služba pro ukládání souborů (object storage - amazon S3 apod.)

------

from [Jan Hamáček, prof. from MFF UK](https://www2.karlin.mff.cuni.cz/~hamacek/programovani.php), author Tomáš Hollan MFF UK

DIFF
   čte dva soubory, porovnává řádky (stejný/různý) a vytvoří HTML-soubor znázorňující rozdíly
   (původní řádky, přidané řádky, smazané řádky mají ruzne CSS-styly (externi CSS soubor)).
   Nemusí být jednoznačné, co je přidaný řádek, proto navrhněte vlastní způsob.

Word-DIFF
   čte dva soubory, porovnává slova (stejné/různé) a vytvoří HTML-soubor znázorňující rozdíly
   (původní slova, přidaná slova, umazaná slova mají ruzne CSS-styly (externi CSS soubor)).
   Nemusí být jednoznačné, co je přidané slovo, proto navrhněte vlastní způsob.

REPLACE
   Z konfiguračního souboru (parametr volání) načte CO má nahradit ČÍM
   a čte ze standardního vstupu, nahrazuje a vypisuje na standardní výstup.

Duplicitní soubory
   Prohledá zadanou cestu (adresář/složku nebo disk) včetně podadresářů
   a vypíše všechny skupiny souborů, které mají shodné
      - velikost
      - [x] datum a čas
      - [x] obsah
      - [x] jméno
   (porovnávání položek označených [x] bude volitelné).
   Je potřeba použít překladač, který umí pracovat s dlouhými jmény souborů
   a adresářů (FreePascal nebo Delphi).

DERIVACE
   výpis derivace funkce

Pretty-printer
   zdrojový text v Pascalu převede do HTML s tím, že
   - zvýrazní klíčová slova
   - rozdělí do řádek
   - odsadí vnořené příkazy

Fuj-printer
   vypíše zdrojový text v Pascalu s tím, že
   - odstraní komentáře
   - odstraní zbytečné mezery
   - identifikátory přejmenuje na x1, x2, x3...
   - program zarovná na zadanou šířku řádky
   - výsledný program bude ekvivalentní původnímu programu
     (půjde přeložit a bude dělat totéž)

Analýza kurzů akcií 1
   na vstupu má soubor - seznam denních kursů jedné akcie.
   Pro každou dvojici hodnot BUY a SELL lze spočítat zisk (nebo ztrátu), kterou by obchodník získal,
   kdyby při kursu BUY za všechny své peníze nakoupil a při kursu SELL všechny své akcie prodal.
   Program nalezne hodnoty BUY a SELL, které by vedly k maximálnímu zisku.

Analýza kurzů akcií 2
   na vstupu má soubor - seznam denních kursů jedné akcie.
   PRAVIDLA mají tvar:

      * pokud je kurs větší než K1-násobek kursu před D1 dny, kup.
      * pokud je kurs větší než K2-násobek kursu před D2 dny, prodej.
      * pokud je kurs menší než K3-násobek kursu před D3 dny, kup.
      * pokud je kurs menší než K4-násobek kursu před D4 dny, prodej.
      * pokud je kurs menší než K5-násobek kursu, za který jsi koupil, prodej.
      * pokud je kurs větší než K6-násobek kursu, za který jsi koupil, prodej.
      * pokud je kurs menší než K7-násobek kursu, za který jsi prodal, kup.
      * pokud je kurs větší než K8-násobek kursu, za který jsi prodal, kup.

   Pokyn "kup" znamená koupit akcie za všechny peníze.
   Pokyn "prodej" znamená prodat všechny akcie.
   Pro známé hodnoty K1..K8, D1..D4 je snadné spočítat výsledný zisk nebo ztrátu
   (předpokládejme, že v posledním dni datového souboru všechny akcie prodáme).
   Program bude hledat hodnoty K1..K8, D1..D4, při kterých by zisk byl největší.

Cross-Reference Pascalu
   načte zdrojový program v pascalu a vytiskne tabulku,
   který podprogram volá který podprogram. Označí nevolané podprogramy.

Cross-Reference PHP
   načte zdrojový program v PHP a vytiskne tabulku,
   který podprogram volá který podprogram. Označí nevolané podprogramy.

Uses v Pascalu
   načte zdrojové soubory programu v Pascalu a jeho unit a vytiskne tabulku,
   která část (program, unita) používá kterou unitu.

require v PHP
   načte zdrojové kódy v PHP a vytiskne tabulku,
   který soubor se (pomocí require,  require_once) odkazuje na který soubor.

Konstanty pro řetězce
   načte zdrojový program v pascalu a upraví ho tak, že všechny textové konstanty
   (třeba write('abc'); ) převede na vhodně pojmenované konstanty, jejichž deklarace
   přidá na začátek programu (třeba const  txABC = 'abc'; ...write( txABC );)

Sousední slova
   přečte (dlouhý) soubor s (českým) textem, zkoumá dvojice po sobě jdoucích slov
   a nakonec vytiskne tabulku dvojic spolu s počty výskytů, seřazenou od nejčastější.

Piškvorky
   Pro dva hráče, s umělou inteligencí.

Společná slova
   přečte (dlouhý) soubor s (českým) textem, zkoumá dvojice slov vyskytujících se ve stejné větě
   a nakonec vytiskne tabulku dvojic spolu s počty výskytů, seřazenou od nejčastější.

Šachové dvoutažky
   načte pozici šachové hry s údajem, kdo je na tahu a zjistí, zda může dát druhým tahem mat.

Mat K-V x K
   hraje koncovku krále a věže proti králi

Mat K-V x K naslepo
   hraje koncovku krále a věže proti králi, když neví, kde je soupeřův král
   (soupeř jenom hlásí nepřípustné tahy a šach nebo mat)
   TĚŽKÉ!

Logik
   hraje hru logik (master-mind) v pozici toho, kdo hádá.

Dáma
   hraje hru dáma.

Prší
   hraje karetní hru prší.

Krávy
   hraje hru "6 bere", hraje proti hráči i za předem daný počet počítačových protihráčů.

BANG!
   hraje hru BANG!, hraje proti hráči i za předem daný počet počítačových protihráčů.
   Je možné si zjednodušit pravidla a implementovat pouze jejich část.

Explodující atomy
   hráči střídavě pokládají své figurky do políček hracího plánu neobsahujících soupeřovy figurky.
   Figurku nelze položit do políčka, kde už leží figurka soupeře.
   Když je políčko NAPLNĚNO, tj. obsahuje tolik figurek, kolik má políčko sousedních políček
   (2, 3 nebo 4), exploduje a rozdělí své figurky mezi sousední políčka.
   Případné soupeřovy figurky, které tam již byly, přebarví na svou barvu,
   jeho vlastní figurky zůstávají a zjišťuje se, zda opět není políčko naplněno.
   Vyhraje hráč, který eliminuje soupeře.

Hra lodě

Překládání papíru
   program načte čísla M a N a spočte a vytiskne počet možností,
   jimiž lze čtverečkovaný papír rozměrů MxN poskládat na jednu kostičku.

Konkrétní kalkulačka
   Program se bude chovat přesně stejně jako (zvolená) kalkulačka,
   tj. po stejných stiscích kláves bude zobrazovat stejný obsah displeje.

Šablony
   Deklarace a funkce pro výstup pomocí šablon výstupu v souborech.
   Šablona je soubor s vyznačenými místy pro nahrazení, například

      Kvadratická rovnice [a]x^2+[b]x+[c]=0
      má řešení x1 = [x1] a x2 = [x2].

   Program spočte a nastaví hodnoty pro výstup do seznamu jméno=hodnota,
   například a=1 b=-5 c=6 x1=2 x2=3 a zavolá funkci pro výstup pomocí šablony,
   výsledkem bude výstup

      Kvadratická rovnice 1x^2+-5x+6=0
      má řešení x1 = 2 a x2 = 3.

   Zápočtový program bude obsahovat deklarace a podprogramy pro práci se seznamem hodnot
   a proceduru

       VytiskniVystupPomociSablony( SOuborSSablonou: string; Hodnoty: THodnoty )

   - spolu s jednoduchými příklady (výstup do textu nebo HTML česky, slovensky...).

DeBOM
   BOM (Byte Order Mark) je značka na začátku (některých) textových souborů udávající pořadí bajtů
   v kódování UTF.
   Problém je v tom, že textové editory ji nezobrazují a na druhou stranu,
   pokud zdrojové texty např. v PHP obsahují BOM, nebude fungovat správně třeba
   generování obrázků (protože obrázky před vlastními bajty obrázku budou mít bajty BOM).

   Program se bude spouštět ve dvou režimech, rozlišených podle parametrů spuštění:
      1) DeBOM <cesta> -f ........... najde a vypíše seznam souborů obsahujících BOM
                                      ve tvaru
                                               DeBOM <soubor i s cestou> -d
                                               DeBOM <soubor i s cestou> -d
                                               DeBOM <soubor i s cestou> -d
      2) DeBOM <soubor i s cestou> -d .. ze zadaného souboru odstraní BOM.

SUDOKU
   Program na řešení Sudoku.

Přečasování titulků
   Vstupem programu bude soubor titulků a dvakrát dva časové údaje:
      - čas, kdy zazněla určitá věta ve filmu
      - čas, pod kterým je uvedena v titulkách.
   Program spočte změnu rychlosti a posunutí a upraví soubor s titulky tak,
   aby ony dvě zadané věty zazněly zároveň se zobrazením odpovídajícího titulku.

XKCD na tabletech
   Komix xkcd (www.xkcd.com) zobrazuje dodatečný text k obrázku pomocí HTML-atributu "title",
   takže po najetí myší na obrázek. To je obtížné na tabletech a dalších dotykových zařízeních.

   Program zpracuje adresář (složku) s uloženými stránkami XKCD tak,
   že najde tento dodatečně zobrazovaný text a připíše ho do stránky mezi obrázek a následující tlačítka.

Beamer
   Beamer je makro do \TeX-u pro sázení presentací.
   Program načte jednoduchý odrážkový seznam,
      případně doplněný o písmenkové značky na začátku řádky
   a vyrobí z něj \TeX-ový zdrojový kód presentace v Beameru.

Hra Miny
