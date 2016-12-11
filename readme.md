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

## Libraries used
I used scrapy and [word_cloud](https://github.com/amueller/word_cloud)

## License

This project uses the MIT license so that when it does show its data, later, others can play around with it.
The MIT licenses for other stuff used in this project is in the license section.
