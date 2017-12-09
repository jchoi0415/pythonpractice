'''
Write code which will find the words for the given index
e.g. If the sentence is 'Hello my name is Choiboy', and firstindex = 2, secondindex = 5
word1 is 'my' and word2 is 'Choiboy'.
HINT: Split the sentence into separate words using space/whitespace.
HINT2: The english index and coding list array index is different. English index starts at 1 but coding index starts
at 0. The numbers you are given in this challenge is in english index so make sure you are checking for the correct
index when using that for code

This function requires two words as results. Check answer1 and answer2 for an idea of the answer format
REMEMBER GOOGLE IS YOUR BEST FRIEND AND MAKE USE OF PRINT DEBUGGING FOR ALL CODING PURPOSES
'''


def whatstheword(sentence, firstindex, secondindex):
    # Write code from below here! I initialised the words you can use to return (but feel free to change it however)
    word1 = ''
    word2 = ''

    return word1, word2


def main():
    answerCounter = 0
    numofCase = 2

    output1a, output1b = whatstheword("I am your teacher and we are going to learn about strings today", 4, 12)
    answer1a = 'teacher'
    answer1b = 'strings'

    output2a, output2b = whatstheword("I hope you are not struggling too much though", 2, 9)
    answer2a = 'hope'
    answer2b = 'though'

    if output1a == answer1a and output1b == answer1b:
        print('Congratz! 1st case 둘다 맞았거든')
        answerCounter += 1
    elif output1a != answer1a and output1b != answer1b:
        print('빼애애애액! 1st case 둘다 틀렸거든... 고쳐봐 ㅋㅋ')
    elif output1a != answer1a:
        print('빼애애애액! 1st case word1 틀렸거든... 고쳐봐 ㅋㅋ')
    elif output1b != answer1b:
        print('빼애애애액! 1st case word2 틀렸거든... 고쳐봐 ㅋㅋ')

    if output2a == answer2a and output2b == answer2b:
        print('Congratz! 2nd case 둘다 맞았거든')
        answerCounter += 1
    elif output2a != answer2a and output2b != answer2b:
        print('빼애애애액! 2nd case 둘다 틀렸거든... 고쳐봐 ㅋㅋ')
    elif output2a != answer2a:
        print('빼애애애액! 2nd case word1 틀렸거든... 고쳐봐 ㅋㅋ')
    elif output2b != answer2b:
        print('빼애애애액! 2nd case word2 틀렸거든... 고쳐봐 ㅋㅋ')

    print('You got ' + str(answerCounter) + ' out of ' + str(numofCase) + ' questions correct')


if __name__ == "__main__":
    main()