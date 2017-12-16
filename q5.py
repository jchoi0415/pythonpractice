'''
Author: Jack Choi
Date: 10/12/17

WELCOME TO THE LAST AND HARDEST? CHALLENGE OF ALL! IF YOU ARE READY, PLEASE CARRY ON...

You wish to buy video games from the famous online video game store Mist.
Usually, all games are sold at the same price, 'p' dollars.
However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price.
Specifically, the first game you buy during the sale will be sold at 'p' dollars,
but every subsequent game you buy will be sold at exactly 'd' dollars less than the cost of the previous one you bought.
This will continue until the cost becomes less than or equal to 'm' dollars,
after which every game you buy will cost 'm' dollars each.
You have 's' dollars in your Mist wallet. How many games can you buy during the Halloween Sale?

EXAMPLE: p = 20, d = 3, m = 6, s = 80
ANSWER: 6
EXPLANATION: Starting at $20 dollars, you will go down by $3 every game you consecutively buy until you reach $6
20, 17, 14, 11, 8, 6, 6, 6, etc... But you can only spend $80...
20 + 17 + 14 + 11 + 8 + 6 = $76 = 6 games
(buying another one would make the total balance $82, hence cannot buy the 7th game)

P.S. I put some corner cases in there so make sure your code can handle those cases as well...

This function requires the number of games you could buy. Check answers for an idea of the answer format
REMEMBER GOOGLE IS YOUR BEST FRIEND AND MAKE USE OF PRINT DEBUGGING FOR ALL CODING PURPOSES
'''


# You only have to modify the function below. Do not modify main function or anything below it
def howmanygames(p, d, m, s):
    # Write code from below here! I initialised the variable you can use to return (but feel free to change it however)
    numofgames = 0
    if p < m:
        return numofgames
    while s >= p:
        while p > m:
            numofgames += 1
            s -= p
            p -= d
        s -= m
        numofgames += 1
    print(numofgames)
    return numofgames


def main():
    answerCounter = 0
    numofCase = 4

    output1 = howmanygames(20, 3, 6, 80)
    answer1 = 6

    output2 = howmanygames(150, 7, 22, 5000)
    answer2 = 171

    output3 = howmanygames(20, 3, 21, 80)
    answer3 = 0

    output4 = howmanygames(20, 3, 6, 0)
    answer4 = 0

    if output1 == answer1:
        print('Congratz! 1st case 맞았거든')
        answerCounter += 1
    else:
        print('빼애애애액! 1st case 틀렸거든... 고쳐봐 ㅋㅋ')

    if output2 == answer2:
        print('Congratz! 2nd case 맞았거든')
        answerCounter += 1
    else:
        print('빼애애애액! 2nd case 틀렸거든... 고쳐봐 ㅋㅋ')

    if output3 == answer3:
        print('Congratz! 3rd case 맞았거든')
        answerCounter += 1
    else:
        print('빼애애애액! 3rd case 틀렸거든... 고쳐봐 ㅋㅋ')

    if output4 == answer4:
        print('Congratz! 4th case 맞았거든')
        answerCounter += 1
    else:
        print('빼애애애액! 4th case 틀렸거든... 고쳐봐 ㅋㅋ')

    print('You got ' + str(answerCounter) + ' out of ' + str(numofCase) + ' questions correct')


if __name__ == "__main__":
    main()