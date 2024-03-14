# get_contestants will be first method called
# this method will take userInput, and adds thems to an array to be returned by the method
# a conditional to make sure all inputs will be numerical
def get_contestants():
    contestants =[]
    while True:
        contestant = input("Enter Contestant #" + (str(len(contestants) + 1)) + " (Enter 'q' to stop): ")
        if contestant.lower() == 'q':
            break
        if contestant.isdigit():
            contestants.append(int(contestant))
        else:
            print("Invalid input! Please enter an integer.")
    return contestants

# This method will just compare 2 number with each other
# I Only decided to make this, if 'max' class isn't allowed
def compare_numbers(contestant_1,contestant_2):
    if contestant_1 > contestant_2:
        return contestant_1
    elif contestant_1 == contestant_2:
        return contestant_1
    else:
        return contestant_2
    
    
# Fuck this is uggeee but im not sure how to tackle it without search
# This method takes an array of numbers, a number (which is the match)
# while loop > 1 
    # Were doing  1st to last in this case we can imagine
     #[1,2,3 vs -3 -2 -1]
        # 1vs-1 etc etc
    #I'm not sure what qualifies as a seach method so I just did a first then pop
def single_elimination(contestants,match):
    winner = []
    rounds = 0
    match += 1
    # All winners from this elimination will be put in the winners array
    # to be return for the next match
    while len(contestants) > 1:
        rounds += 1
        print("Duel : " + str(rounds) + "| Contestant 1: " + str(contestants[0]) + " VS "
              + "Contestant 2 : " + str(contestants[-1]))
        # Since first to last rule, i just did [0] and [-1]
        if contestants[0] > contestants[-1]:
            winner.append(contestants[0])
        else:
            winner.append(contestants[-1])
        print("Duel: " + str(rounds) + "| Winner " + str(winner[-1]))
        contestants.remove(contestants[0])
        contestants.remove(contestants[-1])

    if len(contestants) == 1 :  # If there's a remaining contestant
        print("No Challenger for " + str(contestants[0]) + ". Default Winner is: " + str(contestants[0]))
        winner.append(contestants[0])

    return winner, rounds, match

def main():
    match = 0
    winners = []
    contestants = get_contestants()
    if len(contestants) != 0:      
        print("///////Here Comes a New DareDevil: " + str(match) + "///////" )
        winners, rounds, match = single_elimination(contestants,match)
        while len(winners) > 1:
            print("///////Here Comes a New DareDevil: " + str(match) + "///////" )
            winners, rounds,match = single_elimination(winners,match)
        print("The winner is: " + str(winners[0]))
    else:
        print("Bruh where are the contestants?")
if __name__ == "__main__":
    main()




