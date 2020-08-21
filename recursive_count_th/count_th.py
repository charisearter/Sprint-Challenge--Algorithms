'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # make counter
    counter = word.find('th')  # see if th is there

    if counter != -1:
        return 1 + count_th(word[counter+2:])  # go ahead 2 letters
    else:
        return 0  # if there isn't anything return 0

    # make input all lowercase //took off because gave error
    # check if letter is a t (possibly use regEx) //no need used find method for strings
    # if yes, check that index + 1 and see if it is an //used find()
    # if yes add +1 to counter
    # if no go to next
    # possibly use the count method for this becaue no loops //NOPE gave issues
    # use find() for strings
