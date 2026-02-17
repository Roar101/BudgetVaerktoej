
indtægter = int(input("Denne måneds indtægter: "))
udgifter = int(input("Denne måneds udgifter: "))

def over_underskud(indtægter,udgifter):
    total = indtægter - udgifter
    if total <= 0:
        print("I denne måned er du " + str(total) + " i underskud")
    else:
        print("I denne måned har du " + str(total) + " i overskud")
    return

print(over_underskud(indtægter,udgifter))
