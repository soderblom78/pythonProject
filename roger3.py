import roger2


# information styckningsdetaljer
def oxfile():
    print("\n\nSvensk Oxfilé:"
              "\nTrots att filén inte alltid kommer från oxen kallas den ändå för oxfilé."
              "\nDet rätta namnet är egentligen nötfilé men oxfilé har blivit det vedertagna namnet."
              "\nSom det blir ibland med namn. Filén är den enda muskel som sitter på insidan av skelettet,"
              "\noch det är därför den är så mör. Efterfrågan på filé är stort och i Sverige importerar vi "
              "\nmycket av denna detalj. Namnet filé kommer (inte helt otippat...) från franskan och "
              "\nbetyder fin tråd.")
    print("\nPris/kg:", roger2.nöt_detaljpris[0], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


def fransyska():
    print("\n\nSvensk nötstek av Fransyska:"
              "\nFransyskan (eller plomman) är en stor, rund detalj och sitter på lårets framsida. Fransyskan "
              "\nbestår ursprungligen av fyra olika muskler där en av musklerna vanligtvis tas bort innan den "
              "\nsäljs. Fransyskan kallades förr ländstek, det nya namnet kommer förmodligen från ett recept "
              "\nsom pulicerades i början av 1900-talet: Fransysk stek.")
    print("\nPris/kg:", roger2.nöt_detaljpris[1], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")



def lövbiff():
    print("\n\nSvensk Lövbiff av Nötinnanlår:"
          "\nLövbiff är tunna skivor av vårt uppskattade innanlår. Innanlårets fibrer är korta och går parallellt "
          "\ni muskeln vilket gör att den lämpar sig för snabb tillagning. Stek hastigt eller låt bräsera länge i "
          "\nrött vin. ")
    print("\nPris/kg:", roger2.nöt_detaljpris[2], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


def biff():
    print("\n\nSvensk Ryggbiff:"
          "\nRyggbiffen består av den långa ryggmuskeln som sitter mellan entrecôten och rostbiffen. Främre delen "
          "\nkallas enkelbiff eller clubstek. Urbenad biffstock kallas ryggbiff eller utskuren biff. Biten längst bak "
          "\npå ryggbiffen kallas för skomakarbiff och trots att den innehåller en relativt kraftig sena håller köttet "
          "\nsamma kvalitet som ryggbiffen. När du skär ryggbiff är det viktigt att snedställa kniven så att man skär "
          "\ntvärs över muskelfibrerna."
          "\nTips! Skär gärna ett jack i den grova senan så drar inte biffen ihop sig vid tillagning. Kort biffstock, "
          "\nutan rostbiff, är samma detalj som kotlett med ben på gris. Bakre delen på biffstocken kallas dubbelbiff "
          "\neller T-bensstek och innehåller också filén.")
    print("\nPris/kg:", roger2.nöt_detaljpris[3], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


def kalvkotlett():
    print("\n\nSvensk Kalvkotlett med ben:"
          "\nKotlett från kalv är mört kött som har en mild smak. Kotlettraden kan köpas hel, med eller utan ben."
          "\nKotlettraden kan skivas till kotletter. Kalvkotletten är utskuren i ett stycke med ben, utan filé, motsvarande "
          "\nclubstek från nöt. Beräkna ca 200 g per person med ben eller 100-125 g per person utan. Av kalvkotlett med ben "
          "\nberäknar du ca 175 g per person.")
    print("\nPris/kg:", roger2.kalv_detaljpris[0], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


def kalvstek():
    print("\nSvensk Kalvstek:"
          "\n\nKlassisk kalvstek kommer oftast från fransyskan. Den steks i ugn och serveras med klassiska tillbehör som "
          "\ngräddsås, kokta grönsaker och pressgurka eller gelé. Den kan även tärnas för att tillagas till finare grytor med "
          "\nandra smakrika ingredienser. Grytbitar används till finare grytor tillsammans med smakrika ingredienser.")
    print("\nPris/kg:", roger2.kalv_detaljpris[1], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


def kalvschnitzel():
    print("\n\nSvensk Kalvschnitzel av Kalvinnanlår:"
          "\nKalvinnanlår (fr. sous noix de veau) är de två musklerna på lårets insida. Innanlåret är mört, smakfullt och "
          "\npassar till stekning eller grytbitar. Köttet är magert, cirka 3% fett. Innanlåret passar att skäras i skivor och "
          "\nstekas i panna som schnitzel, eller bräseras som rulad i panna eller ugn. En wienerschnitzel är alltid gjord av "
          "\ntunt skivat kalvinnanlår, ibland missbrukas namnet. Görs schnitzeln på fläsk skall den kallas fläskschnitzel. "
          "\nInnanlåret skuret i bitar kan också användas kokt eller bräserat vilket kan kännas lite lyxigt och onödigt dyrt.")
    print("\nPris/kg:", roger2.kalv_detaljpris[2], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


def kalvfilé():
    print("\n\nSvensk Kalvfilé:"
          "\nKalvfilén skärs ut från kotlettraden ända upp till låret. Filén är den enda muskel som sitter på insidan av "
          "\nskelettet. Det gör att denna muskel arbetar lite och det är förklaringen till köttets mörhet. Kalvfilé kan med "
          "\nfördel stekas hel. "
          "\n\nMed sin milda smak passar den bra med enkel kryddning som salt och malen vitpeppar. Kalvfilé "
          "\nkan även tillagas i bitar eller skivor. Köttet kan skäras i medaljonger, noisetter eller bankas ut till exklusiv "
          "\npiccata. Schnitzel cordon bleu ska lagas av kalvfilé enligt originalreceptet. En annan god smaksättning är vitt vin "
          "\noch citron. Kalvfilé passar även att marinera. Om du vill grilla kalvfilé ska du vara ytterst försiktig. Köttet har "
          "\ninte mycket fett och kan därför lätt bli torrt. Skivor av kalvfilé kan svepas i bacon eller späck innan de grillas, "
          "\nför att undvika att köttet blir torrt.")
    print("\nPris/kg:", roger2.kalv_detaljpris[3], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


def lammkotlett():
    print("\n\nSvensk Lammkotlett med ben:"
          "\nLammkotletter som stekts just så att de har fin stekyta och ett rosa saftigt inre, är en ljuvlig upplevelse. Benen "
          "\noch fettet som kapslar in det möra köttet gör det smakrikt och saftigt.")
    print("\nPris/kg:", roger2.lamm_detaljpris[0], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


def lammstek():
    print("\n\nSvensk Lammstek utan ben:"
          "\nLammstek är förstklassig, omtyckt och lättlagad styckdetalj som kan serveras varm eller kall, med ben eller urbenad, "
          "\nmed fina såser eller till sallader eller klyftpotatis. Det är en av påskens höjdpunkter i många hem, här och i andra "
          "\nländer. Den blir ofta saftig eftersom köttet är tämligen finmarmorerat. "
          "\n\nSteken är lammets bakdel. Vanligen är benet urtaget när du köper en stek i butik. Steken består av flera olika muskler: "
          "\ninnanlår, ytterlår, fransyska, rostbiff och rulle. De olika delarna passar exempelvis som ministekar, särskilt innanlår, "
          "\nrostbiff och fransyska.")
    print("\nPris/kg:", roger2.lamm_detaljpris[1], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


def lammlägg():
    print("\n\nSvensk Lammlägg:"
          "\nLammlägg är lammets framben eller bakben. Läggens kött innehåller stora mängder bindvävnad och fett som ger mycket smak."
          "\nKöttet används mest som grytbitar men kan också kokas, bräseras eller brynas och lagas klart på låga temperaturer tills köttet är "
          "\nsaftigt och supermört och lossnar från benen. Rimmad lammlägg kan användas till rotmos eller ärtsoppa.")
    print("\n\nPris/kg:", roger2.lamm_detaljpris[2], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


def lammfile():
    print("\n\nSvensk Lamminnerfilé:"
          "\n\nLammfilé är bland det möraste kött man kan sätta tänderna i, ändå har den en ganska imponerande smak. Den smörsteks nästan jämt, "
          "\nhel eller som små noisetter. Den kan gå klart i pannan eller i ugn till en innertemperatur mellan 55 och 65 grader. "
          "\n\nEn filé väger ca 100 gram. Beräkna cirka 125 g kött per portion.")
    print("\nPris/kg:", roger2.lamm_detaljpris[3], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


def fläskkotlett():
    print("\n\nSvensk Fläskkotlett med ben:"
          "\nEn rejäl smörstekt fläskkotlett kan vara så läcker. Köttet är härligt motståndskraftigt utan att vara segt, och smaken är "
          "\nfantastisk, inte direkt fyllig men ändå generös. En fläskkotlett ska vara välsaltad, kanske kryddad med peppar, och får gärna "
          "\nserveras med något fruktigt, äppelmos, stekta äpplen eller lingon.")
    print("\nPris/kg:", roger2.gris_detaljpris[0], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


def fläskkarre():
    print("\n\nSvensk Fläskkarré med ben:"
          "\nKarrén är något för dem som gillar tufft och tåligt kött med mycket smak och saftighet. Riktiga barbeque-fantaster väljer ofta "
          "\nfläskkarré för sina långgrillningar under lock. Och med sin höga fetthalt, cirka 11% tål den just sådana långa och långsamma "
          "\ntillagningar, på grillen eller i ugnen.")
    print("\nPris/kg:", roger2.gris_detaljpris[1], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


def skinkstek():
    print("\n\nSvensk Skinkstek:"
          "\nSkinka är en av världens mest berömda och mest använda ingredienser. Och det beror nog till stor del på att den är användbar "
          "\ntill mycket och god i så många former. Som i sin tur kan brukas till allt från saltade, torkade, rökta och kokta charkskinkor, "
          "\njulskinka, flintastek och mycket mer.")
    print("\nPris/kg:", roger2.gris_detaljpris[2], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


def revbensspjäll():
    print("\n\nSvensk Revbensspjäll, tjocka:"
          "\nDet är en särskild upplevelse att äta det smakrika och täta fläskköttet som sitter på revbenen. Det kan vara behagligt segt eller "
          "\nlöst och eftergivet, men det smakar alltid mycket.")
    print("\nPris/kg:", roger2.gris_detaljpris[3], "kr.")
    print("\nVälj detalj genom att trycka på HÖGER PIL, eller PILTANGENT UPP för att komma tillbaka till menyn")


