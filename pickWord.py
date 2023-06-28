import requests
import random


def getWordList():
    word_list =list()
    url  = "http://norvig.com/ngrams/sowpods.txt" #source url with words
   
    get_site = requests.get(url)
    get_site = get_site.text
    words =  get_site.split()
    for w in words:
        if len(w)>10:
            if word_list==None:
                word_list=[w]
            else:
                word_list.append(w)
        else:
            continue
    #print(len(word_list)) # q elementów listy
    return word_list
    

def randomWord():
    word_list = getWordList()
    pick_word = word_list[random.randint(0,len(word_list))]
    return pick_word


if __name__ == "__main__":
    
    print(randomWord())
    