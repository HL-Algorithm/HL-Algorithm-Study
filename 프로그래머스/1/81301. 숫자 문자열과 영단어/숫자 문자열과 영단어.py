def solution(s):

    word_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", 
                 "four": "4", "five": "5", "six": "6", 
                 "seven": "7", "eight": "8", "nine": "9"}


    for word in word_dict:
        if word in s: 
            s = s.replace(word, word_dict[word])  
    return int(s)