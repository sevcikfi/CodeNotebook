# Hradlove sítě

Vytvořte program, který ze vstupního souboru načte hradlovou síť a provede
její vyhodnocení. Hradlová síť se skládá ze logických hradel, jejichž vstupy a
výstupy mohou být propojeny. Hradlová síť i každé hradlo může mít libovolný
počet vstupů a výstupů (podrobněji viz níže). Hradla obsažená v hradlové síti
mohou mít:

* vstupy připojené na výstup jiného hradla nebo na vstup hradlové sítě,
* výstupy připojené na vstup jiného hradla nebo na výstup hradlové sítě.

Na vstupech/výstupech hradla/hradlové sítě se může objevit jedna z
následujících tří hodnot (tj. hradla počítají v třístavové logice):

* `'0'` (logická nula)
* `'1'` (logická jedna)
* `'?'` (nedefinovaná hodnota)

Celá hradlová síť pracuje v taktech — před prvním taktem jsou definovány pouze
hodnoty na vstupech hradlové sítě (kromě výjimek popsaných dále). Pokud v
nějakém taktu dojde ke změně nějakého ze vstupů hradla, tak se případná nová
hodnota na jeho výstupech (vyplývající ze změny vstupu) objeví až v
následujícím taktu, tj. doba výpočtu každého hradla je právě 1 takt.

Výsledkem hradlové sítě jsou hodnoty na jejích výstupech po jejím ustálení,
tj. když je na výstupu každého hradla v ní hodnota odpovídající (dle
přechodové funkce) hodnotám na jeho vstupech a hodnoty na těchto vstupech se
od předchozího taktu nezměnily. Počet taktů, po kterých dojde k ustálení sítě,
je dobou výpočtu hradlové sítě. Pokud jsou mezi hradly v hradlové síti cykly,
tak může dojít k zacyklení hradlové sítě, tj. nikdy nedojde k jejímu ustálení.
Pro detekci zacyklení hradlové sítě bude program používat časové omezení —
pokud se hradlová síť neustálí po 1000000 (jeden milion) taktů, tak jsou za
výsledek hradlové sítě považovány hodnoty na jejich výstupech po provedení
1000000 (jednoho milionu) taktů. Hradlová síť se může ustálit i ve stavu, kdy
na nějakém jejím výstupu je nedefinovaná hodnota (?).

Vstupní soubor hradlové sítě obsahuje 2 druhy bloků: definice **typů hradel**
pomocí jejich přechodových funkcí a definici vlastní **hradlové sítě**.

V každém vstupním souboru musí být definováno alespoň jeden typ hradla a právě
jedna hradlová síť. Ve vstupním souboru mohou být definovány i typy hradel,
které nejsou použity v hradlové síti.

Jednotlivá hradla, jejich součásti (vstupy a výstupy) i jejich instance v
hradlové síti a ostatní součásti hradlové sítě jsou pojmenovány. Jméno
takového prvku je libovolná posloupnost znaků, která nesmí:

* obsahovat bílé znaky (mezera, tabulátor, new line, line feed, atd.)
* obsahovat znak tečka `'.'`
* obsahovat znak středník `';'`
* obsahovat posloupnost znaků pomlčka a větší než `'->'`
* začínat slovem `'end'`

Jména prvků i klíčová slova vstupního souboru jsou case sensitive, tj. `'AND'`
a `'and'` jsou dva rozdílné identifikátory. Jednotlivé bloky nebo řádky v
blocích mohou být ve vstupním souboru odděleny libovolným počtem:

* prázdných řádků
* řádků obsahujících pouze bílé znaky (mezera, tabulátor)
* řádků začínajících znakem středník (`';'`) — lze použít jako komentář

Každý řádek odpovídající jednomu z předchozích tří bodů se zcela ignoruje.
Pokud se řádek nějakého bloku skládá z více složek, tak jsou tyto složky
odděleny právě jednou mezerou.

## Blok definice hradel

    gate _jméno_hradla_
    inputs x1 x2 ... xN
    outputs y1 y2 ... yM
    _definice_přechodové_fce_
    end

Definuje hradlo (nový typ hradla) s `N` vstupy a `M` výstupy. Hradlo může mít
0 vstupů (`N ≥ 0`) (i takový blok obsahuje řádek inputs, ale slovo inputs je
hned následováno koncem řádku), ale musí mít alespoň jeden výstup (`M ≥ 1`).

Za klíčovým slovem `inputs` následuje seznam jmen všech vstupů. Za klíčovým
slovem `outputs` následuje seznam jmen všech výstupů. Jména vstupů a výstupů
jsou jedinečná v rámci definice daného hradla. Ostatní hradla definovaná ve
vstupním souboru ale mohou mít své vstupy/výstupy pojmenované stejně jako
jakékoliv jiné hradlo, či hradlová síť.

Každý řádek přechodové funkce definuje hodnotu všech výstupů hradla v
závislosti na jedné kombinaci všech vstupů hradla. Na řádku jsou nejprve
hodnoty všech vstupů (v pořadí definovaném na řádku inputs) následované
hodnotami všech výstupů (v pořadí podle outputs). Pokud pro nějakou kombinaci
vstupů není přechodová funkce explicitně definována, tak se použije
následující implicitní definice:

* pro kombinaci vstupů, kde ani jeden nenabývá hodnoty `'?'`, je hodnota všech výstupů definována jako `'0'`
* pro kombinaci vstupů, kde alespoň jeden nabývá hodnoty `'?'`, je hodnota všech výstupů definována jako `'?'`

Explicitní definice přechodové funkce může být prázdná, tj. za řádkem outputs
následuje řádek end — potom se na hradlo aplikuje pouze implicitní chování
přechodové funkce.

V počátečním stavu, tj. před prvním taktem sítě mají všechny výstupy všech
hradel následující hodnoty:

* pokud `N = 0` (hradlo s 0 vstupy), hodnoty definované přechodovou funkcí
* pokud `N ≥ 1`, nedefinovanou hodnotu `'?'`

Příklad: Hradlo pojmenované `'and'`, se dvěma vstupy `'i1'` a `'i2'` a jedním
výstupem `'o'` a přechodovou funkcí definovanou podle logického součinu:

    gate and
    inputs i1 i2
    outputs 0
    1 1 1
    0 1 0
    1 0 0
    0 0 0
    end

nebo také zkráceně (s použitím implicitních pravidel)

    gate and
    inputs i1 i2
    outputs 0
    1 1 1
    end

## Blok definice vlastní hradlové sítě

    network
    inputs x1 x2 … xN
    outputs y1 y2 … yM
    gate _jméno_instance_hradla jméno_typu_hradla_
    ...
    gate _jméno_instance_hradla jméno_typu_hradla_
    _definice_propojení_mezi_vnitřními_hradly_
    end

Definuje hradlovou síť s `N` vstupy a `M` výstupy. Hradlová síť musí mít
alespoň jeden vstup (`N ≥ 1`) a alespoň jeden výstup (`M ≥ 1`). Řádky
začínající klíčovým slovem `'gate'` obsahují definici instancí hradel
obsažených v hradlové síti. Jméno instance nějakého vnořeného hradla může být
stejné jako vlastní jméno tohoto hradla (jeho typu). Každá hradlová síť musí
obsahovat alespoň jedno vnořené hradlo.

Za klíčovým slovem `inputs` následuje seznam jmen všech vstupů. Za klíčovým
slovem `outputs` následuje seznam jmen všech výstupů. Jména vstupů a výstupů
jsou jedinečná v rámci definice samotné hradlové sítě. Vnořená hradla ale
mohou mít své vstupy/výstupy pojmenované stejně jako hradlová síť.

Každý řádek v definici propojení definuje jedno spojení mezi dvěma místy v
hradlové síti. Definice propojení má jednu z následujících forem:

* `ga.ix->gb.oy` definuje propojení vstupu `ix` na instanci `ga` vnořeného hradla na výstup `oy` na instanci `gb` vnořeného hradla
* `ga.ix->iy` definuje propojení vstupu `ix` na instanci `ga` vnořeného hradla na vstup `iy` hradlové sítě
* `ox->ga.oy` definuje propojení výstupu `ox` hradlové sítě na výstup `oy` na instanci `ga` vnořeného hradla

Jeden vstup hradlové sítě může být připojen na vstup více vnořených hradel.
Každý vstup hradlové sítě musí být připojený na alespoň jedno vnořené hradlo.
Na každý výstup hradlové sítě musí být připojený právě jeden výstup nějakého
vnořeného hradla. Pokud vstup nějakého z vnořených hradel zůstane nezapojený,
tak je na něm konstantní nedefinovaná hodnota (`'?'`).

Každá hradlová síť má ke svým explicitně definovaným vstupům ještě dva
implicitně definované vstupy pojmenované `'0'` a `'1'`. Na těchto vstupech
jsou vždy konstantní hodnoty 0, resp. 1. Hodnoty těchto vstupů uživatel nijak
nezadává. Pravidla pro připojení vstupů vnořených hradel na vstupy 0 a 1 jsou
stejná jako pro ostatní vstupy hradlové sítě.

## Použití programu

Program se spouští vždy s právě jedním parametrem na příkazové řádce — ten
definuje jméno souboru s definicí hradlové sítě (viz předchozí částí zadání).
Pokud se povede v pořádku načíst celý obsah definičního souboru, tak program
čeká na standardním vstupu na příkazy uživatele. Každý příkaz je na zvláštním
řádku — je to seznam jedniček, nul a otazníků (oddělených jednou mezerou),
které definují hodnoty na vstupech hradlové sítě (v pořadí v jakém jsou vstupy
uvedeny v bloku definice hradlové sítě). Odpovědí na každý příkaz uživatele je
jeden řádek na standardním výstupu programu — doba výpočtu hradlové sítě (v
taktech), jedna mezera a výsledné hodnoty všech výstupů hradlové sítě (opět v
pořadí definice výstupů ve vstupním souboru). Příkazem `'end'` nebo ukončením
standardního vstupu se program ukončí.

Před provedením prvního příkazu je hradlová síť v počátečním stavu, při
provádění dalších příkazů začíná výpočet hradlové sítě ve stavu po posledním
příkazu (tj. na výstupech základních hradel již nejsou nedefinované hodnoty,
ale hodnoty po ustálení hradlové sítě na předchozím vstupu).

Např. pro vstupní soubor `**hradlova_sit.txt**`:

    gate and
    inputs i0 i1
    outputs o
    1 1 1
    end
    
    gate or
    inputs i0 i1
    outputs o
    1 0 1
    0 1 1
    1 1 1
    end
    
    gate not
    inputs i
    outputs o
    0 1
    end
    
    network
    inputs a b
    outputs a&b a|b
    gate a1 and
    gate o1 or
    a1.i0->a
    a1.i1->b
    o1.i0->a
    o1.i1->b
    a&b->a1.o
    a|b->o1.o
    end

a spuštění programu `program.exe hradlova_sit.txt` lze na standardní vstup
zapsat následující příkazy (řádky začínající "$&gt;" jsou vstupní, ostatní
jsou výstupní):

    $> 1 0
    1 0 1
    $> 1 1
    1 1 1
    $> end

Program by měl ošetřovat všechny možné chybné vstupy a za žádných okolností by
neměl spadnout. Pokud program nedostal právě jeden argument na příkazové
řádce, tak program na samostatný řádek standardního výstupu vypíše '`Argument
error.`' a skončí. Pokud vstupní soubor nejde z jakéhokoli důvodu otevřít nebo
z něj nelze číst, apod., tak program vypíše '`File error.`' a skončí. Pokud je
příkaz na standardním vstupu ve špatném formátu, tak program vypíše '`Syntax
error.`' a čeká na další příkaz.

Pokud je chyba ve vstupním souboru hradlové sítě, tak program na standardní
výstup vypíše jeden z následujících řádků a skončí (nebude přijímat žádné
příkazy od uživatele) — `N` označuje číslo řádky ve vstupním souboru na které
došlo k chybě, řádky jsou číslované od 1:

* '`Line N: Duplicate.`'  
Při opakování některé kombinace vstupů v definici přechodové funkce u hradla,
definice již definovaného typu hradla nebo instance, jména vstupu nebo výstupu
nebo definice propojení u hradlové sítě.

* '`Line N: Missing keyword.`'  
Pokud v programu chybí nějaká povinná část, např. `'inputs'` nebo `'outputs'`.

* '`Line N: Binding rule.`'  
Pokud je chyba v logice propojovacího pravidla, např. propojení vstupu jednoho
hradla na vstup jiného, apod. Vznikne též na příkaze `'end'`, pokud nebyla
dodržena pravidla pro tvorbu hradlové sítě(např. nepřipojený výstup).

* '`Line N: Syntax error.`'  
Při jiné chybě (např. neplatné jméno typu hradla v definici hradlové sítě,
odkaz na neexistující vstup nebo výstup v propojovacím pravidle, apod.).

Očekává se, že oznámíte pouze první chybu (tj. chybu s nejmenším číslem
řádku), na kterou narazíte.

Vzorové příklady k otestování vašeho řešení naleznete [zde](https://recodex.mff.cuni.cz:4000/v1/uploaded-files/ab456765-aba6-11e7-a937-00505601122b/download).

## FAQ

Tato část obsahuje často kladené dotazy a odpovědi na ně.

_Q: V zadání se píše, že vstupní soubor obsahuje 2 druhy bloků (definice
základních hradel a vlastní hradlové sítě). Je součástí zadání, že bloky jsou
vždy právě v tomto pořadí?_  
A: Ano, můžete počítat s tím, že ve vstupním souboru jsou nejprve definována
všechna hradla a pak hradlová síť.

_Q: Nepřipadá mi logická ta definice přesměrování `'ox->ga.oy'` definuje
propojení výstupu `'ox'` hradlové sítě na výstup `'oy'` na instanci `'ga'`
vnořeného hradla. Fakticky to přeci znamená, že výstup `'ga.oy'` jde na výstup
`'ox'`._  
A: Ano, šipky v definicích propojení vstupů/výstupů vedou opačným směrem než
proudí data (a jak je to i zachyceno v animaci vyhodnocení příkladu ze zadání

* viz úloha Hradlové sítě II). Tento směr šipek byl použit, protože levá
strana pravidla je to, co definuje vztah spojení (ta strana pro kterou je
„důležité“, že takové spojení existuje). Např. pro hradlo `'ga'` není
důležité, zda nebo jak je zpracováván jeho výstup `'oy'`, ale pro hradlovou
síť je důležité, zda nebo kam je připojen výstup `'ox'`.

_Q: Platí, že pro libovolné hradlo musí být všechny jeho výstupy zapojeny na
vstup jiného vnořeného hradla nebo na výstup hradlové sítě?_  
A: Odpověď na tuto otázku sice není explicitně v zadání uvedena, ale
předpokládá se, že výstupy hradel mohou zůstat nezapojené. Hlavní motivace je,
že se může hodit u nějakého hradla využít pouze některé jeho výstupy. Toto
samozřejmě nedává smysl pro hradla s jedním výstupem, resp. pokud není
zapojený žádný výstup nějakého hradla, nicméně takovéto situace se v rámci
jednoduchosti nijak speciálně neošetřují.
