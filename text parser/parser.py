from collections import Counter
import json
import re
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np

def getBadWords():
    wordList = []
    rel_path = "badWordList.txt"

    with open(rel_path) as f:
        for line in f:
            wordList.append(line.strip())
    return wordList

def getWords(stringOWords,badWords):
    listOWords = stringOWords.lower().split(' ')
    return set([word for word in listOWords if word not in badWords and "_" not in word])

def main():
    c = Counter()
    badWords = getBadWords()
    with open("text.jl") as f:
        for line in f:
            tempDict = json.loads(line)
            if tempDict["articleText"] is not None:
                words = getWords((tempDict["articleText"]+" "+tempDict["title"][0]), badWords)
                for word in words:
                    c[word] += 1
    with open("articleLinks.jl") as f:
        for line in f.readlines()[314:]:
            tempDict = json.loads(line)
            if tempDict["Title"]:
                words = getWords(tempDict["Title"][0], badWords)
                for word in words:
                    c[word] += 1

    wordCloudString = ""
    for element in c.elements():
        wordCloudString += element+" "

    mask = np.array(Image.open("pride flag.png"))

    wordcloud = WordCloud(mask=mask,color_func = ImageColorGenerator(mask), prefer_horizontal = 1).generate(wordCloudString)

    image = wordcloud.to_image()
    image.save("prideCloud2.bmp")
    image.show()

    print(c['transgender']);

if __name__ == '__main__':
    main()
