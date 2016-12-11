## Synopsis

A project that goes through the Journal of Homosexuality's history on [tandfonline](http://www.tandfonline.com/loi/wjhm20) and then generates a graph of word usage, ~~using BokehJS (TBD)~~ using a wordcloud (see below).
This project really isn't meant to be used for accessing Taylor & Francis's website.
I wasn't able to finish the project because the site explicitly blocked me from accessing it, and rather than try to get around that I
wanted to respect the fact that I've made too many requests in the last few days.

So I took the words that I had scraped and turned them into a wordcloud. I think the final result is interesting.
I was ultimately able to get the words for the abstracts from 2012-2015, in addition to all of the titles.
The project currently goes over all of the words and runs them through a counter to print
the top five words in addition to saving the wordcloud as an image.

The current top five words used (on a per article basis) are:
1. gay - 386
2. sexual - 293
3. men - 205
4. lesbian - 190
5. social - 143

![word cloud of word use frequencies](https://github.com/adesca/Journal-crawler/blob/master/text%20parser/wordCloud.bmp "Word cloud")


### Documentation
* scraper/ - contains the scraper's code. There are a couple of spiders with differing roles based on what I needed at the time.
  I don't want to go over it because this project should not be used for scraping.
* text parser/ - contains a parser script that goes over the results I have and collects the word counts in addition to generating the cloud.
* badWordList.txt - list of words that are excluded from counting word usage.
  If you want to increase it just add a word to its own line.
* text.jl - a list of json formatted objects, one per line, of each of the articles I could get (the most recent 315).
* articleLinks.jl - Another jsonlist, but this one contains every article's title and accompanying link.


## Libraries used
I used scrapy and [word_cloud](https://github.com/amueller/word_cloud)

## License

This project uses the MIT license so that when it does show its data, later, others can play around with it.
The MIT licenses for other stuff used in this project is in the license section.
