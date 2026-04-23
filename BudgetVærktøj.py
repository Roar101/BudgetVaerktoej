# Her laves der en input i forhold til indtægter, hvor den spørger brugeren af programmet "Denne måneds indtæger"
indtægter = float(input("Denne måneds indtægter: "))
#Her laves der en dictionary med de forskellige udgifter som er "transport, mad og fornøjelser"
udgifter = {
}


# Denne funktion tilføjer en kategori til udgifter hvis den ikke er i forvejen og tilføjer et tilsvarende beløb.
def tilføj_udgift(beløb,kategori):
    if not kategori in udgifter:
        udgifter[kategori] = 0
    udgifter[kategori] += beløb
    return udgifter

# Denne funktion returnerer summen af ens udgifter - indtægter.
def over_underskud(indtægter, udgifter):
    return indtægter-sum(udgifter.values())


# Denne funktion bestemmer den højeste udgift.
def størst_udgift(udgifter):
    højest = list(udgifter.keys())[0]
    for kategori in udgifter:
        if udgifter[kategori]>udgifter[højest]:
            højest = kategori
    return højest

# Her spørger programmet om kategorier og beløbet på kategorierne.
if __name__ == '__main__':
    menuvalg = None
    while menuvalg != 'stop':
        ny_kategori = input('Kategori? ')
        nyt_beløb = float(input('Beløbet på din kategori '))
        tilføj_udgift(nyt_beløb, ny_kategori)
        menuvalg = input('Er der flere kategori, hvis ikke skriv stop ')

    # Her bliver total defineret
    total=over_underskud(indtægter,udgifter)

    # Her bestemmer programmet om du er over eller underskud.
    if total <= 0:
        print("I denne måned er du " + str(total) + " i underskud")
    else:
        print("I denne måned har du " + str(total) + " i overskud")

    # Her bestemmer den hvad du har brugt flest penge på.
    print("Du har brugt flest penge på", størst_udgift(udgifter))

