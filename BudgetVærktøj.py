
indtægter = int(input("Denne måneds indtægter: "))

udgifter = {
    "transport":400,
    "mad":600,
    "fornøjelser":100
}

def over_underskud(indtægter, udgifter):

    total = indtægter

    if total <= 0:
        print("I denne måned er du " + str(total) + " i underskud")
    else:
        print("I denne måned har du " + str(total) + " i overskud")
    return

def størst_udgift(udgifter):
    højest = udgifter[0]
    for kategori in udgifter:
        if udgifter[kategori]>udgifter[højest]:
            højest = kategori
        print("Du har brugt flest penge på " + højest)


print(over_underskud(indtægter, udgifter), størst_udgift(udgifter))

