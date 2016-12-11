from collections import Counter
import json
import re
from wordcloud import WordCloud
from PIL import Image
import numpy as np

def getBadWords():
    wordList = []
    rel_path = "badWordList.txt"

    with open(rel_path) as f:
        for line in f:
            wordList.append(line.strip())
    return wordList

def getWords(stringOWords):
    badWords = getBadWords();
    listOWords = stringOWords.lower().split(' ')
    return set([word for word in listOWords if word not in badWords])

def main():
    c = Counter()
    with open("text.jl") as f:
        for line in f:
            tempDict = json.loads(line)
            if tempDict["articleText"] is not None:
                words = getWords((tempDict["articleText"]+" "+tempDict["title"][0]))
            for word in words:
                c[word] += 1
    with open("articleLinks.jl") as f:
        for index,line in enumerate(f):
            if index > 314:
                tempDict = json.loads(line)
                if tempDict["Title"]:
                    words = getWords(tempDict["Title"][0])
                    for word in words:
                        c[word] += 1
    
    wordCloudString = ""
    for element in c.elements():
        wordCloudString += element+" "
		
    mask = np.array(Image.open("pride flag.png"))
    wordcloud = WordCloud(mask=mask).generate(wordCloudString)
    image = wordcloud.to_image()
    image.save("prideCloud.bmp")
    image.show()
    
    print(c['transgender']);

if __name__ == '__main__':
    main()
