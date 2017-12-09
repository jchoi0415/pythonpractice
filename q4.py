'''
Author: Jack Choi
Date: 10/12/17

Write code which will find the longest word with its coding index number
e.g. If the sentence is 'Hello my name is Choiboy', the longest word would be 'Choiboy' at wordindex = 4

HINT: Split the sentence into separate words using space/whitespace then iterating through each word
HINT2: If there are two longest words (same max length), please get the one that has a lower index number
HINT3: Return the index number in terms of coding indexing (assuming index starts at 0)
HINT4:

This function requires a word and index as results. Check answer1 and answer2 for an idea of the answer format
REMEMBER GOOGLE IS YOUR BEST FRIEND AND MAKE USE OF PRINT DEBUGGING FOR ALL CODING PURPOSES
'''


# You only have to modify the function below. Do not modify main function or anything below it
def whatstheword(sentence):
    # Write code from below here! I initialised the variables you can use to return (but feel free to change it however)
    longestword = ''
    wordindex = 0

    return longestword, wordindex


def main():
    answerCounter = 0
    numofCase = 2

    output1a, output1b = whatstheword("I am your teacher and we are going to learn about strings today")
    answer1a = 'teacher'
    answer1b = 3

    output2a, output2b = whatstheword("I hope you are not struggling too much though")
    answer2a = 'struggling'
    answer2b = 5

    if output1a == answer1a and output1b == answer1b:
        print('Congratz! 1st case 둘다 맞았거든')
        answerCounter += 1
    elif output1a != answer1a and output1b != answer1b:
        print('빼애애애액! 1st case 둘다 틀렸거든... 고쳐봐 ㅋㅋ')
    elif output1a != answer1a:
        print('빼애애애액! 1st case word 틀렸거든... 고쳐봐 ㅋㅋ')
    elif output1b != answer1b:
        print('빼애애애액! 1st case wordindex 틀렸거든... 고쳐봐 ㅋㅋ')

    if output2a == answer2a and output2b == answer2b:
        print('Congratz! 2nd case 둘다 맞았거든')
        answerCounter += 1
    elif output2a != answer2a and output2b != answer2b:
        print('빼애애애액! 2nd case 둘다 틀렸거든... 고쳐봐 ㅋㅋ')
    elif output2a != answer2a:
        print('빼애애애액! 2nd case word 틀렸거든... 고쳐봐 ㅋㅋ')
    elif output2b != answer2b:
        print('빼애애애액! 2nd case wordindex 틀렸거든... 고쳐봐 ㅋㅋ')

    print('You got ' + str(answerCounter) + ' out of ' + str(numofCase) + ' questions correct')


if __name__ == "__main__":
    main()