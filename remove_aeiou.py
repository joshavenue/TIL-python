def disemvowel(word):
    vowels = "aeiouAEIOU"
    my_list = list(word)
    for char in word:             
        if char in vowels:
            my_list.remove(char)
        else:
            pass
    word = ''.join(my_list)
    return word
