
indtægter = int(input("Denne måneds indtægter: "))

udgifter = {
    "transport":0,
    "mad":0,
    "fornøjelser":0
}



def tilføj_udgift(beløb,kategori):
    if not kategori in udgifter:
        udgifter[kategori] = 0
    udgifter[kategori] += beløb
    return udgifter

def over_underskud(indtægter, udgifter):

    return indtægter-sum(udgifter.values())



def størst_udgift(udgifter):
    højest = list(udgifter.keys())[0]
    for kategori in udgifter:
        if udgifter[kategori]>udgifter[højest]:
            højest = kategori
    return højest

if __name__ == '__main__':
    menuvalg = None
    while menuvalg != 'stop':
        nyt_beløb = int(input('beløb?'))
        ny_kategori = input('kat?')
        tilføj_udgift(nyt_beløb, ny_kategori)
        menuvalg = input('vælg')

    total=over_underskud(indtægter,udgifter)

    if total <= 0:
        print("I denne måned er du " + str(total) + " i underskud")
    else:
        print("I denne måned har du " + str(total) + " i overskud")

    print("Du har brugt flest penge på", størst_udgift(udgifter))

