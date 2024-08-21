# Dice sum probability calculator
# Författare: eric
# Datum:
from collections import Counter

def most_frequent(List):
    occurence_count = Counter(List)
    print( occurence_count.most_common(1)[0][0])

def main():
    user_input = input("Skriv två nummer för tärningarna: ").split(" ")
    diceone=int(user_input[0])
    dicetwo=int(user_input[1])
    dicesum=[]
    for i in range(1,diceone+1):
        for x in range(1,dicetwo+1):
            throw=x+i
            dicesum.append(throw)
    most_frequent(dicesum)

    
if __name__ == "__main__":
    main()