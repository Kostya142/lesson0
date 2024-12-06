def single_root_words (root_word, *other_words):
    same_words=[]
    for i in other_words :
        if root_word.lower() in i.lower():
           same_words.append(i)
    if len(same_words)==0:
        for i in other_words:
            if i.lower() in root_word.lower():
                same_words.append(i)
    return same_words

print(single_root_words("род", 'родина','родня','родимый','родовед','родословие','родственник',
'прородина','борода','продукты','продавец','смородина','родник'))












