def anti_vowel(text):
    t=""
    for c in text:
        for i in "ieaouIEAOU":
            if c==i:
                c=""
            else:
                c=c
        t=t+c
    return t

print(anti_vowel("hello"))
print(anti_vowel("goodbye"))
