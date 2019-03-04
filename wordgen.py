from text_break import text_break
import random

letters = text_break()
letters.set_file("shakespeare.txt")
letters.set_chars("qwertyuiopasdfghjklzxcvbnm ")
letters.run()
l_freq = letters.get_letter_freq()
print("analysis done")

def gen(start = "w", length = 8):
    word = ""

    p = random.random()
    cumulative_p = 0

    for s_letter in l_freq[" "]:
        cumulative_p += l_freq[" "][s_letter]

        if p <= cumulative_p:
            word += s_letter
            break

    while word[-1] != " ":
##  while len(word) < length:
        p = random.random()
        cumulative_p = 0
        
        for s_letter in l_freq[word[-1]]:
            cumulative_p += l_freq[word[-1]][s_letter]

            if p <= cumulative_p:
                word += s_letter
                #print("letter added")
                break
    print(word)