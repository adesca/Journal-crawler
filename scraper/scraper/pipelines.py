# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pickle
from scrapy.exceptions import DropItem
import os
import collections
import re

class dropper(object):
    def process_item(self,item,spider):
        if(item["article"] == "true" and item["articleText"] != None):
            pass
        else:
            raise DropItem("Invalid")

class ScraperPipeline(object):
    def process_item(self, item, spider):
        return item

class saveInformationPipe(object):
    def getBadWords(self):
        wordList = []
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "scraper\\wordList.txt"
        abs_file_path = os.path.join(os.path.dirname(os.path.dirname(script_dir)),rel_path)

        with open(abs_file_path) as f:
            for line in f:
                wordList.append(line.strip())
        return wordList

    def cleanseWords(self,listOWords):
        badWords = self.getBadWords();
        return [x for x in listOWords if x not in badWords]

    def getWords(self,bagOWords):
        return self.cleanseWords(bagOWords.lower().split(" "))

    def getYear(self,dateString):
        return re.findall(r'\d+', dateString)[1]

    def process_item(self,item,spider):
        if(item["article"] == "true" and item["articleText"] != None):
            remainingWords = self.getWords(item['articleText'])
            c = collections.Counter(remainingWords)
            year = self.getYear(item['date'])

            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "scraper\\results.pkl"
            abs_file_path = os.path.join(os.path.dirname(os.path.dirname(script_dir)),rel_path)
            with open(abs_file_path, 'wb+') as file:
                try:
                    counts = pickle.load(file)
                except EOFError:
                    counts = {}

                for key in c:
                    if key in counts:
                        temp = counts[key] #where the dict value is another dict of years/accompanying counts
                        if year in temp:
                            temp[year] = temp[year]+c[key]
                        else:
                            temp[year] = c[key]
                    else:
                        temp = { year:c[key]}
                        counts[key] = temp
            with open(abs_file_path,'wb+') as file:
                pickle.dump(counts, file, -1)
        else:
            raise DropItem("Not an article page.")
