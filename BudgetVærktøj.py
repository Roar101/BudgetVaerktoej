
indtægter = int(input("Denne måneds indtægter: "))
mad = int(input("Denne måneds udgifter for mad: "))
transport = int(input("Denne måneds udgifter for transport: "))
fornøjelser = int(input("Denne måneds udgifter for fornøjelser: "))

def over_underskud(indtægter, mad, transport, fornøjelser):
    total = indtægter - mad - transport - fornøjelser
    if total <= 0:
        print("I denne måned er du " + str(total) + " i underskud")
    else:
        print("I denne måned har du " + str(total) + " i overskud")
    return

def størst_udgift(mad,transport,fornøjelser):
    if mad>transport:
        print("Du har brugt flest penge på mad")


print(over_underskud(indtægter,mad, transport, fornøjelser))

