'''
Write code which will find all such numbers which will return the squared number give to you
The numbers are given to you in a list and you are to use a dictionary to show the results.

This function requires a dict of all the numbers and it's squared numbers.
Check answer1 for an idea of the answer format
REMEMBER GOOGLE IS YOUR BEST FRIEND AND MAKE USE OF PRINT DEBUGGING FOR ALL CODING PURPOSES
'''


def squaremynumber(mylist):
    # Write code from below here! I initialised the dict you can use to return (but feel free to change it however)
    d = dict()

    return d


def main():
    answerCounter = 0
    numofCase = 1

    output1 = squaremynumber(list(range(1, 50)))
    answer1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196,
               15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400, 21: 441, 22: 484, 23: 529, 24: 576, 25: 625,
               26: 676, 27: 729, 28: 784, 29: 841, 30: 900, 31: 961, 32: 1024, 33: 1089, 34: 1156, 35: 1225, 36: 1296,
               37: 1369, 38: 1444, 39: 1521, 40: 1600, 41: 1681, 42: 1764, 43: 1849, 44: 1936, 45: 2025, 46: 2116,
               47: 2209, 48: 2304, 49: 2401}

    if output1 == answer1:
        print('Congratz! 1st case 맞았거든')
        answerCounter += 1
    else:
        print('빼애애애액! 1st case 틀렸거든... 고쳐봐 ㅋㅋ')

    print('You got ' + str(answerCounter) + ' out of ' + str(numofCase) + ' questions correct')


if __name__ == "__main__":
    main()