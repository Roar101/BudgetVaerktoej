
indtægter = int(input("Denne måneds indtægter: "))

udgifter = {
    "transport":400,
    "mad":600,
    "fornøjelser":100
}

def over_underskud(indtægter, udgifter):

    return indtægter-sum(udgifter.values())



def størst_udgift(udgifter):
    højest = list(udgifter.keys())[0]
    for kategori in udgifter:
        if udgifter[kategori]>udgifter[højest]:
            højest = kategori
    return højest

if __name__ == '__main__':
    total=over_underskud(indtægter,udgifter)

    if total <= 0:
        print("I denne måned er du " + str(total) + " i underskud")
    else:
        print("I denne måned har du " + str(total) + " i overskud")

print(over_underskud(indtægter, udgifter))
print("Du har brugt flest penge på",størst_udgift(udgifter))
